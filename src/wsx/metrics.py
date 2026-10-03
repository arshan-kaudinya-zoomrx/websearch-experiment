"""Automatic metrics. Definitions are in docs/METHODOLOGY.md."""

from __future__ import annotations

import json
import statistics
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import yaml

from . import CONFIG_DIR
from .dataset import load_questions, normalize
from .providers import get_provider

DOMAIN_CATEGORIES_PATH = CONFIG_DIR / "domain_categories.yaml"


# ---------- helpers ----------

def load_records(run_dir: Path) -> list[dict]:
    with (run_dir / "results.jsonl").open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def load_domain_categories(path: Path = DOMAIN_CATEGORIES_PATH) -> dict[str, list[str]]:
    if not path.exists():
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def categorize(domain: str, categories: dict[str, list[str]]) -> str:
    for cat, domains in categories.items():
        for d in domains:
            if domain == d or domain.endswith("." + d):
                return cat
    return "other"


def anchor_hit(result: dict, anchors: list[str]) -> bool:
    text = normalize(" ".join([result.get("title", ""), result.get("url", ""), result.get("snippet", "")]))
    return any(normalize(a) and normalize(a) in text for a in anchors)


def parse_date(value: str | None) -> datetime | None:
    if not value:
        return None
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%Y-%m"):
        try:
            return datetime.strptime(value[:10] if fmt == "%Y-%m-%d" else value, fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def pct(values: list[float], q: float) -> float | None:
    if not values:
        return None
    s = sorted(values)
    idx = (len(s) - 1) * q
    lo, hi = int(idx), min(int(idx) + 1, len(s) - 1)
    return round(s[lo] + (s[hi] - s[lo]) * (idx - lo), 1)


def rate(n: int, d: int) -> float:
    return round(n / d, 4) if d else 0.0


# ---------- per-record ----------

def score_record(rec: dict) -> dict:
    hits = [r["rank"] for r in rec["results"] if anchor_hit(r, rec["anchors"])]
    first = min(hits) if hits else None
    return {"hit_ranks": hits, "first_hit_rank": first}


# ---------- run-level ----------

def summarize_records(records: list[dict], categories: dict, cost_per_request: float,
                      now: datetime | None = None) -> dict:
    now = now or datetime.now(timezone.utc)
    n = len(records)
    ok = [r for r in records if r["ok"]]
    latencies = [r["latency_ms"] for r in ok]
    scored = [(r, score_record(r)) for r in ok]

    # A batch request can return results grouped per query (rank restarts per group);
    # hit@k is "any hit at rank <= k" in either case.
    def hit_at(k: int) -> float:
        return rate(sum(1 for _, s in scored if any(rk <= k for rk in s["hit_ranks"])), len(scored))

    all_results = [res for r in ok for res in r["results"]]
    hit_fraction = [len(s["hit_ranks"]) / r["n_results"] for r, s in scored if r["n_results"]]

    # Objective coverage: a row counts if ANY of its requests returned an anchor hit.
    by_row: dict[str, bool] = defaultdict(bool)
    for r, s in scored:
        by_row[r["row_id"]] |= bool(s["hit_ranks"])
    rows_total = {r["row_id"] for r in records}

    cats = Counter(categorize(res["domain"], categories) for res in all_results)
    domains = Counter(res["domain"] for res in all_results)

    dated = [d for d in (parse_date(res.get("date") or res.get("last_updated")) for res in all_results) if d]
    ages = [(now - d).days for d in dated]

    # Latency stability across repeats (only meaningful with repeat > 1).
    per_case = defaultdict(list)
    for r in ok:
        per_case[r["case_id"]].append(r["latency_ms"])
    sds = [statistics.stdev(v) for v in per_case.values() if len(v) > 1]

    return {
        "n_requests": n,
        "n_ok": len(ok),
        "n_cases": len({r["case_id"] for r in records}),
        "n_rows": len(rows_total),
        "error_rate": rate(n - len(ok), n),
        "errors": dict(Counter(r["error"] for r in records if not r["ok"])),
        "zero_result_rate": rate(sum(1 for r in ok if r["n_results"] == 0), len(ok)),
        "latency_ms": {
            "p50": pct(latencies, 0.5), "p90": pct(latencies, 0.9), "p95": pct(latencies, 0.95),
            "max": round(max(latencies), 1) if latencies else None,
            "mean": round(statistics.fmean(latencies), 1) if latencies else None,
            "repeat_sd_mean": round(statistics.fmean(sds), 1) if sds else None,
        },
        "results_per_request_mean": round(statistics.fmean([r["n_results"] for r in ok]), 2) if ok else 0,
        "snippet_chars_mean": round(statistics.fmean([len(x["snippet"]) for x in all_results]), 0) if all_results else 0,
        "anchor": {
            "hit_at_1": hit_at(1), "hit_at_3": hit_at(3), "hit_at_k": hit_at(10 ** 6),
            "hit_fraction_mean": round(statistics.fmean(hit_fraction), 4) if hit_fraction else 0.0,
        },
        "objective_coverage": rate(sum(by_row.values()), len(rows_total)),
        "rows_without_hit": sorted(r for r in rows_total if not by_row.get(r)),
        "source_mix": {k: rate(v, len(all_results)) for k, v in cats.most_common()},
        "unique_domains": len(domains),
        "top_domains": dict(domains.most_common(15)),
        "freshness": {
            "dated_share": rate(len(dated), len(all_results)),
            "median_age_days": statistics.median(ages) if ages else None,
            "within_12m_share": rate(sum(1 for a in ages if a <= 365), len(ages)),
        },
        "cost_usd": round(len(ok) * cost_per_request, 4),  # failed requests are not billed
        "price_per_1k_requests": round(cost_per_request * 1000, 3),
    }


def summarize_run(run_dir: Path, records: list[dict] | None = None, meta: dict | None = None,
                  refresh_anchors: bool = False) -> dict:
    run_dir = Path(run_dir)
    meta = meta or json.loads((run_dir / "run.json").read_text(encoding="utf-8"))
    records = records if records is not None else load_records(run_dir)
    if refresh_anchors:
        anchors = {q["id"]: q["anchors"] for q in load_questions()}
        for r in records:
            r["anchors"] = anchors.get(r["row_id"], r["anchors"])
    cfg = meta["config"]
    provider = get_provider(cfg["provider"], cfg["params"], cfg["run"]["timeout_s"])
    now = datetime.fromisoformat(meta["started_at"]) if meta.get("started_at") else None
    summary = {
        "run_id": meta["run_id"],
        "config_name": cfg["name"],
        "provider": cfg["provider"],
        "mode": cfg["mode"],
        "params": cfg["params"],
        "repeat": cfg["run"]["repeat"],
        "started_at": meta.get("started_at"),
        "duration_s": meta.get("duration_s"),
        **summarize_records(records, load_domain_categories(), provider.cost_per_request(cfg["pricing"]), now),
    }
    old_path = run_dir / "summary.json"
    if old_path.exists():  # keep manual-review scores across re-summaries
        old = json.loads(old_path.read_text(encoding="utf-8"))
        if "review" in old:
            summary["review"] = old["review"]
    old_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    return summary
