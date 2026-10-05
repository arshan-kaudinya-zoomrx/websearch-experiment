# wsx: web-search experiment harness

This CLI runs the questions in `data/Web_Questions.csv` (64 pharma/biotech CI objectives, 210 sub-queries) against a search API. It saves every request and result as JSON, scores runs automatically, exports a manual review sheet, and compares runs.

Scope: this covers **only the web-search step** of the pipeline (`Perplexity Search` → Jev filter → Luna). There's no answer generation. The **Jev filter** (TypeSafe's model, which reranks the fetched links, keeps the best and abstains if none qualify) is replayed over saved runs, so it measures Jev's time and selection quality without new search calls. Perplexity Search is the first provider; others plug in with one file each (see [docs/ADDING_PROVIDERS.md](docs/ADDING_PROVIDERS.md)).

## Setup
```bash
uv sync                       # Python >=3.11; creates .venv
cp .env.example .env          # then set PERPLEXITY_API_KEY (and TYPESAFE_API_KEY for Jev)
```
On OneDrive, `uv` may warn about hardlinks. Running `set UV_LINK_MODE=copy` (or `export UV_LINK_MODE=copy` in Git Bash) silences it.

## Quickstart
```bash
uv run wsx query "SOR102 safety adverse events"         # one search, readable output, saved to outputs/queries/
uv run wsx prepare --show                               # CSV -> data/questions.jsonl, print anchors
uv run wsx run -c pplx_web_default --rows 1-5 --dry-run # plan + cost, no API calls
uv run wsx run -c pplx_web_default --rows 1-5           # real run -> outputs/runs/<run_id>/
uv run wsx matrix -c pplx_web_default -c pplx_fast --modes queries,objective,batch   # grid + compare + report
uv run wsx filter 175621 --dry-run                      # Jev over a saved run: links, tokens, cost, no calls
uv run wsx filter 175621                                # Jev over a saved run -> outputs/filters/<id>/ (no search calls)
uv run wsx rescore latest --set select.keep_threshold=0.7   # new threshold on stored scores, free
uv run wsx query "SOR102 safety" --jev --anchor SOR102  # one live search + Jev, with the timing split
```

## Commands
| command | what it does |
|---|---|
| `query "text" [opts]` | Run **one** search and print readable results (rank, title, domain, source category, date, URL, snippet). Saves `outputs/queries/<ts>__<provider>-<config>__<query>.{json,md}`. Opts: `-c CFG` (default `pplx_web_default`), `--set params.search_type=fast`, `--anchor SOR102` (flags results that mention the term), `--row q005` (that row's queries as one batch, plus its anchors), `--row q005 --objective` (search the objective text), `--json`, `--jev [CFG]` (then filter with Jev: links in Jev order with score and KEPT/dropped, plus a `search ms + jev ms = total` line; objective = the query or the `--row` objective, overridable with `--objective-text`), `--jev-set k=v`. Several quoted strings make one multi-query request. |
| `filter RUN… [-c CFG] [--set k=v] [--rows …] [--dry-run]` | Run the Jev filter (default config `jev_default`) over the **saved** links of each run. Scores every link against the row's objective, keeps those ≥ `select.keep_threshold` (max `select.max_keep`), or abstains. Writes `outputs/filters/<ts>__jev-<cfg>__on__<run_id>/`. Makes no search calls; Jev costs about $0.01–0.04 per run. |
| `rescore FILTER… --set select.keep_threshold=0.7` | Re-apply the selection to stored Jev scores. It's free and writes a new filter folder, for threshold sweeps. `FILTER` can be a path, a substring, or `latest`. |
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

Jev filter configs:
- `jev_default` (v1): one yes/no question per link, kept if the score is ≥ `select.keep_threshold`.
- `jev_v2` (recommended): two separate questions per link. `on_target` (yes/no) asks whether the link is about this asset, not a name collision. `evidence` is a 4-level scale from "nothing" to "states the requested facts". Both are applied as `select.gates` in code, and the state includes a `target` built from the anchors. For competitor objectives, the target becomes the asset's competitors.
- `jev_per_list`: v1, but with one call per list.

Fields:
- `granularity`: `per_link` makes one Jev call per link, all in parallel; `per_list` makes one call per list.
- `question` (v1) or `questions` (v2): what Jev is asked about each link. Quote `"true"`/`"false"` criteria keys; bare `true:` is a YAML boolean.
- `select.gates` (v2): the minimum answer per question. Every dropped link records a `reason`: `low_<question>`, `below_threshold`, `max_keep` or `error`.
- `max_snippet_chars`, `select.keep_threshold` / `select.max_keep`, `run.link_concurrency`, `pricing.per_1m_input_tokens`.

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
  queries/<ts>__<provider>-<config>__<query-slug>.{json,md}   single ad-hoc searches (wsx query)
  filters/<ts>__jev-<config>__on__<run_id>/
    filter.json     Jev config, source run id + dataset sha, timings
    results.jsonl   one object per link list (schema below)
    summary.json    timing without/with Jev, selection (+ drop reasons), quality before→after, cost
    inspect.md      every link per objective: kept, or dropped and why, with Jev's answers
  comparisons/<ts>__<runA>__vs__<runB>.{json,md}
  report.{md,json}  leaderboard of all runs + Jev filters
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

Each line of a filter's `results.jsonl` (`results` holds every link in Jev order):
```json
{"case_id": "q001-1", "row_id": "q001", "objective": "...", "query": "...", "anchors": ["Tamuzimod"],
 "search_latency_ms": 1344.2, "jev_latency_ms": 412.7, "total_ms": 1756.9,
 "ok": true, "error": null, "calls": 10, "attempts": 10, "usage": {"input_tokens": 3980, "output_tokens": 20},
 "cost_usd": 0.000167, "n_candidates": 10, "n_kept": 3, "abstain": false, "top_score": 0.97,
 "results": [{"orig_rank": 4, "jev_rank": 1, "jev_score": 0.97, "kept": true, "title": "...", "url": "..."}]}
```

## Docs
- [docs/METHODOLOGY.md](docs/METHODOLOGY.md): what each metric means, and the caveats.
- [docs/RESEARCH.md](docs/RESEARCH.md): the full research summary, with dates, numbers and the recommendation.
- [docs/FINDINGS.md](docs/FINDINGS.md): a short log of experiments and conclusions.
- [docs/ADDING_PROVIDERS.md](docs/ADDING_PROVIDERS.md): how to add Linkup, Brave, Tavily, Parallel and others.

## Tests
`uv run pytest`: offline tests, including an end-to-end run against a mocked API.
