# wsx: web-search experiment harness

This CLI runs the questions in `data/Web_Questions.csv` (64 pharma/biotech CI objectives, 210 sub-queries) against a search API. It saves every request and result as JSON, scores runs automatically, exports a manual review sheet, and compares runs.

Scope: the **web-search fallback** of the pipeline (search → Jev filter → Luna). Search providers: Perplexity and Parallel. The **Jev filter** (TypeSafe's model, which reranks the fetched links, keeps the best and abstains if none qualify) is replayed over saved runs, so it measures Jev's time and selection quality without new search calls. Perplexity Search is the first provider; others plug in with one file each (see [docs/ADDING_PROVIDERS.md](docs/ADDING_PROVIDERS.md)). **Luna** answers are generated from saved links with the production prompt (`data/prompts.py`, imported unchanged) and scored by code metrics plus a blind LLM judge, so search × filter arms can be compared on the answer, not only on the links.

## Setup
```bash
uv sync                       # Python >=3.11; creates .venv
cp .env.example .env          # then set the keys you need: PERPLEXITY / PARALLEL / TYPESAFE (Jev) / OPENAI (Luna, judge)
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
uv run wsx synth 20261003-181326 --dry-run              # Luna on saved links: calls, tokens, facet per row, no calls
uv run wsx synth 20261003-181326 --rows 1-5             # Luna answers -> outputs/synth/<id>/ (answers.md)
uv run wsx synth-retry latest                           # re-run rows that hit a rate limit / timeout, same folder
uv run wsx judge <synthA> <synthB> <synthC> <synthD>    # blind judge across arms -> outputs/judge/<id>/compare.md
```

## Commands
| command | what it does |
|---|---|
| `query "text" [opts]` | Run **one** search and print readable results (rank, title, domain, source category, date, URL, snippet). Saves `outputs/queries/<ts>__<provider>-<config>__<query>.{json,md}`. Opts: `-c CFG` (default `pplx_web_default`), `--set params.search_type=fast`, `--anchor SOR102` (flags results that mention the term), `--row q005` (that row's queries as one batch, plus its anchors), `--row q005 --objective` (search the objective text), `--json`, `--jev [CFG]` (then filter with Jev: links in Jev order with score and KEPT/dropped, plus a `search ms + jev ms = total` line; objective = the query or the `--row` objective, overridable with `--objective-text`), `--jev-set k=v`. Several quoted strings make one multi-query request. |
| `filter RUN… [-c CFG] [--set k=v] [--rows …] [--dry-run]` | Run the Jev filter (default config `jev_default`) over the **saved** links of each run. Scores every link against the row's objective, keeps those ≥ `select.keep_threshold` (max `select.max_keep`), or abstains. Writes `outputs/filters/<ts>__jev-<cfg>__on__<run_id>/`. Makes no search calls; Jev costs about $0.03 (64 lists) to $0.10 (210 lists) per run. |
| `rescore FILTER… --set select.keep_threshold=0.7` | Re-apply the selection to stored Jev scores. It's free and writes a new filter folder, for threshold sweeps. `FILTER` can be a path, a substring, or `latest`. |
| `synth SOURCE… [-c luna_openai] [--set k=v] [--rows …] [--dry-run]` | Luna answers from saved links. `SOURCE` is a search run (all links, the no-Jev arm) or a Jev filter folder (kept links; a row where Jev kept nothing is not sent to Luna). One OpenAI call per row with `build_system(facet, scope)` + `build_user(...)` from `data/prompts.py`. Writes `outputs/synth/<ts>__luna-<cfg>__on__<source>/`. The dry run prints the facet chosen for every row. |
| `judge SYNTH… [-c judge_openai] [--set k=v] [--rows …] [--dry-run]` | Blind LLM judge over 2–4 synth folders (arms): per row, the union of the arms' evidence plus the shuffled answers; 1–5 scores (correct, complete, subject, useful) and a ranking. Re-judges the first rows in reversed order (position-bias check) and exports `human_review.csv`. Writes `outputs/judge/<ts>__judge-<cfg>__<n>arms/compare.md`. |
| `synth-retry SYNTH… [--set k=v]` | Re-run only the rows whose Luna call failed (429, timeout, invalid JSON) into the **same** synth folder, so the arm stays complete and paired. Logged in `synth.json → retried`. |
| `judge-score JUDGE…` | Recompute a judge folder's summary; once `human_review.csv` is filled in, adds judge–human agreement. |
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
`pplx_web_default.yaml` documents every field. Other configs use `extends:` and override only what changes. Shipped variants: `pplx_fast`, `pplx_maxres20`, `pplx_ctx_low`, `pplx_recent_year`, `pplx_domains_biomed`. `parallel_fast` (Parallel Search, `mode: fast`, one request per row with the objective + up to 5 queries) is standalone, because Parallel rejects Perplexity's params. The fields are:
- `params`: sent to the API as-is. Null or empty values are dropped.
- `selection`: which rows to run.
- `run`: concurrency, timeout, retries, repeat, `max_cost_usd` guard, `save_raw`, `review_top_k`.
- `pricing`: USD per 1K requests, by tier.

Any key can be overridden ad hoc: `--set params.max_results=20 --set run.concurrency=8`.

Jev filter configs:
- `jev_default` (v1): one yes/no question per link, kept if the score is ≥ `select.keep_threshold`.
- `jev_v2`: two separate questions per link. `on_target` (yes/no) asks whether the link is about this asset, not a name collision. `evidence` is a 4-level scale from "nothing" to "states the requested facts". Both are applied as `select.gates` in code, and the state includes a `target` built from the anchors. For competitor objectives, the target becomes the asset's competitors.
- `jev_per_list`: v1, but with one call per list.
- `jev_v2_k10`: v2 keeping up to 10 links, used to feed Luna.
- `jev_v3` (recommended if Jev is used): v2_k10 with the competitor target widened to "X itself, or drugs competing with X". v2 rejected pages about X on competitor objectives, which Luna's positioning contract needs (RESEARCH §5).

Fields:
- `granularity`: `per_link` makes one Jev call per link, all in parallel; `per_list` makes one call per list.
- `question` (v1) or `questions` (v2): what Jev is asked about each link. Quote `"true"`/`"false"` criteria keys; bare `true:` is a YAML boolean.
- `select.gates` (v2): the minimum answer per question. Every dropped link records a `reason`: `low_<question>`, `below_threshold`, `max_keep` or `error`.
- `max_snippet_chars`, `select.keep_threshold` / `select.max_keep`, `run.link_concurrency`, `pricing.per_1m_input_tokens`.

Luna and judge configs (`luna_openai`, `judge_openai`):
- `llm.model`: Luna = `gpt-6-luna`. The judge's is null, which means it uses the synth folders' model and pricing; override with `--set llm.model=<name>`. Set `llm.pricing` to get $ numbers. `temperature` / `reasoning_effort` are left out of the request when null (Luna runs unseeded, so answers vary between runs).
- `llm.max_completion_tokens: 16000`: at 4000, 3 of 19 calls spent the budget reasoning and returned no JSON. `llm.retries: 5` (the 2026-10-06 arms other than Parallel ran with 2); a 429 waits for `Retry-After`, or at least 10s × attempt.
- Luna: `as_of`, `evidence.max_items` / `max_chars_per_item` (the same cap for every arm), `facets` (objective regex → prompt COLUMN CONTRACT; first match wins).
- Judge: `seed` (answer shuffle), `position_check_rows`, `human_sample`, `max_chars_per_item`.

Other editable inputs:
- `data/anchor_overrides.yaml`: corrects the asset-name anchors used for scoring.
- `configs/domain_categories.yaml`: maps domains to source categories.
- `data/facet_overrides.yaml`: per-row facet/scope when the `facets` patterns pick the wrong contract.

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
  synth/<ts>__luna-<config>__on__<source>/
    synth.json      config, prompt sha256, arm, facet per row
    results.jsonl   per row: evidence [E1].., Luna output, metrics, timing (search/jev/luna), cost
    summary.json    answer metrics (answering, contract, grounding, subject, evidence use, timing, cost)
    answers.md      every answer with its flags and evidence links
  judge/<ts>__judge-<config>__<n>arms/
    compare.md      one row per arm: code metrics + judge scores, rank, win rate, latency, $
    results.jsonl   per row: order shown, judge scores per arm, ranking, position-check rerun
    human_review.csv, human_evidence.md, human_key.json   blind spot-check sheet (open the key only after scoring)
  comparisons/<ts>__<runA>__vs__<runB>.{json,md}
  report.{md,json}  leaderboard of all runs + Jev filters + Luna arms
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
- [docs/ADDING_PROVIDERS.md](docs/ADDING_PROVIDERS.md): how to add Linkup, Brave, Tavily and others.

## Tests
`uv run pytest`: offline tests, including end-to-end search, Jev, Luna and judge runs against mocked APIs.
