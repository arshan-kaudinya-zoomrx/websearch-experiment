"""Luna layer: turn one arm's links (a search run, or a Jev filter folder) into Luna answers with the
production synthesis prompt (data/prompts.py), then score the answers with code-only metrics.

outputs/synth/<ts>__luna-<config>__on__<source_id>/{synth.json,results.jsonl,summary.json,answers.md}

No search or Jev calls are made: links come from the source folder. One LLM call per row; a row
whose links were all dropped by Jev (abstain) is not sent to Luna and is recorded as has_answer "no".
Metric definitions are in docs/METHODOLOGY.md ("Luna answers").
"""

from __future__ import annotations

import asyncio
import hashlib
import importlib.util
import json
import platform
import re
import statistics
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import httpx
import yaml

from . import FILTERS_DIR, ROOT, RUNS_DIR, SYNTH_DIR, __version__, llm
from .config import deep_merge, load_file, set_dotted
from .dataset import normalize, select_rows
from .filtering import candidates, is_competitor
from .metrics import load_records, pct, rate
from .runner import slug

LUNA_DEFAULTS: dict = {
    "name": "unnamed",
    "prompt": {"path": "data/prompts.py", "version": "enrich-v8"},
    "as_of": "2026-10-06",
    "evidence": {"max_items": 10, "max_chars_per_item": 3000},
    "facet_overrides": "data/facet_overrides.yaml",
    "facets": [],      # ordered [{pattern, facet, scope}], first match wins; see configs/luna_openai.yaml
    "llm": {"model": None, "temperature": None, "reasoning_effort": None, "max_completion_tokens": 4000,
            "seed": None, "timeout_s": 120, "retries": 2,
            "pricing": {"per_1m_input_tokens": 0, "per_1m_cached_input_tokens": None, "per_1m_output_tokens": 0}},
    "run": {"concurrency": 4, "max_cost_usd": 2.0},
}
REQUIRED_KEYS = ("has_answer", "summarized_answer", "missing", "citations", "next_queries")
EST_OUTPUT_TOKENS = 700  # per answer, for --dry-run only


def build_luna_config(path: str | Path | None, sets: list[str] | None = None) -> dict:
    cfg = deep_merge(LUNA_DEFAULTS, load_file(path) if path else {})
    for s in sets or []:
        set_dotted(cfg, s)
    return cfg


# ---------- the production prompt ----------

def load_prompts(cfg: dict):
    """Import data/prompts.py by path so the prompt is never copied (prompt edits stay in one place)."""
    path = ROOT / cfg["prompt"]["path"]
    spec = importlib.util.spec_from_file_location("luna_prompts", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.SHA256 = hashlib.sha256(path.read_bytes()).hexdigest()
    return mod


def load_facet_overrides(cfg: dict) -> dict:
    path = ROOT / (cfg.get("facet_overrides") or "")
    if not cfg.get("facet_overrides") or not path.exists():
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def facet_of(row_id: str, objective: str, cfg: dict, overrides: dict | None = None) -> tuple[str | None, str | None]:
    """(facet, scope) for build_system: an override for the row, else the first matching pattern, else core."""
    o = (overrides or {}).get(row_id)
    if o:
        return o.get("facet"), o.get("scope")
    for rule in cfg.get("facets") or []:
        if re.search(rule["pattern"], objective or "", re.I):
            return rule.get("facet"), rule.get("scope")
    return None, None


def subject_of(anchors: list[str]) -> str:
    names = list(dict.fromkeys(a for a in anchors or [] if a))
    if not names:
        return "(unknown)"
    return names[0] + (f"\nalso known as: {'; '.join(names[1:])}" if names[1:] else "")


def clip_text(text: str | None, max_chars: int) -> str:
    """Collapse whitespace, then cut at a word boundary. The one text view Luna, the metrics and the judge share."""
    text = " ".join((text or "").split())
    if max_chars and len(text) > max_chars:
        text = text[:max_chars].rsplit(" ", 1)[0] + " ..."
    return text


def format_evidence(items: list[dict], max_chars: int) -> str:
    """[E1].. blocks: source line, title, url, date header, then the text. Assumed to match production."""
    blocks = []
    for i, x in enumerate(items, start=1):
        text = clip_text(x.get("snippet"), max_chars)
        lines = [f"[E{i}] source: web ({x.get('domain') or '-'})", f"title: {x.get('title') or '-'}",
                 f"url: {x.get('url') or '-'}"]
        if x.get("date"):
            lines.append(f"date: {x['date']}")
        lines.append(text)
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks)


# ---------- sources (one arm) ----------

def source_kind(d: Path) -> str:
    if (d / "filter.json").exists():
        return "filter"
    if (d / "run.json").exists():
        return "run"
    raise SystemExit(f"{d} is neither a search run (run.json) nor a Jev filter folder (filter.json)")


def _run_cost_per_request(run_dir: Path) -> float:
    s = run_dir / "summary.json"
    if not s.exists():
        return 0.0
    d = json.loads(s.read_text(encoding="utf-8"))
    return float(d.get("cost_usd") or 0) / max(1, int(d.get("n_requests") or 1))


def load_source(d: Path, rows: str | None = None) -> dict:
    """Per row: the links Luna sees, in the arm's order, plus timing and cost of getting them."""
    kind = source_kind(d)
    meta = json.loads((d / ("filter.json" if kind == "filter" else "run.json")).read_text(encoding="utf-8"))
    if kind == "filter":
        run_id = meta["source_run_id"]
        run_dir = next((p for p in (RUNS_DIR / run_id, d.parent / run_id) if (p / "run.json").exists()), RUNS_DIR / run_id)
        run_meta = json.loads((run_dir / "run.json").read_text(encoding="utf-8")) if run_dir.exists() else {}
        search_cpr = _run_cost_per_request(run_dir)
    else:
        run_id, run_meta, search_cpr = d.name, meta, _run_cost_per_request(d)
    rcfg = run_meta.get("config") or {}
    provider = rcfg.get("provider", "?")
    tier = (rcfg.get("params") or {}).get("search_type") or (rcfg.get("params") or {}).get("mode") or "-"
    arm = f"{provider}-{tier}/{rcfg.get('mode', '?')}" + (" + jev" if kind == "filter" else "")

    # Every row in the source is kept, failed ones included, so all arms share one denominator.
    by_row: dict[str, list[dict]] = defaultdict(list)
    for r in load_records(d):
        if r.get("repeat", 0) == 0:
            by_row[r["row_id"]].append(r)
    wanted = set(by_row)
    if rows:
        wanted = {q["id"] for q in select_rows([{"id": i} for i in sorted(by_row)], rows)}

    out = {}
    for row_id in sorted(wanted):
        all_recs = sorted(by_row[row_id], key=lambda r: r["case_id"])
        recs = [r for r in all_recs if r.get("ok")]
        first = all_recs[0]
        row = {"row_id": row_id, "objective": first["objective"], "anchors": first.get("anchors") or [],
               "items": [], "skip": None, "source_error": None, "search_ms": 0.0, "jev_ms": 0.0,
               "search_cost": search_cpr * len(all_recs), "jev_cost": 0.0}
        if not recs:  # search (or Jev) failed for the whole row: not an abstain, an error
            row.update(skip="source_error", source_error=str(first.get("error") or "failed"))
        elif kind == "filter":
            kept = [x for r in recs for x in r["results"] if x.get("kept")]
            kept.sort(key=lambda x: -(x.get("jev_score") or 0))
            row["items"] = candidates(kept)
            row.update(jev_ms=max(r["jev_latency_ms"] for r in recs),
                       jev_cost=sum(r.get("cost_usd") or 0 for r in recs),
                       search_ms=max(r["search_latency_ms"] for r in recs))
            if not row["items"]:
                row["skip"] = "jev_abstain" if any(r["results"] for r in recs) else "no_links"
        else:
            # Interleave several lists by rank (rank 1 of each list first), then dedupe by URL.
            flat = [(x.get("rank", 0), i, j, x) for i, r in enumerate(recs) for j, x in enumerate(r["results"])]
            row["items"] = candidates([x for *_, x in sorted(flat, key=lambda t: t[:3])])
            row["search_ms"] = max(r["latency_ms"] for r in recs)
            if not row["items"]:
                row["skip"] = "no_links"
        out[row_id] = row
    return {"kind": kind, "source_id": d.name, "source_run_id": run_id, "arm": arm, "rows": out}


# ---------- one row ----------

def build_messages(prompts, row: dict, cfg: dict, overrides: dict | None = None) -> dict:
    facet, scope = facet_of(row["row_id"], row["objective"], cfg, overrides)
    items = row["items"][: int(cfg["evidence"]["max_items"])]
    evidence = format_evidence(items, int(cfg["evidence"]["max_chars_per_item"]))
    system = prompts.build_system(facet, scope)
    user = prompts.build_user(row["objective"], row["objective"], subject_of(row["anchors"]), cfg["as_of"], evidence)
    return {"facet": facet, "scope": scope, "items": items, "evidence_chars": len(evidence),
            "system": system, "user": user}


def _evidence_view(items: list[dict], max_chars: int) -> list[dict]:
    return [{"id": f"E{i}", "url": x.get("url"), "domain": x.get("domain"), "title": x.get("title"),
             "date": x.get("date"), "text": clip_text(x.get("snippet"), max_chars)}
            for i, x in enumerate(items, start=1)]


NO_EVIDENCE = {"jev_abstain": "no web evidence passed the filter", "no_links": "the search returned no links"}
SKIP_LABEL = {"jev_abstain": "ABSTAIN (Jev kept nothing)", "no_links": "NO LINKS (search returned nothing)",
              "source_error": "SOURCE ERROR (search/Jev failed)"}


async def synth_row(client: httpx.AsyncClient, prompts, row: dict, cfg: dict, overrides: dict | None = None) -> dict:
    """skip: jev_abstain / no_links -> Luna not called, has_answer "no" (production renders "No data available");
    source_error -> Luna not called, the row is an error. A failed Luna call is an error too, never a "no"."""
    m = build_messages(prompts, row, cfg, overrides)
    skip = row["skip"]
    base = {"row_id": row["row_id"], "objective": row["objective"], "anchors": row["anchors"],
            "facet": m["facet"], "scope": m["scope"], "skip": skip, "abstained": skip == "jev_abstain",
            "n_items": len(m["items"]), "evidence_chars": m["evidence_chars"],
            "evidence": _evidence_view(m["items"], int(cfg["evidence"]["max_chars_per_item"]))}
    if skip == "source_error":
        resp = llm.LLMResponse(False, 0.0, error=f"source failed: {row['source_error']}"[:300])
    elif skip:
        resp = llm.LLMResponse(True, 0.0, parsed={"has_answer": "no", "summarized_answer": "", "confident_score": None,
                                                    "missing": NO_EVIDENCE[skip], "citations": [], "next_queries": []})
    else:
        resp = await llm.complete(client, cfg["llm"], m["system"], m["user"])
    luna_cost = llm.cost_usd(cfg["llm"], resp.usage)
    timing = {"search_ms": row["search_ms"], "jev_ms": row["jev_ms"], "luna_ms": round(resp.latency_ms, 1)}
    timing["total_ms"] = round(sum(timing.values()), 1)
    return {**base, "ok": resp.ok, "error": resp.error, "status": resp.status, "attempts": resp.attempts,
            "usage": resp.usage, "timing": timing, "luna_wall_ms": round(resp.wall_ms or resp.latency_ms, 1),
            "cost_usd": {"search": round(row["search_cost"], 6), "jev": round(row["jev_cost"], 6),
                         "luna": round(luna_cost, 6)},
            "output": resp.parsed, "raw_text": None if resp.parsed else resp.text,
            "metrics": answer_metrics(resp.parsed, base["evidence"], row["anchors"], row["objective"])}


# ---------- objective metrics (code only) ----------

TAG_RE = re.compile(r"\[E(\d+)\]")
URL_RE = re.compile(r"https?://|www\.\w", re.I)
SEARCH_TALK_RE = re.compile(
    r"(the|supplied|provided|available|retrieved) (evidence|items|sources|documents)\b[^.]{0,40}\b"
    r"(does not|do not|doesn't|don't|did not|provides? no|contains? no|is silent|are silent|lacks?)"
    r"|not (available|reported|stated|mentioned|found|identified) in the (supplied|provided|searched|available|retrieved)"
    r"|\b(document index|structured database|search results?|the search)\b"
    r"|\bno (results|data|information|evidence)\b[^.]{0,40}\b(were|was|is|are) (found|retrieved|reported|identified)",
    re.I)
NUM_RE = re.compile(r"(?<![\w.])\d+(?:[.,]\d+)*%?")
CODE_RE = re.compile(r"\b[A-Za-z]{1,10}-?\d[\w-]*\b")  # SOR102, NCT05156125, HEC-234055 (no "with 30")
PROPER_RE = re.compile(r"(?<![.!?:]\s)(?<!^)\b[A-Z][a-zA-Z]{2,}(?:[- ][A-Z][a-zA-Z]+)*\b")
COMMON_CAPS = {"The", "This", "These", "Phase", "Grade", "Study", "Trial", "Data", "Results", "In", "No", "And",
               "Both", "Each", "Its", "It", "With", "For", "As", "At", "On", "Of", "An", "Patients", "Mice",
               "Treatment", "Monotherapy", "Combination", "Preclinical", "Clinical", "Animal"}


def claim_tokens(answer: str) -> list[str]:
    """Numbers, alphanumeric codes and mid-sentence capitalised names: what must be literally in the evidence."""
    text = TAG_RE.sub(" ", answer or "")
    toks = [t for t in NUM_RE.findall(text) if len(t.rstrip("%").replace(",", "").replace(".", "")) >= 2]
    toks += [t for t in CODE_RE.findall(text) if any(c.isalpha() for c in t)]
    toks += [t for t in PROPER_RE.findall(text) if t not in COMMON_CAPS]
    return list(dict.fromkeys(toks))


def answer_metrics(out: dict | None, evidence: list[dict], anchors: list[str], objective: str) -> dict:
    if out is None:
        return {"json_valid": False}
    answer = str(out.get("summarized_answer") or "")
    has = str(out.get("has_answer", "")).strip().lower() == "yes"
    n = len(evidence)
    tags = [int(t) for t in TAG_RE.findall(answer)]
    cited = sorted({t for t in tags if 1 <= t <= n})
    ev_norm = normalize(" ".join(f"{e.get('title') or ''} {e.get('url') or ''} {e.get('text') or ''}" for e in evidence))
    toks = claim_tokens(answer) if has else []
    ungrounded = [t for t in toks if normalize(t) and normalize(t) not in ev_norm]
    queries = [q for q in (out.get("next_queries") or []) if isinstance(q, str)]
    anchor_norms = [normalize(a) for a in anchors or [] if normalize(a)]
    subject_first = [any(normalize(q[:60]).startswith(a) or a in normalize(" ".join(q.split()[:3]))
                         for a in anchor_norms) for q in queries]
    cited_text = normalize(" ".join(f"{evidence[t - 1].get('title') or ''} {evidence[t - 1].get('text') or ''}"
                                    for t in cited))
    return {
        "json_valid": all(k in out for k in REQUIRED_KEYS) and (not has or "confident_score" in out),
        "has_answer": has,
        "answer_chars": len(answer),
        "confident_score": out.get("confident_score") if has else None,
        "missing_nothing": str(out.get("missing", "")).strip().lower().rstrip(".") == "nothing",
        "missing_empty": not str(out.get("missing", "")).strip(),
        "n_tags": len(tags),
        "invalid_tags": sorted({t for t in tags if not 1 <= t <= n}),
        "uncited_answer": has and not tags,
        "n_cited_items": len(cited),
        "cited_domains": sorted({evidence[t - 1].get("domain") or "" for t in cited}),
        "url_in_answer": bool(URL_RE.search(answer)),
        "search_talk": [m.group(0) for m in SEARCH_TALK_RE.finditer(answer)][:3],
        "nonempty_when_no": (not has) and bool(answer.strip()),
        "claim_tokens": len(toks),
        "ungrounded_tokens": ungrounded[:15],
        "n_ungrounded": len(ungrounded),
        "names_subject": any(a in normalize(answer) for a in anchor_norms),
        "subject_in_cited": any(a in cited_text for a in anchor_norms),
        "next_queries": len(queries),
        "next_queries_subject_first": sum(subject_first),
    }


def summarize_synth(records: list[dict], competitor_cfg: dict | None = None) -> dict:
    """Rates are over ALL rows of the source (errors included), so arms share one denominator."""
    n = len(records)
    m = [r["metrics"] for r in records]
    valid = [x for x in m if x.get("json_valid")]
    answered = [r for r in records if r["metrics"].get("has_answer")]
    called = [r for r in records if not r.get("skip")]                   # Luna was called
    replied = [r for r in called if r["ok"] or r.get("error") == "invalid JSON"]  # ...and returned text
    luna_ok = [r for r in called if r["ok"]]
    timed = [r for r in records if r.get("skip") != "source_error"]
    skips = Counter(r.get("skip") for r in records)
    own = [r for r in answered if not is_competitor(r["objective"], competitor_cfg or {"target": {
        "competitor_pattern": r"competing agents|competitors?\b|drugs approved against the target"}})]
    toks = sum(r["metrics"]["claim_tokens"] for r in answered)
    ungr = sum(r["metrics"]["n_ungrounded"] for r in answered)
    nq = sum(x.get("next_queries", 0) for x in valid)

    def lat(key, rs):
        v = [r["timing"][key] for r in rs]
        return {"p50": pct(v, 0.5), "p95": pct(v, 0.95), "mean": round(statistics.fmean(v), 1) if v else None}

    cost = {k: round(sum(r["cost_usd"][k] for r in records), 4) for k in ("search", "jev", "luna")}
    by_facet: dict[str, list[dict]] = defaultdict(list)
    for r in records:
        by_facet[r["facet"] or "core"].append(r)
    return {
        "n_rows": n,
        "errors": dict(Counter(r["error"][:60] for r in records if r.get("error"))),
        "answering": {
            "answer_rate": rate(len(answered), n),
            "jev_abstain_rate": rate(skips["jev_abstain"], n),
            "no_links_rate": rate(skips["no_links"], n),
            "luna_no_rate": rate(sum(1 for r in luna_ok if not r["metrics"].get("has_answer")), n),
            "error_rate": rate(sum(1 for r in records if not r["ok"]), n),  # source failed or Luna call failed
            "complete_rate": rate(sum(r["metrics"].get("missing_nothing", False) for r in answered), len(answered)),
            "confident_mean": round(statistics.fmean([r["metrics"]["confident_score"] for r in answered
                                                      if isinstance(r["metrics"].get("confident_score"), (int, float))]
                                                     or [0]), 3),
            "answer_chars_mean": round(statistics.fmean([r["metrics"]["answer_chars"] for r in answered] or [0]), 0),
        },
        "contract": {
            "json_valid_rate": rate(sum(1 for r in replied if r["metrics"].get("json_valid")), len(replied)),
            "invalid_tag_rows": rate(sum(1 for x in valid if x["invalid_tags"]), n),
            "uncited_answer_rows": rate(sum(1 for x in valid if x["uncited_answer"]), len(answered)),
            "url_in_answer_rows": rate(sum(1 for x in valid if x["url_in_answer"]), n),
            "search_talk_rows": rate(sum(1 for x in valid if x["search_talk"]), n),
            "nonempty_when_no_rows": rate(sum(1 for x in valid if x["nonempty_when_no"]), n),
            "missing_empty_rows": rate(sum(1 for x in valid if x["missing_empty"]), n),
            "next_queries_subject_first": rate(sum(x.get("next_queries_subject_first", 0) for x in valid), nq),
        },
        "grounding": {
            "claim_tokens_per_answer": round(toks / len(answered), 1) if answered else 0,
            "ungrounded_token_rate": rate(ungr, toks),
            "answers_with_ungrounded": rate(sum(1 for r in answered if r["metrics"]["n_ungrounded"]), len(answered)),
        },
        "subject": {
            "rows_judged": len(own),
            "names_subject": rate(sum(r["metrics"]["names_subject"] for r in own), len(own)),
            "subject_in_cited": rate(sum(r["metrics"]["subject_in_cited"] for r in own), len(own)),
        },
        "evidence_use": {
            "items_given_mean": round(statistics.fmean([r["n_items"] for r in records] or [0]), 2),
            "evidence_chars_mean": round(statistics.fmean([r["evidence_chars"] for r in records] or [0]), 0),
            "items_cited_mean": round(statistics.fmean([r["metrics"]["n_cited_items"] for r in answered] or [0]), 2),
            "domains_cited": len({d for r in answered for d in r["metrics"]["cited_domains"]}),
        },
        "timing_ms": {k.removesuffix("_ms"): lat(k, timed) for k in ("search_ms", "jev_ms", "luna_ms", "total_ms")},
        "luna_timing_ms_called": lat("luna_ms", luna_ok),
        "tokens": {"input_mean": round(statistics.fmean([r["usage"]["input_tokens"] for r in called] or [0]), 0),
                   "output_mean": round(statistics.fmean([r["usage"]["output_tokens"] for r in called] or [0]), 0)},
        "cost_usd": {**cost, "total": round(sum(cost.values()), 4),
                     "per_row": round(sum(cost.values()) / n, 5) if n else None,
                     "per_answer": round(sum(cost.values()) / len(answered), 5) if answered else None},
        "by_facet": {f: {"n": len(rs), "answer_rate": rate(sum(r["metrics"].get("has_answer", False) for r in rs), len(rs))}
                     for f, rs in sorted(by_facet.items())},
    }


# ---------- a whole arm ----------

def plan_synth(source_dir: Path, cfg: dict, rows: str | None = None) -> dict:
    src = load_source(source_dir, rows)
    prompts, overrides = load_prompts(cfg), load_facet_overrides(cfg)
    est_in = n_calls = 0
    facets = {}
    for r in src["rows"].values():
        msg = build_messages(prompts, r, cfg, overrides)
        facets[r["row_id"]] = (msg["facet"] or "core") + (f"/{msg['scope']}" if msg["scope"] else "")
        if not r["skip"]:
            n_calls += 1
            est_in += llm.estimate_tokens(msg["system"] + msg["user"])
    usage = {"input_tokens": est_in, "output_tokens": EST_OUTPUT_TOKENS * n_calls}
    return {"source": src, "prompts": prompts, "overrides": overrides, "facets": facets, "n_rows": len(src["rows"]),
            "n_calls": n_calls, "est_input_tokens": est_in, "est_cost_usd": round(llm.cost_usd(cfg["llm"], usage), 4)}


def _out_dir(cfg: dict, source_id: str, out_root: Path | None) -> Path:
    root = out_root or SYNTH_DIR
    base = f"{datetime.now():%Y%m%d-%H%M%S}__luna-{slug(cfg['name'])}__on__{source_id}"
    d, n = root / base, 2
    while d.exists():
        d, n = root / f"{base}-{n}", n + 1
    d.mkdir(parents=True)
    return d


async def _execute(p: dict, cfg: dict, out_path: Path, transport: httpx.AsyncBaseTransport | None) -> list[dict]:
    sem = asyncio.Semaphore(int(cfg["run"]["concurrency"]))
    rows = list(p["source"]["rows"].values())
    records: list[dict] = []
    async with httpx.AsyncClient(transport=transport) as client:

        async def one(row):
            async with sem:
                return await synth_row(client, p["prompts"], row, cfg, p["overrides"])

        tasks = [asyncio.create_task(one(r)) for r in rows]
        with out_path.open("w", encoding="utf-8") as f:
            for fut in asyncio.as_completed(tasks):
                rec = await fut
                if (rec.get("error") or "").startswith(("HTTP 401", "HTTP 403")):
                    for t in tasks:
                        t.cancel()
                    await asyncio.gather(*tasks, return_exceptions=True)
                    raise SystemExit(f"OpenAI auth failed, aborting: {rec['error'][:200]}")
                records.append(rec)
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
                f.flush()
                verdict = (SKIP_LABEL[rec["skip"]] if rec["skip"] else
                           f"{'answer' if rec['metrics'].get('has_answer') else 'no'}"
                           f" {rec['metrics'].get('answer_chars', 0)}ch {rec['n_items']} items")
                print(f"  [{len(records):>3}/{len(rows)}] {'ok ' if rec['ok'] else 'ERR'} {rec['row_id']} "
                      f"{rec['facet'] or 'core':<10} luna {rec['timing']['luna_ms']:>7.0f} ms  {verdict}"
                      + (f"  {rec['error'][:80]}" if rec.get("error") else ""), flush=True)
    records.sort(key=lambda r: r["row_id"])
    return records


def run_synth(source_dir: Path, cfg: dict, rows: str | None = None, cli_args: list[str] | None = None,
              transport: httpx.AsyncBaseTransport | None = None, out_root: Path | None = None) -> Path:
    p = plan_synth(source_dir, cfg, rows)
    if p["n_calls"]:
        llm.check_ready(cfg["llm"])
    max_cost = float(cfg["run"].get("max_cost_usd") or 0)
    if max_cost and p["est_cost_usd"] > max_cost:
        raise SystemExit(f"Estimated cost ${p['est_cost_usd']} exceeds run.max_cost_usd=${max_cost}. "
                         f"Raise it with --set run.max_cost_usd=<n>.")
    src = p["source"]
    out_dir = _out_dir(cfg, src["source_id"], out_root)
    meta = {"synth_id": out_dir.name, "source_id": src["source_id"], "source_dir": str(Path(source_dir).resolve()),
            "source_kind": src["kind"],
            "source_run_id": src["source_run_id"], "arm": src["arm"], "config": cfg,
            "prompt_sha256": p["prompts"].SHA256, "facets": p["facets"],
            "started_at": datetime.now(timezone.utc).isoformat(timespec="seconds"), "finished_at": None,
            "n_rows": p["n_rows"], "n_calls": p["n_calls"], "est_cost_usd": p["est_cost_usd"],
            "cli_args": cli_args if cli_args is not None else sys.argv[1:],
            "env": {"wsx": __version__, "python": platform.python_version(), "platform": platform.platform()}}
    _write(out_dir / "synth.json", meta)
    print(f"Synth {out_dir.name}: arm {src['arm']}, {p['n_rows']} rows, {p['n_calls']} Luna calls, "
          f"est ${p['est_cost_usd']}")
    records = asyncio.run(_execute(p, cfg, out_dir / "results.jsonl", transport))
    meta["finished_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    _write(out_dir / "synth.json", meta)
    s = summarize_synth_dir(out_dir, records, meta)
    print_synth_summary(s)
    print(f"Saved to {out_dir}")
    return out_dir


def retry_failed(d: Path, sets: list[str] | None = None, transport: httpx.AsyncBaseTransport | None = None) -> list[str]:
    """Re-run the rows whose Luna call failed (rate limit, timeout, invalid JSON) into the SAME synth folder,
    with the folder's own config, so the arm stays complete and paired. Source errors are not retried."""
    meta = json.loads((d / "synth.json").read_text(encoding="utf-8"))
    records = load_records(d)
    failed = [r["row_id"] for r in records if not r["ok"] and r.get("skip") != "source_error"]
    if not failed:
        return []
    cfg = meta["config"]
    for s in sets or []:
        set_dotted(cfg, s)
    cands = ([Path(meta["source_dir"])] if meta.get("source_dir") else []) + [b / meta["source_id"] for b in (FILTERS_DIR, RUNS_DIR)]
    src = next((c for c in cands if c.exists()), None)
    if src is None:
        raise SystemExit(f"Source folder {meta['source_id']} not found")
    p = plan_synth(src, cfg, ",".join(failed))
    llm.check_ready(cfg["llm"])
    print(f"Retrying {len(failed)} failed rows of {d.name}: {' '.join(failed)}")
    new = {r["row_id"]: r for r in asyncio.run(_execute(p, cfg, d / "retry.jsonl", transport))}
    (d / "retry.jsonl").unlink(missing_ok=True)
    records = [new.get(r["row_id"], r) for r in records]
    with (d / "results.jsonl").open("w", encoding="utf-8") as f:
        f.writelines(json.dumps(r, ensure_ascii=False) + "\n" for r in records)
    meta.setdefault("retried", []).append({"at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                                           "rows": failed, "still_failed": [k for k, r in new.items() if not r["ok"]]})
    _write(d / "synth.json", meta)
    print_synth_summary(summarize_synth_dir(d, records, meta))
    return failed


def summarize_synth_dir(d: Path, records: list[dict] | None = None, meta: dict | None = None) -> dict:
    meta = meta or json.loads((d / "synth.json").read_text(encoding="utf-8"))
    if records is None:  # re-summarising a folder: recompute metrics so metric fixes apply without new calls
        records = load_records(d)
        for r in records:
            r["metrics"] = answer_metrics(r.get("output"), r["evidence"], r["anchors"], r["objective"])
        with (d / "results.jsonl").open("w", encoding="utf-8") as f:
            f.writelines(json.dumps(r, ensure_ascii=False) + "\n" for r in records)
    s = {"synth_id": meta["synth_id"], "arm": meta["arm"], "source_id": meta["source_id"],
         "model": meta["config"]["llm"]["model"], "prompt": meta["config"]["prompt"]["version"],
         "prompt_sha256": meta["prompt_sha256"][:12], **summarize_synth(records)}
    _write(d / "summary.json", s)
    (d / "answers.md").write_text(render_answers(records, s), encoding="utf-8")
    return s


def render_answers(records: list[dict], s: dict) -> str:
    lines = [f"# Luna answers: {s['arm']}", "", f"`{s['synth_id']}` · model `{s['model']}` · prompt {s['prompt']} "
             f"({s['prompt_sha256']})", ""]
    for r in records:
        m, o = r["metrics"], r.get("output") or {}
        head = SKIP_LABEL[r["skip"]] if r.get("skip") else (
            f"has_answer **{o.get('has_answer')}** · confidence {o.get('confident_score')} · {r['n_items']} items · "
            f"luna {r['timing']['luna_ms']:.0f} ms")
        lines += [f"## {r['row_id']} · {r['facet'] or 'core'}{'/' + r['scope'] if r['scope'] else ''}", "",
                  f"**Objective:** {r['objective']}  ", f"{head}", ""]
        if r.get("error"):
            lines += [f"ERROR: {r['error']}", ""]
        if o.get("summarized_answer"):
            lines += [str(o["summarized_answer"]).replace("<br>", "  \n"), ""]
        lines += [f"**Missing:** {o.get('missing', '-')}", ""]
        flags = [f"ungrounded {m['ungrounded_tokens']}" if m.get("ungrounded_tokens") else "",
                 f"search-talk {m['search_talk']}" if m.get("search_talk") else "",
                 f"invalid tags {m['invalid_tags']}" if m.get("invalid_tags") else "",
                 "URL in answer" if m.get("url_in_answer") else ""]
        if any(flags):
            lines += ["**Flags:** " + " · ".join(f for f in flags if f), ""]
        for e in r["evidence"]:
            lines.append(f"- {e['id']} [{(e['title'] or '-')[:90]}]({e['url']}) — {e['domain']}")
        lines.append("")
    return "\n".join(lines) + "\n"


def print_synth_summary(s: dict) -> None:
    a, c, g, t = s["answering"], s["contract"], s["grounding"], s["timing_ms"]
    print(f"  rows={s['n_rows']} answered={a['answer_rate']:.0%} jev-abstain={a['jev_abstain_rate']:.0%} "
          f"no-links={a['no_links_rate']:.0%} luna-no={a['luna_no_rate']:.0%} errors={a['error_rate']:.0%} complete={a['complete_rate']:.0%} conf={a['confident_mean']}")
    print(f"  contract: json {c['json_valid_rate']:.0%} | bad tags {c['invalid_tag_rows']:.0%} | url "
          f"{c['url_in_answer_rows']:.0%} | search-talk {c['search_talk_rows']:.0%} | ungrounded tokens "
          f"{g['ungrounded_token_rate']:.1%}")
    print(f"  timing p50: search {t['search']['p50']} + jev {t['jev']['p50']} + luna {t['luna']['p50']} = "
          f"{t['total']['p50']} ms (p95 {t['total']['p95']}) | cost ${s['cost_usd']['total']}")


def _write(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
