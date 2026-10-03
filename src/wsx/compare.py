"""Compare N runs. The first run is the baseline.

Comparison is at row (objective) level, so runs in different modes are comparable:
for each row we take the union of URLs across its requests (repeat 0) and whether
any result hit the anchor.
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from . import COMPARISONS_DIR
from .metrics import load_records, score_record

METRIC_ROWS = [
    ("mode", lambda s: s["mode"]),
    ("search_type", lambda s: s["params"].get("search_type", "-")),
    ("max_results", lambda s: s["params"].get("max_results", "-")),
    ("requests", lambda s: s["n_requests"]),
    ("error rate", lambda s: f"{s['error_rate']:.1%}"),
    ("zero-result rate", lambda s: f"{s['zero_result_rate']:.1%}"),
    ("latency p50 ms", lambda s: s["latency_ms"]["p50"]),
    ("latency p95 ms", lambda s: s["latency_ms"]["p95"]),
    ("results / request", lambda s: s["results_per_request_mean"]),
    ("anchor hit@1", lambda s: f"{s['anchor']['hit_at_1']:.1%}"),
    ("anchor hit@3", lambda s: f"{s['anchor']['hit_at_3']:.1%}"),
    ("anchor hit@k", lambda s: f"{s['anchor']['hit_at_k']:.1%}"),
    ("objective coverage", lambda s: f"{s['objective_coverage']:.1%}"),
    ("registry share", lambda s: f"{s['source_mix'].get('registry', 0):.1%}"),
    ("literature share", lambda s: f"{s['source_mix'].get('literature', 0):.1%}"),
    ("company/press share", lambda s: f"{s['source_mix'].get('company_press', 0):.1%}"),
    ("dated within 12m", lambda s: f"{s['freshness']['within_12m_share']:.1%}"),
    ("cost USD", lambda s: s["cost_usd"]),
    ("review precision", lambda s: f"{s['review']['precision']:.1%}" if s.get("review") else "-"),
]


def short_label(run_id: str) -> str:
    """'20261003-101500__perplexity-web__queries' -> 'perplexity-web__queries'."""
    return run_id.split("__", 1)[1] if "__" in run_id else run_id


def row_view(records: list[dict]) -> dict[str, dict]:
    rows: dict[str, dict] = {}
    for r in records:
        if r["repeat"] != 0 or not r["ok"]:
            continue
        row = rows.setdefault(r["row_id"], {"urls": set(), "hit": False})
        row["urls"].update(x["url"] for x in r["results"])
        row["hit"] |= bool(score_record(r)["hit_ranks"])
    return rows


def compare_runs(run_dirs: list[Path]) -> tuple[Path, Path]:
    run_dirs = [Path(d) for d in run_dirs]
    summaries = [json.loads((d / "summary.json").read_text(encoding="utf-8")) for d in run_dirs]
    views = [row_view(load_records(d)) for d in run_dirs]
    labels = [short_label(s["run_id"]) for s in summaries]

    base_view = views[0]
    pairwise = []
    for label, view in zip(labels[1:], views[1:]):
        common = sorted(set(base_view) & set(view))
        jacc = {}
        wins, losses = [], []
        for rid in common:
            a, b = base_view[rid]["urls"], view[rid]["urls"]
            jacc[rid] = round(len(a & b) / len(a | b), 3) if a | b else 1.0
            if view[rid]["hit"] and not base_view[rid]["hit"]:
                wins.append(rid)
            elif base_view[rid]["hit"] and not view[rid]["hit"]:
                losses.append(rid)
        pairwise.append({
            "baseline": labels[0], "candidate": label, "rows_compared": len(common),
            "url_jaccard_mean": round(sum(jacc.values()) / len(jacc), 3) if jacc else None,
            "coverage_wins": wins, "coverage_losses": losses, "url_jaccard_by_row": jacc,
        })

    out = {
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "runs": [s["run_id"] for s in summaries],
        "metrics": {lab: {name: fn(s) for name, fn in METRIC_ROWS} for lab, s in zip(labels, summaries)},
        "pairwise_vs_baseline": pairwise,
    }

    COMPARISONS_DIR.mkdir(parents=True, exist_ok=True)
    stem = f"{datetime.now():%Y%m%d-%H%M%S}__" + "__vs__".join(labels)
    if len(stem) > 150:
        stem = f"{datetime.now():%Y%m%d-%H%M%S}__{labels[0]}__vs__{len(labels) - 1}-runs"
    json_path = COMPARISONS_DIR / f"{stem}.json"
    md_path = COMPARISONS_DIR / f"{stem}.md"
    json_path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    md_path.write_text(render_md(out, labels), encoding="utf-8")
    return json_path, md_path


def render_md(out: dict, labels: list[str]) -> str:
    lines = [f"# Comparison ({out['created_at']})", "", "Baseline: `" + labels[0] + "`", ""]
    lines.append("| metric | " + " | ".join(f"`{l}`" for l in labels) + " |")
    lines.append("|---|" + "---|" * len(labels))
    for name, _ in METRIC_ROWS:
        lines.append(f"| {name} | " + " | ".join(str(out["metrics"][l][name]) for l in labels) + " |")
    lines += ["", "## vs baseline (row level)", ""]
    lines.append("| candidate | rows | URL Jaccard | coverage wins | coverage losses |")
    lines.append("|---|---|---|---|---|")
    for p in out["pairwise_vs_baseline"]:
        lines.append(f"| `{p['candidate']}` | {p['rows_compared']} | {p['url_jaccard_mean']} | "
                     f"{len(p['coverage_wins'])} {', '.join(p['coverage_wins'])} | "
                     f"{len(p['coverage_losses'])} {', '.join(p['coverage_losses'])} |")
    return "\n".join(lines) + "\n"
