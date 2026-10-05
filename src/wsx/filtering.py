"""Jev layer: replay a saved search run through a filter (rerank, select, abstain), write
outputs/filters/<ts>__<filter>-<config>__on__<source_run_id>/{filter.json,results.jsonl,summary.json,inspect.md}.

No search calls are made: links come from the source run's results.jsonl. Metric definitions
are in docs/METHODOLOGY.md ("Jev filter").
"""

from __future__ import annotations

import asyncio
import json
import math
import platform
import re
import statistics
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import httpx

from . import FILTERS_DIR, __version__
from .config import deep_merge, load_file, set_dotted
from .dataset import select_rows
from .filters import Filter, get_filter
from .metrics import anchor_hit, categorize, load_domain_categories, load_records, pct, rate
from .runner import slug

GRANULARITIES = ("per_link", "per_list")

FILTER_DEFAULTS: dict = {
    "name": "unnamed",
    "filter": "jev",
    "model": "jev-latest",
    "granularity": "per_link",
    "max_snippet_chars": 1500,
    "send_target": False,
    "target": {
        "competitor_pattern": r"competing agents|competitors?\b|drugs approved against the target",
        "competitor_template": "drugs competing with {name}: other agents in the same mechanistic class "
                               "or for the same indication, as described in `objective`",
    },
    "question": None,   # v1: one noul (see configs/jev_default.yaml)
    "questions": None,  # v2: named noul/score questions (see configs/jev_v2.yaml)
    "select": {"keep_threshold": 0.5, "max_keep": 5, "gates": None},
    "run": {"concurrency": 2, "link_concurrency": 20, "timeout_s": 15, "retries": 2, "max_cost_usd": 1.0},
    "pricing": {"per_1m_input_tokens": 0.042},
}


def build_filter_config(path: str | Path | None, sets: list[str] | None = None) -> dict:
    cfg = deep_merge(FILTER_DEFAULTS, load_file(path) if path else {})
    for s in sets or []:
        set_dotted(cfg, s)
    if cfg["granularity"] not in GRANULARITIES:
        raise SystemExit(f"granularity must be one of {GRANULARITIES}, got {cfg['granularity']}")
    return cfg


def is_competitor(objective: str, cfg: dict) -> bool:
    pattern = (cfg.get("target") or {}).get("competitor_pattern")
    return bool(pattern and re.search(pattern, objective or "", re.I))


def target_of(objective: str, anchors: list[str] | None, cfg: dict) -> str | None:
    """What the links must be about: the asset (anchor names), or its competitors for competitor objectives."""
    if not anchors:
        return None
    name = " / ".join(dict.fromkeys(anchors))
    if is_competitor(objective, cfg):
        return cfg["target"]["competitor_template"].format(name=name)
    return name


# ---------- one link list ----------

def candidates(results: list[dict]) -> list[dict]:
    """Dedupe by URL (batch records merge several queries' results), keep fetch order as orig_rank."""
    seen, out = set(), []
    for r in results:
        key = r.get("url") or r.get("title")
        if key in seen:
            continue
        seen.add(key)
        out.append({**r, "orig_rank": len(out) + 1})
    return out


def composite(answers: dict | None) -> float | None:
    """Rank score: product of the normalized answers (one question -> that answer)."""
    if not answers:
        return None
    return round(math.prod(answers.values()), 4)


def select(results: list[dict], select_cfg: dict) -> list[dict]:
    """Order by jev_score (ties: fetch order); keep links passing every gate (or keep_threshold
    when no gates are configured), at most max_keep. Each link gets a `reason`."""
    gates = select_cfg.get("gates") or {}
    threshold, max_keep = float(select_cfg.get("keep_threshold", 0.5)), int(select_cfg["max_keep"])
    ranked = sorted(results, key=lambda r: (-(r["jev_score"] if r.get("jev_score") is not None else -1),
                                            r["orig_rank"]))
    n_kept = 0
    for i, r in enumerate(ranked, start=1):
        r["jev_rank"] = i
        answers, score = r.get("answers"), r.get("jev_score")
        if score is None:
            reason = "error"
        elif gates and answers:
            failed = [g for g, lo in gates.items() if answers.get(g, 0) < float(lo)]
            reason = f"low_{failed[0]}" if failed else "pass"
        else:
            reason = "pass" if score >= threshold else "below_threshold"
        if reason == "pass":
            reason = "kept" if n_kept < max_keep else "max_keep"
        r["kept"] = reason == "kept"
        r["reason"] = reason
        n_kept += r["kept"]
    return ranked


def _selection_fields(results: list[dict]) -> dict:
    scores = [r["jev_score"] for r in results if r.get("jev_score") is not None]
    n_kept = sum(1 for r in results if r["kept"])
    return {"n_candidates": len(results), "n_kept": n_kept, "abstain": n_kept == 0,
            "top_score": max(scores) if scores else None}


async def filter_list(filt: Filter, client: httpx.AsyncClient, objective: str, results: list[dict],
                      select_cfg: dict, target: str | None = None) -> dict:
    """Score + select one list of links. Shared by `wsx filter` and `wsx query --jev`."""
    cands = candidates(results)
    resp = await filt.score(client, objective, cands, target)
    for c, a in zip(cands, resp.answers):
        c["answers"] = a
        c["jev_score"] = composite(a)
    ranked = select(cands, select_cfg)
    return {
        "target": target,
        "ok": resp.ok,
        "error": resp.error,
        "jev_latency_ms": round(resp.latency_ms, 1),
        "calls": resp.calls,
        "attempts": resp.attempts,
        "usage": resp.usage,
        "cost_usd": round(filt.cost_usd(resp.usage["input_tokens"], resp.usage["output_tokens"]), 6),
        **_selection_fields(ranked),
        "results": ranked,
    }


# ---------- a whole source run ----------

def plan_filter(source_run_dir: Path, cfg: dict, rows: str | None = None) -> dict:
    filt = get_filter(cfg)
    records = [r for r in load_records(source_run_dir) if r["ok"] and r.get("repeat", 0) == 0]
    if rows:
        wanted = {q["id"] for q in select_rows([{"id": i} for i in sorted({r["row_id"] for r in records})], rows)}
        records = [r for r in records if r["row_id"] in wanted]
    n_links = sum(len(candidates(r["results"])) for r in records)
    tokens = sum(filt.estimate_input_tokens(r["objective"], candidates(r["results"]),
                                            target_of(r["objective"], r.get("anchors"), cfg)) for r in records)
    calls = n_links if cfg["granularity"] == "per_link" else sum(1 for r in records if r["results"])
    return {"filter": filt, "source_run_id": source_run_dir.name, "records": records,
            "n_requests": len(records), "n_links": n_links, "n_calls": calls,
            "est_input_tokens": tokens, "est_cost_usd": round(filt.cost_usd(tokens), 4)}


def _out_dir(cfg: dict, source_run_id: str, out_root: Path | None) -> Path:
    root = out_root or FILTERS_DIR
    base = f"{datetime.now():%Y%m%d-%H%M%S}__{slug(cfg['filter'])}-{slug(cfg['name'])}__on__{source_run_id}"
    d, n = root / base, 2
    while d.exists():
        d, n = root / f"{base}-{n}", n + 1
    d.mkdir(parents=True)
    return d


async def _execute(filt: Filter, src_records: list[dict], cfg: dict, out_path: Path,
                   transport: httpx.AsyncBaseTransport | None = None) -> list[dict]:
    run = cfg["run"]
    sem = asyncio.Semaphore(int(run["concurrency"]))
    records: list[dict] = []
    limits = httpx.Limits(max_connections=int(run["link_concurrency"]) + 4)
    async with httpx.AsyncClient(limits=limits, transport=transport) as client:

        async def one(src: dict) -> dict:
            target = target_of(src["objective"], src.get("anchors"), cfg)
            async with sem:
                out = await filter_list(filt, client, src["objective"], src["results"], cfg["select"], target)
            base = {k: src.get(k) for k in ("case_id", "row_id", "mode", "objective", "query", "anchors")}
            return {**base, "search_latency_ms": src["latency_ms"], **out,
                    "total_ms": round(src["latency_ms"] + out["jev_latency_ms"], 1),
                    "ts": datetime.now(timezone.utc).isoformat(timespec="seconds")}

        tasks = [asyncio.create_task(one(s)) for s in src_records]
        with out_path.open("w", encoding="utf-8") as f:
            for fut in asyncio.as_completed(tasks):
                rec = await fut
                if (rec.get("error") or "").startswith(("HTTP 401", "HTTP 403")):  # bad key: stop, don't retry 2K calls
                    for t in tasks:
                        t.cancel()
                    await asyncio.gather(*tasks, return_exceptions=True)
                    raise SystemExit(f"Jev auth failed, aborting: {rec['error'][:200]}")
                records.append(rec)
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
                f.flush()
                mark = "ok " if rec["ok"] else "ERR"
                verdict = "ABSTAIN" if rec["abstain"] else f"kept {rec['n_kept']}/{rec['n_candidates']}"
                print(f"  [{len(records):>4}/{len(src_records)}] {mark} {rec['case_id']:<14} "
                      f"jev {rec['jev_latency_ms']:>6.0f} ms  {verdict}"
                      + (f"  {rec['error']}" if rec["error"] else ""), flush=True)
    records.sort(key=lambda x: x["case_id"])
    return records


def apply_filter(source_run_dir: Path, cfg: dict, rows: str | None = None, cli_args: list[str] | None = None,
                 transport: httpx.AsyncBaseTransport | None = None, out_root: Path | None = None) -> Path:
    p = plan_filter(source_run_dir, cfg, rows)
    filt: Filter = p["filter"]
    filt.check_ready()
    max_cost = float(cfg["run"].get("max_cost_usd") or 0)
    if max_cost and p["est_cost_usd"] > max_cost:
        raise SystemExit(f"Estimated cost ${p['est_cost_usd']} exceeds run.max_cost_usd=${max_cost}. "
                         f"Raise it with --set run.max_cost_usd=<n>.")
    out_dir = _out_dir(cfg, p["source_run_id"], out_root)
    started = datetime.now(timezone.utc)
    meta = _meta(out_dir, cfg, source_run_dir, cli_args, started)
    meta.update({"n_requests": p["n_requests"], "n_links": p["n_links"],
                 "est_input_tokens": p["est_input_tokens"], "est_cost_usd": p["est_cost_usd"]})
    _write(out_dir / "filter.json", meta)

    print(f"Filter {out_dir.name}: {p['n_requests']} link lists, {p['n_links']} links, "
          f"{p['n_calls']} calls, est ${p['est_cost_usd']}")
    records = asyncio.run(_execute(filt, p["records"], cfg, out_dir / "results.jsonl", transport))

    finished = datetime.now(timezone.utc)
    meta["finished_at"] = finished.isoformat(timespec="seconds")
    meta["duration_s"] = round((finished - started).total_seconds(), 1)
    _write(out_dir / "filter.json", meta)
    s = summarize_filter_dir(out_dir, records, meta)
    print_filter_summary(s)
    print(f"Saved to {out_dir}")
    return out_dir


def rescore(filter_dir: Path, sets: list[str], out_root: Path | None = None) -> Path:
    """Re-apply `select` to stored answers (no API calls) and save as a new filter folder."""
    old = json.loads((filter_dir / "filter.json").read_text(encoding="utf-8"))
    cfg = deep_merge(FILTER_DEFAULTS, old["config"])
    for s in sets:
        set_dotted(cfg, s)
    sel = cfg["select"]
    gates = sel.get("gates") or {}
    tag = "-".join(f"{g}{v}" for g, v in gates.items()) if gates else f"t{sel['keep_threshold']}"
    cfg["base_name"] = old["config"].get("base_name", old["config"]["name"])
    cfg["name"] = f"{cfg['base_name']}-{tag}-k{sel['max_keep']}"
    records = load_records(filter_dir)
    for r in records:
        for x in r["results"]:
            if "answers" not in x:  # v1 folders stored only the single score
                x["answers"] = {"evidence": x["jev_score"]} if x.get("jev_score") is not None else None
        r["results"] = select(sorted(r["results"], key=lambda x: x["orig_rank"]), sel)
        r.update(_selection_fields(r["results"]))
    out_dir = _out_dir(cfg, old["source_run_id"], out_root)
    meta = {**old, "filter_id": out_dir.name, "config": cfg, "rescored_from": filter_dir.name,
            "cli_args": sys.argv[1:], "started_at": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    _write(out_dir / "filter.json", meta)
    with (out_dir / "results.jsonl").open("w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    s = summarize_filter_dir(out_dir, records, meta)
    print_filter_summary(s)
    print(f"Saved to {out_dir}")
    return out_dir


def _meta(out_dir: Path, cfg: dict, source_run_dir: Path, cli_args, started: datetime) -> dict:
    src_meta_path = source_run_dir / "run.json"
    src_meta = json.loads(src_meta_path.read_text(encoding="utf-8")) if src_meta_path.exists() else {}
    return {
        "filter_id": out_dir.name,
        "source_run_id": source_run_dir.name,
        "source_config": (src_meta.get("config") or {}).get("name"),
        "source_mode": (src_meta.get("config") or {}).get("mode"),
        "source_params": (src_meta.get("config") or {}).get("params"),
        "dataset_sha256": (src_meta.get("dataset") or {}).get("sha256"),
        "started_at": started.isoformat(timespec="seconds"),
        "finished_at": None,
        "config": cfg,
        "cli_args": cli_args if cli_args is not None else sys.argv[1:],
        "env": {"wsx": __version__, "python": platform.python_version(), "platform": platform.platform()},
    }


def _write(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


# ---------- metrics ----------

def _lat(values: list[float]) -> dict:
    return {"p50": pct(values, 0.5), "p95": pct(values, 0.95),
            "mean": round(statistics.fmean(values), 1) if values else None}


def summarize_filter(records: list[dict], categories: dict, cfg: dict | None = None) -> dict:
    """Without Jev = every fetched link in fetch order; with Jev = the kept links in Jev order.
    Anchor-based quality skips competitor objectives (their good links name other drugs)."""
    cfg = cfg or FILTER_DEFAULTS
    n = len(records)
    ok = [r for r in records if r["ok"]]
    scored = [r for r in ok if r["n_candidates"]]
    judged = [r for r in scored if not is_competitor(r["objective"], cfg)]  # anchor proxy applies

    search = [r["search_latency_ms"] for r in scored]
    jev = [r["jev_latency_ms"] for r in scored]
    total = [r["total_ms"] for r in scored]

    links_all = links_kept = hits_all = hits_kept = 0
    hit1_before = hit1_rerank = hit1_after = 0
    abstain_no_hits = abstain_with_hits = kept_no_hits = 0
    cov_before: dict[str, bool] = defaultdict(bool)
    cov_after: dict[str, bool] = defaultdict(bool)
    for r in judged:
        fetched = sorted(r["results"], key=lambda x: x["orig_rank"])
        ranked = sorted(r["results"], key=lambda x: x["jev_rank"])
        kept = [x for x in ranked if x["kept"]]
        h_all = [anchor_hit(x, r["anchors"]) for x in fetched]
        h_kept = [anchor_hit(x, r["anchors"]) for x in kept]
        links_all += len(fetched)
        links_kept += len(kept)
        hits_all += sum(h_all)
        hits_kept += sum(h_kept)
        hit1_before += h_all[0]
        hit1_rerank += anchor_hit(ranked[0], r["anchors"])
        hit1_after += bool(h_kept and h_kept[0])
        cov_before[r["row_id"]] |= any(h_all)
        cov_after[r["row_id"]] |= any(h_kept)
        if r["abstain"]:
            abstain_no_hits += not any(h_all)
            abstain_with_hits += any(h_all)
        elif not any(h_all):
            kept_no_hits += 1

    cats_all, cats_kept, reasons = Counter(), Counter(), Counter()
    for r in scored:
        for x in r["results"]:
            cats_all[categorize(x["domain"], categories)] += 1
            if x["kept"]:
                cats_kept[categorize(x["domain"], categories)] += 1
            reasons[x.get("reason", "kept" if x["kept"] else "dropped")] += 1
    n_all, n_kept_all = sum(cats_all.values()), sum(cats_kept.values())

    answer_means: dict[str, list[float]] = defaultdict(list)
    for r in ok:
        for x in r["results"]:
            for q, v in (x.get("answers") or {}).items():
                answer_means[q].append(v)

    judged_rows = {r["row_id"] for r in judged}
    scores = [x["jev_score"] for r in ok for x in r["results"] if x.get("jev_score") is not None]
    cost = sum(r["cost_usd"] for r in records)
    k, kj = len(scored), len(judged)
    return {
        "n_requests": n,
        "n_scored": k,
        "error_rate": rate(n - len(ok), n),
        "errors": dict(Counter(r["error"] for r in records if not r["ok"])),
        "timing_ms": {
            "search": _lat(search), "jev": _lat(jev), "total": _lat(total),
            "jev_share_of_total_p50": rate(pct(jev, 0.5) or 0, pct(total, 0.5) or 0),
        },
        "calls_per_request_mean": round(statistics.fmean([r["calls"] for r in scored]), 2) if scored else 0,
        "input_tokens_per_request_mean": round(statistics.fmean([r["usage"]["input_tokens"] for r in scored]), 0) if scored else 0,
        "selection": {
            "candidates_mean": round(n_all / k, 2) if k else 0,
            "kept_mean": round(n_kept_all / k, 2) if k else 0,
            "abstain_rate": rate(sum(1 for r in scored if r["abstain"]), k),
            "score_p10": pct(scores, 0.1), "score_p50": pct(scores, 0.5), "score_p90": pct(scores, 0.9),
            "answer_means": {q: round(statistics.fmean(v), 3) for q, v in answer_means.items()},
            "reasons": dict(reasons.most_common()),
        },
        "quality": {
            "lists_judged": kj,
            "rows_judged": len(judged_rows),
            "competitor_lists_excluded": k - kj,
            "anchor_precision": {"without_jev": rate(hits_all, links_all), "with_jev": rate(hits_kept, links_kept)},
            "hit_at_1": {"without_jev": rate(hit1_before, kj), "with_jev": rate(hit1_after, kj),
                         "rerank_only": rate(hit1_rerank, kj)},
            "objective_coverage": {"without_jev": rate(sum(cov_before.values()), len(judged_rows)),
                                   "with_jev": rate(sum(cov_after.values()), len(judged_rows))},
            "anchor_recall_retained": rate(hits_kept, hits_all),
            "abstain_no_anchor_hits": rate(abstain_no_hits, kj),
            "abstain_with_anchor_hits": rate(abstain_with_hits, kj),
            "kept_without_anchor_hits": rate(kept_no_hits, kj),
            "rows_lost": sorted(r for r in judged_rows if cov_before.get(r) and not cov_after.get(r)),
        },
        "source_mix": {
            "without_jev": {c: rate(v, n_all) for c, v in cats_all.most_common()},
            "with_jev": {c: rate(v, n_kept_all) for c, v in cats_kept.most_common()},
        },
        "cost_usd": round(cost, 4),
        "cost_per_1k_requests": round(cost / k * 1000, 4) if k else None,
    }


def summarize_filter_dir(filter_dir: Path, records: list[dict] | None = None, meta: dict | None = None) -> dict:
    meta = meta or json.loads((filter_dir / "filter.json").read_text(encoding="utf-8"))
    records = records if records is not None else load_records(filter_dir)
    cfg = deep_merge(FILTER_DEFAULTS, meta["config"])
    summary = {
        "filter_id": meta["filter_id"],
        "source_run_id": meta["source_run_id"],
        "source_mode": meta.get("source_mode"),
        "source_params": meta.get("source_params"),
        "filter": cfg["filter"],
        "config_name": cfg["name"],
        "model": cfg.get("model"),
        "granularity": cfg["granularity"],
        "select": cfg["select"],
        "rescored_from": meta.get("rescored_from"),
        "started_at": meta.get("started_at"),
        "duration_s": meta.get("duration_s"),
        **summarize_filter(records, load_domain_categories(), cfg),
    }
    _write(filter_dir / "summary.json", summary)
    (filter_dir / "inspect.md").write_text(render_inspect(records, summary, cfg), encoding="utf-8")
    return summary


def render_inspect(records: list[dict], summary: dict, cfg: dict) -> str:
    """Every link, per objective: kept or why dropped, with Jev's answers. For human review."""
    sel = summary["selection"]
    lines = [f"# Jev inspect: {summary['filter_id']}", "",
             f"Config `{summary['config_name']}` ({summary['granularity']}), select={json.dumps(summary['select'])}. "
             f"Reasons: {json.dumps(sel['reasons'])}. Answer means: {json.dumps(sel['answer_means'])}.", "",
             "Legend: ✅ kept · ❌ dropped (reason) · `A` = mentions the anchor · scores are Jev's answers in [0, 1].",
             ""]
    by_row: dict[str, list[dict]] = defaultdict(list)
    for r in records:
        by_row[r["row_id"]].append(r)
    for row_id in sorted(by_row):
        recs = by_row[row_id]
        first = recs[0]
        comp = " (competitor objective)" if is_competitor(first["objective"], cfg) else ""
        lines += [f"## {row_id}{comp}", "", f"**Objective:** {first['objective']}  ",
                  f"**Target sent:** {first.get('target') or '-'} · anchors {first.get('anchors')}", ""]
        for r in recs:
            q = r["query"] if isinstance(r["query"], str) else " || ".join(r["query"])
            verdict = "ABSTAIN" if r["abstain"] else f"kept {r['n_kept']}/{r['n_candidates']}"
            lines.append(f"**{r['case_id']}** `{q}` → {verdict}, jev {r['jev_latency_ms']:.0f} ms"
                         + (f" · ERROR {r['error']}" if r.get("error") else ""))
            lines.append("")
            for x in sorted(r["results"], key=lambda x: x["jev_rank"]):
                mark = "✅" if x["kept"] else f"❌ {x.get('reason', 'dropped')}"
                ans = " ".join(f"{q}={v:.2f}" for q, v in (x.get("answers") or {}).items())
                a = " `A`" if anchor_hit(x, r.get("anchors") or []) else ""
                title = (x.get("title") or "(no title)").replace("|", "/")[:100]
                lines.append(f"- {mark} **{x['jev_score'] if x.get('jev_score') is not None else 'n/a'}** "
                             f"[{ans}] {title} — {x['domain']} (#{x['orig_rank']}){a}")
            lines.append("")
    return "\n".join(lines) + "\n"


def print_filter_summary(s: dict) -> None:
    t, sel, q = s["timing_ms"], s["selection"], s["quality"]
    print(f"  lists={s['n_scored']} errors={s['error_rate']:.1%} calls/list={s['calls_per_request_mean']} "
          f"cost=${s['cost_usd']}")
    print(f"  timing p50: search {t['search']['p50']} + jev {t['jev']['p50']} = {t['total']['p50']} ms "
          f"| p95 jev {t['jev']['p95']} total {t['total']['p95']}")
    print(f"  kept/list={sel['kept_mean']} of {sel['candidates_mean']} | abstain={sel['abstain_rate']:.1%} "
          f"| reasons {sel['reasons']}")
    ap, h1, cov = q["anchor_precision"], q["hit_at_1"], q["objective_coverage"]
    print(f"  [anchor proxy, {q['rows_judged']} non-competitor rows] precision {ap['without_jev']:.1%} -> "
          f"{ap['with_jev']:.1%} | hit@1 {h1['without_jev']:.1%} -> {h1['with_jev']:.1%} | coverage "
          f"{cov['without_jev']:.1%} -> {cov['with_jev']:.1%} | recall kept {q['anchor_recall_retained']:.1%} "
          f"| rows lost {q['rows_lost']}")
