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

## Jev filter (`wsx filter`, `outputs/filters/*/summary.json`)
Jev (TypeSafe System One, `jev-latest`) is asked the config's questions about every link. Each answer is normalized to 0–1: a yes/no (Noul) answer is a probability, and a Score answer is its expected level divided by the top level.
- **v1 (`jev_default`):** one question, "does this result help answer the objective?". A link is kept if it scores ≥ `keep_threshold`.
- **v2 (`jev_v2`):** `on_target` (is it about this asset, or about a name collision?) and `evidence` (a 4-level scale). A link is kept if every answer is ≥ its `select.gates` value. Links are ranked by on_target × evidence.

Links are deduped by URL (batch records merge several queries). At most `max_keep` are kept. If none pass, Jev **abstains**. Each link records a `reason`, and `inspect.md` lists every link.

**Without Jev** = every fetched link in Perplexity order. **With Jev** = only the kept links, in Jev order.

| metric | definition |
|---|---|
| `timing_ms.search/jev/total` | p50/p95/mean. `search` is **replayed** from the source run's measured latency. `jev` is the measured wall time to score one list (`per_link`: all calls in parallel). `total` = search + jev, per list. |
| `jev_share_of_total_p50` | Jev p50 ÷ total p50. |
| `calls_per_request_mean`, `input_tokens_per_request_mean`, `cost_usd`, `cost_per_1k_requests` | Jev load and cost, from the API's `usage` × $0.042 per 1M input tokens (output tokens are free). |
| `selection.kept_mean / candidates_mean / abstain_rate / score_p10-p90` | How much Jev passes on to Luna, and how its scores are spread. |
| `selection.reasons`, `selection.answer_means` | Why links were dropped (`low_on_target`, `low_evidence`, `below_threshold`, `max_keep`, `error`), and the mean answer per question. |
| `quality.lists_judged / competitor_lists_excluded` | The anchor proxy is computed only on **non-competitor** objectives. For "competing agents …" objectives, good links name *other* drugs, so the asset-name proxy would count correct keeps as misses. |
| `quality.anchor_precision` | Share of links that hit the anchor, over all fetched links vs over kept links. |
| `quality.hit_at_1` | Is the first link an anchor hit: Perplexity's #1 vs Jev's first kept link (abstain counts as a miss). `rerank_only` is Jev's #1 with no threshold applied. |
| `quality.objective_coverage` | Rows with ≥1 anchor hit, among fetched vs among kept links. `rows_lost` lists the rows Jev dropped all anchor hits for. |
| `quality.anchor_recall_retained` | Anchor-hit links kept ÷ anchor-hit links fetched. Low means Jev throws away on-asset pages. |
| `quality.abstain_no_anchor_hits` | Abstained on a list with no anchor hit (proxy: correct abstain). |
| `quality.abstain_with_anchor_hits` | Abstained although on-asset links existed (proxy: possible false abstain; inspect these). |
| `quality.kept_without_anchor_hits` | Passed links on although none mention the asset (proxy: possible false pass). |
| `source_mix.without_jev / with_jev` | Source categories of fetched vs kept links. |

**Caveats.**
- The anchor proxy rewards links that *mention* the asset. Jev is asked a stricter question (does the link *answer* the objective?), so a lower recall on anchor hits can be correct behaviour. Spot-check `abstain_with_anchor_hits` cases.
- `per_link` latency depends on `run.link_concurrency` and on the API's rate limits (80 req/s). With `run.concurrency` > 1, the parallel lists share that budget, so keep it low for latency tests.
- Only `wsx query --jev` measures search + Jev live, end to end, on one query.
- `wsx rescore` changes only the selection. Scores and timings are reused.
- `anchor_recall_retained` is capped by `max_keep`. With about 10 links and `max_keep: 5`, at most about half the anchor links can be kept, so read it alongside `selection.reasons.max_keep`.

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
