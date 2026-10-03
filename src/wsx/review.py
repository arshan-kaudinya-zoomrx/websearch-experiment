"""Manual review sheet: export top-k results per request, then score the filled sheet.

Reviewers fill `relevant` (Y/N) per result and `answers_objective` (Y/N) for any
result that alone answers the row's objective. Blank = not reviewed.
The anchor-hit proxy is deliberately NOT in the sheet (avoids biasing reviewers);
it is joined back in at scoring time.
"""

from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path

from .metrics import anchor_hit, load_records, rate

COLUMNS = ["case_id", "row_id", "objective", "query", "rank", "title", "url", "domain", "date",
           "snippet", "relevant", "answers_objective", "notes"]
YES, NO = {"y", "yes", "1", "true"}, {"n", "no", "0", "false"}


def export_review(run_dir: Path, records: list[dict] | None = None, top_k: int = 5,
                  force: bool = False, filename: str = "review.csv") -> Path:
    run_dir = Path(run_dir)
    path = run_dir / filename
    if path.exists() and not force and _has_labels(path):
        raise SystemExit(f"{path} already has labels; pass --force to overwrite.")
    records = records if records is not None else load_records(run_dir)
    with path.open("w", encoding="utf-8-sig", newline="") as f:  # utf-8-sig opens cleanly in Excel
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        for rec in sorted(records, key=lambda r: r["case_id"]):
            if rec["repeat"] != 0:
                continue
            query = rec["query"] if isinstance(rec["query"], str) else " || ".join(rec["query"])
            for res in rec["results"]:
                if res["rank"] > top_k:
                    continue
                w.writerow({
                    "case_id": rec["case_id"], "row_id": rec["row_id"], "objective": rec["objective"],
                    "query": query, "rank": res["rank"], "title": res["title"], "url": res["url"],
                    "domain": res["domain"], "date": res.get("date") or "",
                    "snippet": res["snippet"].replace("\n", " ")[:300],
                    "relevant": "", "answers_objective": "", "notes": "",
                })
    return path


def _has_labels(path: Path) -> bool:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return any((row.get("relevant") or "").strip() or (row.get("answers_objective") or "").strip()
                   for row in csv.DictReader(f))


def _flag(value: str | None) -> bool | None:
    v = (value or "").strip().lower()
    return True if v in YES else False if v in NO else None


def score_review(run_dir: Path, filename: str = "review.csv") -> dict:
    run_dir = Path(run_dir)
    records = {(r["case_id"]): r for r in load_records(run_dir) if r["repeat"] == 0}
    with (run_dir / filename).open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    labeled, per_case, answerable = [], defaultdict(list), defaultdict(bool)
    agree = tp = fp = fn = 0
    for row in rows:
        rel = _flag(row.get("relevant"))
        ans = _flag(row.get("answers_objective"))
        if ans:
            answerable[row["row_id"]] = True
        elif ans is False:
            answerable.setdefault(row["row_id"], False)
        if rel is None:
            continue
        labeled.append(rel)
        per_case[row["case_id"]].append(rel)
        rec = records.get(row["case_id"])
        if rec:
            res = next((x for x in rec["results"] if str(x["rank"]) == str(row["rank"]) and x["url"] == row["url"]), None)
            if res is not None:
                proxy = anchor_hit(res, rec["anchors"])
                agree += proxy == rel
                tp += proxy and rel
                fp += proxy and not rel
                fn += (not proxy) and rel

    review = {
        "sheet": filename,
        "labeled_results": len(labeled),
        "labeled_requests": len(per_case),
        "precision": rate(sum(labeled), len(labeled)),
        "precision_per_request_mean": round(sum(rate(sum(v), len(v)) for v in per_case.values()) / len(per_case), 4) if per_case else 0.0,
        "any_relevant_rate": rate(sum(1 for v in per_case.values() if any(v)), len(per_case)),
        "rows_judged_for_answer": len(answerable),
        "objective_answerable_rate": rate(sum(answerable.values()), len(answerable)),
        "anchor_proxy_vs_human": {
            "agreement": rate(agree, agree + fp + fn),  # fp + fn = disagreements
            "proxy_precision": rate(tp, tp + fp),
            "proxy_recall": rate(tp, tp + fn),
        },
    }
    summary_path = run_dir / "summary.json"
    summary = json.loads(summary_path.read_text(encoding="utf-8")) if summary_path.exists() else {}
    summary["review"] = review
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    return review
