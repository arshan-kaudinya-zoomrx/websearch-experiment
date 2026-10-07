"""Subjective scoring: a blind LLM judge compares the arms' Luna answers row by row, plus a human
spot-check sheet to calibrate it.

outputs/judge/<ts>__judge-<config>__<n>arms/
  judge.json         config, the synth folders (arms), shuffle seed
  results.jsonl      per row: answer order shown, judge scores per arm, ranking, position-check rerun
  summary.json       per arm: mean scores, mean rank, win rate, pairwise wins + objective metrics
  compare.md         one table, one row per arm
  human_review.csv   stratified sample, same blind labels, empty score columns (fill in, then `wsx judge-score`)
  human_evidence.md  the evidence pool for each sampled row
  human_key.json     label -> arm for the sample (do not open before scoring)

The judge sees the objective, the UNION of every arm's evidence (deduped by URL, tags [S1]..), and
each answer with its [Ek] tags rewritten to the pool's [Sx] tags, in a shuffled order labelled A-D.
"""

from __future__ import annotations

import asyncio
import csv
import json
import random
import statistics
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import httpx

from . import JUDGE_DIR, llm
from .config import deep_merge, load_file, set_dotted
from .luna import TAG_RE, summarize_synth_dir
from .metrics import load_records, rate

CRITERIA = ("correct", "complete", "subject", "useful")
LABELS = "ABCDEFGH"

JUDGE_DEFAULTS: dict = {
    "name": "unnamed",
    "seed": 7,
    "max_chars_per_item": None,  # None = the judge sees exactly the text Luna saw
    "position_check_rows": 10,
    "human_sample": 16,
    "llm": {"model": None, "temperature": None, "reasoning_effort": None, "max_completion_tokens": 4000,
            "seed": None, "timeout_s": 180, "retries": 2,
            "pricing": {"per_1m_input_tokens": 0, "per_1m_cached_input_tokens": None, "per_1m_output_tokens": 0}},
    "run": {"concurrency": 4, "max_cost_usd": 2.0},
}

JUDGE_SYSTEM = """You grade answers written for one cell of a pharma competitive-intelligence research table.

You are given an OBJECTIVE (what the cell must answer), an EVIDENCE POOL of web items [S1], [S2] ...,
and several candidate ANSWERS labelled A, B, C ... Each answer was written from a SUBSET of the pool
and cites items with [S] tags. An answer may be EMPTY: the cell would then read "No data available".

Judge every answer ONLY against the evidence pool. Do not use outside knowledge about these drugs.
The answers are in random order and come from different systems; do not prefer an answer for its
position, its length or its style.

Score each answer from 1 to 5 on:
  correct   Every claim is supported by the item it cites and is about the right entity. 5 = no
            unsupported or wrong claim; 1 = a central claim is wrong, invented, or about another drug.
            An EMPTY answer scores 5 here (it asserts nothing).
  complete  How much of what the POOL can answer about the objective this answer delivers.
            5 = everything the pool supports; 1 = misses most of it. An EMPTY answer scores 1 if the
            pool does answer the objective, and 5 if the pool genuinely holds nothing relevant.
  subject   Stays on the objective's subject (or, for competitor objectives, on the competing
            agents) and does not write a lookalike or neighbouring asset's facts into it.
            An EMPTY answer scores 5.
  useful    Overall value to an analyst reading this cell: correct, specific, complete, readable.

Then RANK all answers from best to worst (ties are not allowed). List the concrete errors you found
for each answer (wrong claim, unsupported number, wrong entity, important omission), at most 3 each.

Return ONE JSON object and nothing else:
{"answers": {"A": {"correct": n, "complete": n, "subject": n, "useful": n, "errors": ["..."]}, ...},
 "ranking": ["B", "A", ...],
 "pool_answers_objective": "yes" | "partly" | "no"}"""


def build_judge_config(path: str | Path | None, sets: list[str] | None = None) -> dict:
    cfg = deep_merge(JUDGE_DEFAULTS, load_file(path) if path else {})
    for s in sets or []:
        set_dotted(cfg, s)
    return cfg


# ---------- building one row ----------

def load_arms(synth_dirs: list[Path]) -> list[dict]:
    arms = []
    for d in synth_dirs:
        meta = json.loads((d / "synth.json").read_text(encoding="utf-8"))
        arms.append({"synth_id": d.name, "arm": meta["arm"], "dir": d, "llm": meta["config"].get("llm") or {},
                     "rows": {r["row_id"]: r for r in load_records(d)}})
    names = [a["arm"] for a in arms]
    if len(set(names)) != len(names):  # same arm twice (e.g. two models): disambiguate by folder
        for a in arms:
            a["arm"] = f"{a['arm']} [{a['synth_id'][:15]}]"
    return arms


def pool_and_answers(recs: list[dict], max_chars: int | None = None) -> tuple[list[dict], list[dict]]:
    """Union of the arms' evidence (dedupe by URL) as [S1].., and each arm's answer re-tagged to it.
    When arms hold different text for one URL (e.g. a Perplexity snippet vs a Parallel excerpt), the
    pool keeps every distinct text, so each answer can be checked against what its own Luna saw.
    `max_chars` is an optional extra cut; by default the judge sees exactly the text Luna saw."""
    pool, by_url = [], {}
    for r in recs:
        for e in r["evidence"]:
            key = e.get("url") or e.get("title")
            text = e.get("text") or ""
            if key not in by_url:
                by_url[key] = len(pool) + 1
                pool.append({**e, "sid": f"S{len(pool) + 1}", "texts": []})
            texts = pool[by_url[key] - 1]["texts"]
            if text and not any(text in t for t in texts):
                texts[:] = [t for t in texts if t not in text] + [text]
    for p in pool:
        joined = "\n[another copy of this page:] ".join(p.pop("texts"))
        p["text"] = joined[:max_chars] if max_chars else joined
    answers = []
    for r in recs:
        o = r.get("output") or {}
        local = {int(e["id"][1:]): by_url[e.get("url") or e.get("title")] for e in r["evidence"]}
        text = TAG_RE.sub(lambda m: f"[S{local[int(m.group(1))]}]" if int(m.group(1)) in local else m.group(0),
                          str(o.get("summarized_answer") or ""))
        answers.append({"text": text, "missing": o.get("missing"), "has_answer": o.get("has_answer")})
    return pool, answers


def judge_user(objective: str, pool: list[dict], shown: list[tuple[str, dict]]) -> str:
    ev = []
    for e in pool:
        head = f"[{e['sid']}] {e.get('title') or '-'} ({e.get('domain') or '-'})" + (f" date: {e['date']}" if e.get("date") else "")
        ev.append(head + "\n" + (e.get("text") or ""))
    ans = []
    for label, a in shown:
        body = a["text"].strip() or "(EMPTY: the cell reads \"No data available\")"
        ans.append(f"ANSWER {label}:\n{body}\nStated as missing: {a.get('missing') or '-'}")
    return f"OBJECTIVE:\n{objective}\n\nEVIDENCE POOL:\n" + "\n\n".join(ev) + "\n\nANSWERS:\n" + "\n\n".join(ans)


def shuffled(n: int, seed: int, row_id: str) -> list[int]:
    order = list(range(n))
    random.Random(f"{seed}:{row_id}").shuffle(order)
    return order


def unshuffle(parsed: dict | None, order: list[int], arm_names: list[str]) -> dict | None:
    """Map the judge's labels back to arms. order[i] = arm index shown as label i."""
    if not parsed:
        return None
    by_label = {LABELS[i]: arm_names[a] for i, a in enumerate(order)}
    scores = {}
    for label, s in (parsed.get("answers") or {}).items():
        if label in by_label and isinstance(s, dict):
            scores[by_label[label]] = {c: s.get(c) for c in CRITERIA} | {"errors": s.get("errors") or []}
    ranking = [by_label[x] for x in parsed.get("ranking") or [] if x in by_label]
    valid = len(scores) == len(order) and sorted(ranking) == sorted(arm_names) and all(
        isinstance(v[c], (int, float)) for v in scores.values() for c in CRITERIA)
    return {"scores": scores, "ranking": ranking, "valid": valid,
            "pool_answers_objective": parsed.get("pool_answers_objective")}


# ---------- run ----------

def plan_judge(synth_dirs: list[Path], cfg: dict, rows: str | None = None) -> dict:
    from .dataset import select_rows
    arms = load_arms(synth_dirs)
    if not cfg["llm"].get("model"):  # default: judge with Luna's own model (the one the synth folders used)
        luna = arms[0]["llm"]
        for key in ("model", "temperature", "reasoning_effort", "pricing"):
            if luna.get(key) is not None:
                cfg["llm"][key] = luna[key]
        cfg["llm_from_synth"] = True
    common = sorted(set.intersection(*(set(a["rows"]) for a in arms)))
    if rows:
        common = [q["id"] for q in select_rows([{"id": i} for i in common], rows)]
    arm_names = [a["arm"] for a in arms]
    # A row where any arm errored (search/Jev failed, or the Luna call failed) is not judged:
    # an error is not an empty answer, and judging it as one would score a 429 as an abstain.
    skipped = {row_id: [a["arm"] for a in arms if not a["rows"][row_id].get("ok")] for row_id in common}
    skipped = {k: v for k, v in skipped.items() if v}
    common = [r for r in common if r not in skipped]
    items, est = [], 0
    for i, row_id in enumerate(common):
        recs = [a["rows"][row_id] for a in arms]
        pool, answers = pool_and_answers(recs, cfg.get("max_chars_per_item"))
        order = shuffled(len(arms), int(cfg["seed"]), row_id)
        user = judge_user(recs[0]["objective"], pool, [(LABELS[k], answers[a]) for k, a in enumerate(order)])
        check = i < int(cfg["position_check_rows"])
        est += llm.estimate_tokens(JUDGE_SYSTEM + user) * (2 if check else 1)
        items.append({"row_id": row_id, "objective": recs[0]["objective"], "facet": recs[0].get("facet"),
                      "pool": pool, "answers": answers, "order": order, "user": user, "check": check})
    n_calls = len(items) + sum(x["check"] for x in items)
    usage = {"input_tokens": est, "output_tokens": 600 * n_calls}
    return {"arms": arms, "arm_names": arm_names, "items": items, "skipped": skipped, "n_calls": n_calls,
            "est_input_tokens": est, "est_cost_usd": round(llm.cost_usd(cfg["llm"], usage), 4)}


async def _judge_row(client, cfg, item, arm_names) -> dict:
    resp = await llm.complete(client, cfg["llm"], JUDGE_SYSTEM, item["user"])
    rec = {"row_id": item["row_id"], "objective": item["objective"], "facet": item["facet"],
           "order": [arm_names[a] for a in item["order"]], "n_pool": len(item["pool"]),
           "ok": resp.ok, "error": resp.error, "latency_ms": round(resp.latency_ms, 1), "usage": resp.usage,
           "cost_usd": round(llm.cost_usd(cfg["llm"], resp.usage), 6), "judge": unshuffle(resp.parsed, item["order"], arm_names),
           "raw": resp.parsed}
    if item["check"]:  # same row, reversed presentation order: does the ranking follow the position?
        rev = list(reversed(item["order"]))
        user = judge_user(item["objective"], item["pool"], [(LABELS[k], item["answers"][a]) for k, a in enumerate(rev)])
        r2 = await llm.complete(client, cfg["llm"], JUDGE_SYSTEM, user)
        rec["position_check"] = unshuffle(r2.parsed, rev, arm_names)
        rec["cost_usd"] = round(rec["cost_usd"] + llm.cost_usd(cfg["llm"], r2.usage), 6)
    return rec


def run_judge(synth_dirs: list[Path], cfg: dict, rows: str | None = None, out_root: Path | None = None,
              transport: httpx.AsyncBaseTransport | None = None) -> Path:
    p = plan_judge(synth_dirs, cfg, rows)
    llm.check_ready(cfg["llm"])
    max_cost = float(cfg["run"].get("max_cost_usd") or 0)
    if max_cost and p["est_cost_usd"] > max_cost:
        raise SystemExit(f"Estimated cost ${p['est_cost_usd']} exceeds run.max_cost_usd=${max_cost}.")
    root = out_root or JUDGE_DIR
    base = f"{datetime.now():%Y%m%d-%H%M%S}__judge-{cfg['name']}__{len(p['arms'])}arms"
    out, n = root / base, 2
    while out.exists():
        out, n = root / f"{base}-{n}", n + 1
    out.mkdir(parents=True)
    meta = {"judge_id": out.name, "config": cfg, "arms": {a["arm"]: a["synth_id"] for a in p["arms"]},
            "synth_dirs": {a["arm"]: str(a["dir"]) for a in p["arms"]},
            "rows": [x["row_id"] for x in p["items"]], "skipped_rows": p["skipped"], "est_cost_usd": p["est_cost_usd"],
            "started_at": datetime.now(timezone.utc).isoformat(timespec="seconds"), "cli_args": sys.argv[1:]}
    (out / "judge.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Judge {out.name}: {len(p['items'])} rows x {len(p['arms'])} arms, {p['n_calls']} calls, est ${p['est_cost_usd']}"
          + (f" | not judged (an arm errored): {p['skipped']}" if p["skipped"] else ""))

    async def go():
        sem = asyncio.Semaphore(int(cfg["run"]["concurrency"]))
        recs = []
        async with httpx.AsyncClient(transport=transport) as client:
            async def one(item):
                async with sem:
                    return await _judge_row(client, cfg, item, p["arm_names"])
            tasks = [asyncio.create_task(one(x)) for x in p["items"]]
            with (out / "results.jsonl").open("w", encoding="utf-8") as f:
                for fut in asyncio.as_completed(tasks):
                    rec = await fut
                    if (rec.get("error") or "").startswith(("HTTP 401", "HTTP 403")):
                        for t in tasks:
                            t.cancel()
                        await asyncio.gather(*tasks, return_exceptions=True)
                        raise SystemExit(f"OpenAI auth failed, aborting: {rec['error'][:200]}")
                    recs.append(rec)
                    f.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    f.flush()
                    rank = " > ".join(rec["judge"]["ranking"]) if rec.get("judge") else rec.get("error")
                    print(f"  [{len(recs):>3}/{len(tasks)}] {rec['row_id']} {rank}", flush=True)
        return sorted(recs, key=lambda r: r["row_id"])

    records = asyncio.run(go())
    meta["finished_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    (out / "judge.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    summarize_judge_dir(out, records)
    export_human(out, p, cfg)
    print((out / "compare.md").read_text(encoding="utf-8"))
    print(f"Saved to {out}")
    return out


# ---------- metrics ----------

def summarize_judge(records: list[dict], arm_names: list[str]) -> dict:
    valid = [r for r in records if r.get("judge") and r["judge"]["valid"]]
    per_arm = {}
    for a in arm_names:
        sc = {c: [r["judge"]["scores"][a][c] for r in valid] for c in CRITERIA}
        ranks = [r["judge"]["ranking"].index(a) + 1 for r in valid]
        per_arm[a] = {**{c: round(statistics.fmean(v), 2) if v else None for c, v in sc.items()},
                      "mean_rank": round(statistics.fmean(ranks), 2) if ranks else None,
                      "win_rate": rate(sum(1 for x in ranks if x == 1), len(ranks))}
    pairwise = {a: {b: rate(sum(1 for r in valid if r["judge"]["ranking"].index(a) < r["judge"]["ranking"].index(b)),
                            len(valid)) for b in arm_names if b != a} for a in arm_names}
    checks = [r for r in valid if (r.get("position_check") or {}).get("valid")]
    same_top = sum(1 for r in checks if r["judge"]["ranking"][0] == r["position_check"]["ranking"][0])
    rho = [spearman(r["judge"]["ranking"], r["position_check"]["ranking"]) for r in checks]
    by_facet: dict[str, dict] = defaultdict(dict)
    for f in sorted({r.get("facet") or "core" for r in valid}):
        rs = [r for r in valid if (r.get("facet") or "core") == f]
        for a in arm_names:
            by_facet[f][a] = round(statistics.fmean([r["judge"]["scores"][a]["useful"] for r in rs]), 2)
    return {
        "n_rows": len(records), "n_valid": len(valid),
        "errors": dict(Counter((r.get("error") or "invalid judge output")[:60] for r in records if r not in valid)),
        "per_arm": per_arm,
        "pairwise_win_rate": pairwise,
        "position_check": {"n": len(checks), "same_winner": rate(same_top, len(checks)),
                           "rank_spearman_mean": round(statistics.fmean(rho), 3) if rho else None},
        "pool_answers_objective": dict(Counter(r["judge"].get("pool_answers_objective") for r in valid)),
        "useful_by_facet": dict(by_facet),
        "cost_usd": round(sum(r["cost_usd"] for r in records), 4),
    }


def spearman(r1: list[str], r2: list[str]) -> float:
    n = len(r1)
    if n < 2:
        return 1.0
    d2 = sum((r1.index(x) - r2.index(x)) ** 2 for x in r1)
    return round(1 - 6 * d2 / (n * (n * n - 1)), 3)


def summarize_judge_dir(d: Path, records: list[dict] | None = None) -> dict:
    meta = json.loads((d / "judge.json").read_text(encoding="utf-8"))
    records = records if records is not None else load_records(d)
    arm_names = list(meta["arms"])
    s = {"judge_id": d.name, "model": meta["config"]["llm"]["model"], "arms": meta["arms"],
         "skipped_rows": meta.get("skipped_rows") or {},
         **summarize_judge(records, arm_names)}
    synth = {}
    for arm, sd in (meta.get("synth_dirs") or {}).items():
        sp = Path(sd) / "summary.json"
        synth[arm] = (json.loads(sp.read_text(encoding="utf-8")) if sp.exists()
                      else summarize_synth_dir(Path(sd)) if Path(sd).exists() else None)
    s["objective"] = synth
    human = d / "human_review.csv"
    if human.exists() and _human_filled(human):
        s["human"] = score_human(d)
    (d / "summary.json").write_text(json.dumps(s, indent=2, ensure_ascii=False), encoding="utf-8")
    (d / "compare.md").write_text(render_compare(s), encoding="utf-8")
    return s


def _pct(v) -> str:
    return "-" if v is None else f"{v:.0%}"


def render_compare(s: dict) -> str:
    lines = [f"# Luna answer quality by arm: `{s['judge_id']}`", "",
             f"Judge `{s['model']}` on {s['n_valid']}/{s['n_rows']} rows"
             f" ({len(s['skipped_rows'])} rows not judged: an arm errored {sorted(s['skipped_rows'])})"
             f" · position check: same winner "
             f"{_pct(s['position_check']['same_winner'])}, rank ρ {s['position_check']['rank_spearman_mean']} "
             f"(n={s['position_check']['n']}) · judge cost ${s['cost_usd']}", "",
             "| arm | answered | jev abstain | complete | ungrounded tok | search-talk | bad tags | names subject "
             "| judge correct | complete | subject | useful | mean rank | wins | total p50 ms | total p95 ms | $ / answer |",
             "|" + "---|" * 17]
    for arm, j in s["per_arm"].items():
        o = s["objective"].get(arm) or {}
        a, c, g, t = (o.get("answering", {}), o.get("contract", {}), o.get("grounding", {}),
                      o.get("timing_ms", {}).get("total", {}))
        lines.append(f"| {arm} | {_pct(a.get('answer_rate'))} | {_pct(a.get('jev_abstain_rate'))} | "
                     f"{_pct(a.get('complete_rate'))} | {_pct(g.get('ungrounded_token_rate'))} | "
                     f"{_pct(c.get('search_talk_rows'))} | {_pct(c.get('invalid_tag_rows'))} | "
                     f"{_pct((o.get('subject') or {}).get('names_subject'))} | {j['correct']} | {j['complete']} | "
                     f"{j['subject']} | {j['useful']} | {j['mean_rank']} | {_pct(j['win_rate'])} | {t.get('p50')} | "
                     f"{t.get('p95')} | {(o.get('cost_usd') or {}).get('per_answer')} |")
    lines += ["", "Pairwise (row beats column, share of rows):", "",
              "| | " + " | ".join(s["per_arm"]) + " |", "|---|" + "---|" * len(s["per_arm"])]
    for a, row in s["pairwise_win_rate"].items():
        lines.append(f"| {a} | " + " | ".join("-" if b == a else _pct(row[b]) for b in s["per_arm"]) + " |")
    lines += ["", "Judge `useful` by facet:", "", "| facet | " + " | ".join(s["per_arm"]) + " |",
              "|---|" + "---|" * len(s["per_arm"])]
    for f, row in s["useful_by_facet"].items():
        lines.append(f"| {f} | " + " | ".join(str(row.get(a)) for a in s["per_arm"]) + " |")
    if s.get("human"):
        h = s["human"]
        lines += ["", f"Human spot-check ({h['n_rows']} rows): judge agreement exact {_pct(h['exact'])}, "
                      f"±1 {_pct(h['within_1'])}, rank ρ {h['rank_spearman_mean']}; human mean useful "
                      + ", ".join(f"{a} {v}" for a, v in h["human_useful"].items())]
    return "\n".join(lines) + "\n"


# ---------- human spot-check ----------

def export_human(out: Path, p: dict, cfg: dict) -> None:
    """Stratified by facet, same blind labels and order as the judge saw."""
    n = int(cfg["human_sample"])
    by_facet: dict[str, list[dict]] = defaultdict(list)
    for x in p["items"]:
        by_facet[x["facet"] or "core"].append(x)
    rng = random.Random(int(cfg["seed"]))
    for v in by_facet.values():
        rng.shuffle(v)
    picked = []
    while len(picked) < min(n, len(p["items"])):  # round-robin over facets
        for f in sorted(by_facet):
            if by_facet[f] and len(picked) < n:
                picked.append(by_facet[f].pop())
    picked.sort(key=lambda x: x["row_id"])
    key = {}
    with (out / "human_review.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["row_id", "label", "objective", "answer", "missing", *CRITERIA, "rank", "notes"])
        for x in picked:
            key[x["row_id"]] = {}
            for k, a in enumerate(x["order"]):
                ans = x["answers"][a]
                w.writerow([x["row_id"], LABELS[k], x["objective"] if k == 0 else "",
                            ans["text"] or "(EMPTY: No data available)", ans.get("missing") or "",
                            "", "", "", "", "", ""])
                key[x["row_id"]][LABELS[k]] = p["arm_names"][a]
    (out / "human_key.json").write_text(json.dumps(key, indent=2, ensure_ascii=False), encoding="utf-8")
    md = ["# Evidence pools for the human spot-check", "",
          "Score each answer in human_review.csv 1-5 on correct / complete / subject / useful (same rubric as "
          "the judge, see src/wsx/judge.py JUDGE_SYSTEM), and rank the answers of a row 1 = best.", ""]
    for x in picked:
        md += [f"## {x['row_id']}", "", f"**Objective:** {x['objective']}", ""]
        md += [f"- **[{e['sid']}]** [{e.get('title') or '-'}]({e.get('url')}) — {e.get('domain')}: "
               f"{' '.join((e.get('text') or '').split())[:600]}" for e in x["pool"]]
        md.append("")
    (out / "human_evidence.md").write_text("\n".join(md) + "\n", encoding="utf-8")


def _human_filled(path: Path) -> bool:
    with path.open(encoding="utf-8-sig") as f:
        return any((r.get("useful") or "").strip() for r in csv.DictReader(f))


def score_human(d: Path) -> dict:
    key = json.loads((d / "human_key.json").read_text(encoding="utf-8"))
    judged = {r["row_id"]: r for r in load_records(d) if r.get("judge") and r["judge"]["valid"]}
    rows: dict[str, dict[str, dict]] = defaultdict(dict)
    with (d / "human_review.csv").open(encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            if (r.get("useful") or "").strip():
                rows[r["row_id"]][key[r["row_id"]][r["label"]]] = r
    exact = within = total = 0
    rho, human_useful = [], defaultdict(list)
    for row_id, by_arm in rows.items():
        for arm, r in by_arm.items():
            human_useful[arm].append(float(r["useful"]))
        j = judged.get(row_id)
        if not j:
            continue
        for arm, r in by_arm.items():
            for c in CRITERIA:
                if (r.get(c) or "").strip():
                    diff = abs(float(r[c]) - float(j["judge"]["scores"][arm][c]))
                    exact += diff == 0
                    within += diff <= 1
                    total += 1
        if all((r.get("rank") or "").strip() for r in by_arm.values()) and len(by_arm) == len(j["judge"]["ranking"]):
            human_rank = [a for a, _ in sorted(by_arm.items(), key=lambda kv: float(kv[1]["rank"]))]
            rho.append(spearman(human_rank, j["judge"]["ranking"]))
    return {"n_rows": len(rows), "exact": rate(exact, total), "within_1": rate(within, total),
            "rank_spearman_mean": round(statistics.fmean(rho), 3) if rho else None,
            "human_useful": {a: round(statistics.fmean(v), 2) for a, v in human_useful.items()}}
