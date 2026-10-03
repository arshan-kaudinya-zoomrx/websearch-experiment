"""Build cases from the dataset, execute them against a provider, write the run folder."""

from __future__ import annotations

import asyncio
import json
import platform
import random
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import httpx

from . import RUNS_DIR, __version__
from .dataset import JSONL_PATH, file_sha256, load_questions, select_rows
from .providers import Provider, get_provider

RETRYABLE = {408, 409, 425, 429, 500, 502, 503, 504}


def build_cases(questions: list[dict], mode: str, max_batch: int = 5) -> list[dict]:
    """queries: one case per sub-query | objective: one per row (objective text)
    | batch: one per row, all sub-queries in one multi-query request."""
    cases = []
    for q in questions:
        base = {"row_id": q["id"], "objective": q["objective"], "anchors": q["anchors"], "mode": mode}
        if mode == "queries":
            for i, text in enumerate(q["queries"], start=1):
                cases.append({**base, "case_id": f"{q['id']}-{i}", "query": text})
        elif mode == "objective":
            cases.append({**base, "case_id": f"{q['id']}-obj", "query": q["objective"]})
        elif mode == "batch":
            for start in range(0, len(q["queries"]), max_batch):
                chunk = q["queries"][start:start + max_batch]
                suffix = "" if start == 0 else f"-{start // max_batch + 1}"
                cases.append({**base, "case_id": f"{q['id']}-batch{suffix}", "query": chunk})
    return cases


def slug(text: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "-", text).strip("-").lower()


def make_run_dir(cfg: dict, runs_dir: Path | None = None) -> Path:
    runs_dir = runs_dir or RUNS_DIR
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    base = f"{ts}__{slug(cfg['provider'])}-{slug(cfg['name'])}__{cfg['mode']}"
    run_dir = runs_dir / base
    n = 2
    while run_dir.exists():
        run_dir = runs_dir / f"{base}-{n}"
        n += 1
    run_dir.mkdir(parents=True)
    return run_dir


def plan(cfg: dict) -> dict:
    """Everything needed to run (or dry-run) a config."""
    run = cfg["run"]
    provider = get_provider(cfg["provider"], cfg["params"], run["timeout_s"])
    if cfg["mode"] == "batch" and provider.max_queries_per_request < 2:
        raise SystemExit(f"Provider {provider.name} does not support multi-query batch mode.")
    sel = cfg["selection"]
    rows = select_rows(load_questions(), sel.get("rows"), sel.get("sample"), sel.get("seed", 42))
    cases = build_cases(rows, cfg["mode"], provider.max_queries_per_request)
    n_requests = len(cases) * int(run["repeat"])
    est_cost = n_requests * provider.cost_per_request(cfg["pricing"])
    return {"provider": provider, "rows": rows, "cases": cases,
            "n_requests": n_requests, "est_cost_usd": round(est_cost, 4)}


async def _run_one(provider: Provider, client: httpx.AsyncClient, case: dict, repeat_idx: int,
                   retries: int, sem: asyncio.Semaphore, save_raw: bool) -> dict:
    async with sem:
        attempts = 0
        while True:
            attempts += 1
            resp = await provider.search(client, case["query"])
            retryable = resp.status is None or resp.status in RETRYABLE
            if resp.ok or not retryable or attempts > retries:
                break
            await asyncio.sleep(min(30, 2 ** attempts) + random.random())
    raw = resp.raw
    if not save_raw and isinstance(raw, dict):
        raw = {k: v for k, v in raw.items() if k != "results"} if resp.ok else raw
    return {
        **case,
        "repeat": repeat_idx,
        "provider": provider.name,
        "request": resp.request,
        "ok": resp.ok,
        "status": resp.status,
        "error": resp.error,
        "attempts": attempts,
        "latency_ms": round(resp.latency_ms, 1),
        "n_results": len(resp.results),
        "results": resp.results,
        "raw": raw,
        "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }


async def _execute(provider: Provider, cases: list[dict], run: dict, out_path: Path,
                   transport: httpx.AsyncBaseTransport | None = None) -> list[dict]:
    sem = asyncio.Semaphore(int(run["concurrency"]))
    records: list[dict] = []
    total = len(cases) * int(run["repeat"])
    limits = httpx.Limits(max_connections=int(run["concurrency"]) * 2)
    async with httpx.AsyncClient(limits=limits, transport=transport) as client:
        # Repeats run as successive passes so latency samples are spread over time.
        with out_path.open("w", encoding="utf-8") as f:
            for r in range(int(run["repeat"])):
                tasks = [asyncio.create_task(
                    _run_one(provider, client, c, r, int(run["retries"]), sem, bool(run["save_raw"])))
                    for c in cases]
                for fut in asyncio.as_completed(tasks):
                    rec = await fut
                    records.append(rec)
                    f.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    f.flush()
                    mark = "ok " if rec["ok"] else "ERR"
                    print(f"  [{len(records):>4}/{total}] {mark} {rec['case_id']:<14} "
                          f"{rec['latency_ms']:>7.0f} ms  {rec['n_results']:>2} results"
                          + (f"  {rec['error']}" if rec["error"] else ""), flush=True)
    records.sort(key=lambda x: (x["repeat"], x["case_id"]))
    return records


def execute(cfg: dict, cli_args: list[str] | None = None,
            transport: httpx.AsyncBaseTransport | None = None, runs_dir: Path | None = None) -> Path:
    """Run a config end to end; returns the run directory. `transport` is for tests."""
    from .metrics import summarize_run
    from .review import export_review

    p = plan(cfg)
    provider: Provider = p["provider"]
    provider.check_ready()
    max_cost = float(cfg["run"].get("max_cost_usd") or 0)
    if max_cost and p["est_cost_usd"] > max_cost:
        raise SystemExit(f"Estimated cost ${p['est_cost_usd']} exceeds run.max_cost_usd=${max_cost}. "
                         f"Raise it with --set run.max_cost_usd=<n>.")

    run_dir = make_run_dir(cfg, runs_dir)
    started = datetime.now(timezone.utc)
    meta = {
        "run_id": run_dir.name,
        "started_at": started.isoformat(timespec="seconds"),
        "finished_at": None,
        "config": cfg,
        "cli_args": cli_args or sys.argv[1:],
        "dataset": {
            "path": "data/questions.jsonl",
            "sha256": file_sha256(JSONL_PATH),
            "row_ids": [r["id"] for r in p["rows"]],
        },
        "n_cases": len(p["cases"]),
        "n_requests_planned": p["n_requests"],
        "est_cost_usd": p["est_cost_usd"],
        "env": {"wsx": __version__, "python": platform.python_version(), "platform": platform.platform()},
    }
    (run_dir / "run.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Run {run_dir.name}: {len(p['rows'])} rows, {len(p['cases'])} cases, "
          f"{p['n_requests']} requests, est ${p['est_cost_usd']}")
    records = asyncio.run(_execute(provider, p["cases"], cfg["run"], run_dir / "results.jsonl", transport))

    finished = datetime.now(timezone.utc)
    meta["finished_at"] = finished.isoformat(timespec="seconds")
    meta["duration_s"] = round((finished - started).total_seconds(), 1)
    (run_dir / "run.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")

    summary = summarize_run(run_dir, records=records, meta=meta)
    export_review(run_dir, records=records, top_k=int(cfg["run"].get("review_top_k", 5)))
    print_summary(summary)
    print(f"Saved to {run_dir}")
    return run_dir


def print_summary(s: dict) -> None:
    lat, anc = s["latency_ms"], s["anchor"]
    print(f"  requests={s['n_requests']} errors={s['error_rate']:.1%} zero-results={s['zero_result_rate']:.1%}")
    print(f"  latency p50={lat['p50']} p95={lat['p95']} ms | results/req={s['results_per_request_mean']}")
    print(f"  anchor hit@1={anc['hit_at_1']:.1%} hit@3={anc['hit_at_3']:.1%} hit@k={anc['hit_at_k']:.1%} "
          f"| objective coverage={s['objective_coverage']:.1%} | cost=${s['cost_usd']}")
