# Methodology

## Question
How well does the web-search step retrieve evidence for our CI questions? We look at latency, cost and relevance, and at how each one shifts with configuration and provider. Reference point: the vendor benchmark had Perplexity Search (standard) at **97.3% / 1.4s / $5 per 1K**, on generic company-news lookups. Our questions are niche: preclinical codes, conference abstracts, and Chinese biotech assets.

## Dataset
`data/Web_Questions.csv` → `data/questions.jsonl`: 64 rows (`q001…q064`) and 210 sub-queries. Each row has an **objective** (the information need) and 1–5 pre-written **queries**. There is no ground-truth answer.

## Automatic metrics (`summary.json`)
| metric | definition |
|---|---|
| `latency_ms.p50/p90/p95/max/mean` | Client-side wall time of the successful HTTP call, including network. `repeat_sd_mean` is the mean per-case std dev when `repeat>1`. |
| `error_rate` | Share of requests that failed after retries. Retries cover 429, 5xx and timeouts, with exponential backoff. |
| `zero_result_rate` | Share of successful requests that returned no results. |
| `results_per_request_mean`, `snippet_chars_mean` | Payload volume. |
| `anchor.hit_at_1/3/k` | Share of requests with ≥1 result at rank ≤ k that mentions the row's **anchor** (the asset name) in its title, URL or snippet. Matching ignores case and punctuation, so "SOR-102" = "SOR102". |
| `anchor.hit_fraction_mean` | Mean share of a request's results that hit the anchor. This is a precision proxy. |
| `objective_coverage` | Share of rows where **any** request hit the anchor. Comparable across modes. |
| `rows_without_hit` | Rows with no anchor hit at all. These are the first ones to inspect. |
| `source_mix` | Share of results per source category (registry, literature, regulatory, company_press, trade_news, databases, other), from `configs/domain_categories.yaml`. |
| `freshness` | Share of results with a date, their median age in days, and the share dated within 12 months. |
| `cost_usd` | Successful requests × list price for the tier (web $5/1K, fast $1/1K). A multi-query batch request counts as 1. |

**Anchor caveat:** an anchor hit means a result is *about the asset*. It does not mean the result *answers the objective* (for example, TGI numbers for a specific model). The proxy is good for spotting retrieval failures (no page about the asset at all), and weak for judging answer quality. The manual review measures how well the two agree.

## Manual review (`review.csv`)
The sheet holds the top-k results per request (default k=5, repeat 0). Reviewers fill in:
- `relevant` = Y/N: is the result about this asset *and* useful for the objective?
- `answers_objective` = Y: does this result alone answer the objective? Mark it on any one row of that objective.

`wsx review score` reports:
- `precision`: the share of labelled results marked relevant. This is the closest analogue to the vendor "accuracy".
- `any_relevant_rate`: the share of requests with ≥1 relevant result in the top k.
- `objective_answerable_rate`
- `anchor_proxy_vs_human`: agreement, precision and recall of the proxy against human labels.

Partial labelling is fine; blank cells are ignored. The anchor proxy is left out of the sheet on purpose, so reviewers aren't biased by it.

## Comparisons
`wsx compare` puts the metric tables side by side and adds row-level analysis against the baseline:
- **URL Jaccard**: how much the result sets overlap.
- **Coverage wins/losses**: rows where only one run found the asset.

## Rules for fair comparisons
- Compare runs over the same rows (`run.json → dataset.row_ids`) and the same dataset hash.
- For latency, use `--repeat 3` and the same concurrency. Run providers back to back, not hours apart.
- Search indexes change over time, so date every finding (`run.json → started_at`).
