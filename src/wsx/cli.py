"""wsx command line. Run `uv run wsx -h` or `uv run wsx <command> -h`."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from dotenv import load_dotenv

from . import ROOT, RUNS_DIR


def _run_dir(value: str) -> Path:
    """Accept a full path, a run folder name, or a unique prefix/substring of one."""
    p = Path(value)
    if p.is_dir():
        return p
    matches = [d for d in RUNS_DIR.iterdir() if d.is_dir() and value in d.name] if RUNS_DIR.exists() else []
    if len(matches) == 1:
        return matches[0]
    if not matches:
        raise SystemExit(f"No run folder matches '{value}'")
    raise SystemExit(f"'{value}' matches {len(matches)} runs; be more specific:\n  " +
                     "\n  ".join(m.name for m in matches))


def _resolve_runs(values: list[str]) -> list[Path]:
    out = []
    for v in values:
        if v == "latest":
            runs = sorted(d for d in RUNS_DIR.iterdir() if d.is_dir())
            if not runs:
                raise SystemExit("No runs yet.")
            out.append(runs[-1])
        else:
            out.append(_run_dir(v))
    return out


def _add_selection_args(p: argparse.ArgumentParser) -> None:
    p.add_argument("--mode", choices=["queries", "objective", "batch"], help="override config mode")
    p.add_argument("--rows", help='rows to run: "all", "1-10", "1-5,9", "q003,q017"')
    p.add_argument("--sample", type=int, help="random sample of N rows (after --rows)")
    p.add_argument("--seed", type=int, help="seed for --sample")
    p.add_argument("--repeat", type=int, help="run every case N times (latency stability)")
    p.add_argument("--concurrency", type=int, help="parallel requests")
    p.add_argument("--set", action="append", default=[], metavar="KEY=VALUE",
                   help="override any config key, e.g. --set params.max_results=20 (repeatable)")


def cmd_prepare(args) -> None:
    from .dataset import build_questions, write_questions, JSONL_PATH
    qs = build_questions()
    write_questions(qs)
    n_q = sum(len(q["queries"]) for q in qs)
    print(f"Wrote {JSONL_PATH.relative_to(ROOT)}: {len(qs)} rows, {n_q} sub-queries")
    if args.show:
        for q in qs:
            tag = "*" if q["anchors_source"] == "override" else " "
            print(f"  {q['id']}{tag} {len(q['queries'])}q  anchors={q['anchors']}")
        print("  (* = from data/anchor_overrides.yaml)")


def cmd_run(args) -> None:
    from .config import build_config
    from .runner import execute, plan
    cfg = build_config(args.config, args.set, mode=args.mode, rows=args.rows, sample=args.sample,
                       seed=args.seed, repeat=args.repeat, concurrency=args.concurrency, name=args.name)
    if args.dry_run:
        p = plan(cfg)
        example = p["cases"][0] if p["cases"] else None
        print(json.dumps({
            "config": cfg,
            "rows": len(p["rows"]), "cases": len(p["cases"]), "requests": p["n_requests"],
            "est_cost_usd": p["est_cost_usd"],
            "example_request": p["provider"].public_request(example["query"]) if example else None,
        }, indent=2, ensure_ascii=False))
        return
    execute(cfg)


def cmd_matrix(args) -> None:
    from .compare import compare_runs
    from .config import build_config
    from .report import build_report
    from .runner import execute, plan
    modes = args.modes.split(",") if args.modes else [None]
    cfgs = [build_config(c, args.set, mode=m, rows=args.rows, sample=args.sample, seed=args.seed,
                         repeat=args.repeat, concurrency=args.concurrency)
            for c in args.config for m in modes]
    plans = [plan(c) for c in cfgs]
    total_cost = sum(p["est_cost_usd"] for p in plans)
    for c, p in zip(cfgs, plans):
        print(f"  {c['name']:<28} {c['mode']:<10} {p['n_requests']:>5} requests  ${p['est_cost_usd']}")
    print(f"Matrix: {len(cfgs)} runs, {sum(p['n_requests'] for p in plans)} requests, est ${round(total_cost, 4)}")
    if args.dry_run:
        return
    run_dirs = [execute(c) for c in cfgs]
    if len(run_dirs) > 1:
        j, m = compare_runs(run_dirs)
        print(f"Comparison: {m}")
    build_report()
    print("Report: outputs/report.md")


def cmd_summarize(args) -> None:
    from .metrics import summarize_run
    from .runner import print_summary
    for d in _resolve_runs(args.runs):
        s = summarize_run(d, refresh_anchors=args.refresh_anchors)
        print(d.name)
        print_summary(s)


def cmd_compare(args) -> None:
    from .compare import compare_runs
    j, m = compare_runs(_resolve_runs(args.runs))
    print(m.read_text(encoding="utf-8"))
    print(f"Saved {j}\n      {m}")


def cmd_review(args) -> None:
    from .review import export_review, score_review
    d = _resolve_runs([args.run])[0]
    if args.action == "export":
        print(f"Wrote {export_review(d, top_k=args.top_k, force=args.force)}")
    else:
        print(json.dumps(score_review(d), indent=2))


def cmd_report(args) -> None:
    from .report import build_report
    md, _ = build_report()
    print(md)


def cmd_providers(args) -> None:
    from .providers import PROVIDERS
    for name, cls in PROVIDERS.items():
        print(f"{name:<12} env={cls.env_key:<22} max_queries_per_request={cls.max_queries_per_request}")


def main(argv: list[str] | None = None) -> None:
    load_dotenv(ROOT / ".env")
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(prog="wsx", description="Web-search experiment harness")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("prepare", help="CSV -> data/questions.jsonl (+ anchors)")
    p.add_argument("--show", action="store_true", help="print every row's anchors")
    p.set_defaults(func=cmd_prepare)

    p = sub.add_parser("run", help="run one config")
    p.add_argument("-c", "--config", required=True, help="configs/<name>.yaml or just <name>")
    p.add_argument("--name", help="override config name (used in the run folder name)")
    p.add_argument("--dry-run", action="store_true", help="show plan + cost, call nothing")
    _add_selection_args(p)
    p.set_defaults(func=cmd_run)

    p = sub.add_parser("matrix", help="run several configs x modes, then compare + report")
    p.add_argument("-c", "--config", action="append", required=True, help="repeatable")
    p.add_argument("--modes", help="comma list, e.g. queries,objective,batch (default: each config's mode)")
    p.add_argument("--dry-run", action="store_true")
    _add_selection_args(p)
    p.set_defaults(func=cmd_matrix)

    p = sub.add_parser("summarize", help="recompute summary.json for run(s)")
    p.add_argument("runs", nargs="+", help="run folder, name substring, or 'latest'")
    p.add_argument("--refresh-anchors", action="store_true", help="re-read anchors from data/questions.jsonl")
    p.set_defaults(func=cmd_summarize)

    p = sub.add_parser("compare", help="compare runs (first = baseline)")
    p.add_argument("runs", nargs="+")
    p.set_defaults(func=cmd_compare)

    p = sub.add_parser("review", help="manual review sheet")
    p.add_argument("action", choices=["export", "score"])
    p.add_argument("run")
    p.add_argument("--top-k", type=int, default=5)
    p.add_argument("--force", action="store_true", help="overwrite a sheet that has labels")
    p.set_defaults(func=cmd_review)

    p = sub.add_parser("report", help="leaderboard of all runs -> outputs/report.md")
    p.set_defaults(func=cmd_report)

    p = sub.add_parser("providers", help="list available providers")
    p.set_defaults(func=cmd_providers)

    args = ap.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
