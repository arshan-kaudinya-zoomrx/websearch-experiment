# wsx: web-search experiment harness

This CLI runs the questions in `data/Web_Questions.csv` (64 pharma/biotech CI objectives, 210 sub-queries) against a search API. It saves every request and result as JSON, scores runs automatically, exports a manual review sheet, and compares runs.

Scope: this covers **only the web-search step** of the pipeline (`Perplexity Search` → Jev filter → Luna). There's no answer generation. Perplexity Search is the first provider; others plug in with one file each (see [docs/ADDING_PROVIDERS.md](docs/ADDING_PROVIDERS.md)).

## Setup
```bash
uv sync                       # Python >=3.11; creates .venv
cp .env.example .env          # then set PERPLEXITY_API_KEY
```
On OneDrive, `uv` may warn about hardlinks. Running `set UV_LINK_MODE=copy` (or `export UV_LINK_MODE=copy` in Git Bash) silences it.

## Quickstart
```bash
uv run wsx prepare --show                               # CSV -> data/questions.jsonl, print anchors
uv run wsx run -c pplx_web_default --rows 1-5 --dry-run # plan + cost, no API calls
uv run wsx run -c pplx_web_default --rows 1-5           # real run -> outputs/runs/<run_id>/
uv run wsx matrix -c pplx_web_default -c pplx_fast --modes queries,objective,batch   # grid + compare + report
```

## Commands
| command | what it does |
|---|---|
| `prepare [--show]` | Parse the CSV into `data/questions.jsonl` with ids `q001…q064` and anchor terms. Run it again after editing `data/anchor_overrides.yaml`. |
| `run -c CFG [opts]` | Run one config. Opts: `--mode queries\|objective\|batch`, `--rows 1-10\|q003,q017`, `--sample N --seed S`, `--repeat N`, `--concurrency N`, `--set key.path=value` (repeatable), `--name`, `--dry-run`. |
| `matrix -c A -c B [--modes …]` | Run every config × mode, then compare all of them and rebuild the report. Takes the same opts as `run`. |
| `summarize RUN… [--refresh-anchors]` | Recompute `summary.json`. With `--refresh-anchors`, rescore using updated anchors. |
| `compare RUN RUN…` | Compare runs side by side; the first one is the baseline. Writes `outputs/comparisons/`. |
| `review export RUN [--top-k 5] [--force]` | (Re)write `review.csv` for manual labelling. |
| `review score RUN` | Score a labelled `review.csv` and write the results into `summary.json["review"]`. |
| `report` | Build a leaderboard of all runs in `outputs/report.md` and `outputs/report.json`. |
| `providers` | List the registered providers. |

`RUN` can be a path, any unique substring of a run folder name, or `latest`.

## Modes (the unit of a test case)
| mode | one request = | case id |
|---|---|---|
| `queries` | one pre-written sub-query from the CSV | `q001-1`, `q001-2`, … |
| `objective` | the full Objective text as the query | `q001-obj` |
| `batch` | all of a row's sub-queries in one multi-query request (≤5, billed as 1) | `q001-batch` |

## Configs (`configs/*.yaml`)
`pplx_web_default.yaml` documents every field. Other configs use `extends:` and override only what changes. Shipped variants: `pplx_fast`, `pplx_maxres20`, `pplx_ctx_low`, `pplx_recent_year`, `pplx_domains_biomed`. The fields are:
- `params`: sent to the API as-is. Null or empty values are dropped.
- `selection`: which rows to run.
- `run`: concurrency, timeout, retries, repeat, `max_cost_usd` guard, `save_raw`, `review_top_k`.
- `pricing`: USD per 1K requests, by tier.

Any key can be overridden ad hoc: `--set params.max_results=20 --set run.concurrency=8`.

Other editable inputs:
- `data/anchor_overrides.yaml`: corrects the asset-name anchors used for scoring.
- `configs/domain_categories.yaml`: maps domains to source categories.

## Outputs
```
outputs/
  runs/<YYYYMMDD-HHMMSS>__<provider>-<config>__<mode>/
    run.json        resolved config, CLI args, dataset sha256 + row ids, timings, env
    results.jsonl   one JSON object per request (schema below)
    summary.json    run metrics (+ "review" once scored)
    review.csv      top-k results per request for manual labelling
  comparisons/<ts>__<runA>__vs__<runB>.{json,md}
  report.{md,json}  leaderboard of all runs
```
Each line of `results.jsonl` has this shape:
```json
{"case_id": "q001-1", "row_id": "q001", "mode": "queries", "repeat": 0, "provider": "perplexity",
 "query": "...", "objective": "...", "anchors": ["Tamuzimod"],
 "request": {"query": "...", "search_type": "web", "max_results": 10},
 "ok": true, "status": 200, "error": null, "attempts": 1, "latency_ms": 1380.2, "n_results": 10,
 "results": [{"rank": 1, "query_index": null, "title": "...", "url": "...", "domain": "...",
              "snippet": "...", "date": "2025-10-01", "last_updated": null}],
 "raw": {"id": "...", "server_time": null}, "ts": "2026-10-03T10:15:00+00:00"}
```

## Docs
- [docs/METHODOLOGY.md](docs/METHODOLOGY.md): what each metric means, and the caveats.
- [docs/FINDINGS.md](docs/FINDINGS.md): a short log of experiments and conclusions.
- [docs/ADDING_PROVIDERS.md](docs/ADDING_PROVIDERS.md): how to add Linkup, Brave, Tavily, Parallel and others.

## Tests
`uv run pytest`: offline tests, including an end-to-end run against a mocked API.
