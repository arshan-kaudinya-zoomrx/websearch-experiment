# Web-search + Jev research summary

Scope: the **web-search fallback** of the pipeline only: question → registry / vector RAG → (low confidence) **Perplexity Search → Jev filter** → Luna. There's no answer generation here.
Harness: `wsx` CLI (this repo). Raw data is in `outputs/`, and metric definitions are in `docs/METHODOLOGY.md`.

## 1. Initial research (2026-10-02; refer: `images/`)
This research chose the search provider and the pipeline shape. The harness work below tests those choices on our own questions.

**1a. Provider benchmark:** accuracy vs search latency on a **300-question company-news factual lookup** (`images/Image.jpg`), with list prices and decisions (`images/Image (2).jpg`).

| option | accuracy | search latency | $ / 1K searches | decision |
|---|---|---|---|---|
| **Perplexity Search (standard)** | **97.3%** | 1.4s | $5 | **Start here** |
| Linkup (fast) | 96.7% | 1.2s | $5 | Backup |
| Brave (LLM Context) | 94.0% | **0.6s** | $5 | Backup |
| Parallel Basic | ≈93% | ≈1.7s | – | – (chart only) |
| Tavily (basic / advanced) | 87.7% / 93.0% | 1.9s / 4.3s | $8 / $16 | Dropped: slower and pricier for no gain |
| Parallel Search (fast), the setup in use then | 86.0% | 0.9s | $1 | Cheapest, least accurate |
| Parallel Turbo | ≈71% | ≈0.35s | – | – (chart only) |
| Deep-research APIs (Parallel Task, FindAll) | n/a | 5s to 1h | $5+ | Dropped: too slow for a live answer |


**1b. Target pipeline** (`images/Image (1).jpg`):
1. **NCT ID in the question** → Registry API (ClinicalTrials.gov) → Luna.
2. Otherwise **vector retrieval** (existing RAG index) → **Jev check, "answerable from vector?" (~0.2–0.3s)** → yes → Luna.
3. No / low confidence → **Perplexity Search (standard, ~1.4s)** → **Jev: filter web results** (rerank; abstain if no evidence) → Luna.
4. Luna streams the answer from the registry, vector or filtered web results, and marks it *partial* when evidence is incomplete.

This repo covers step 3 only.

**1c. How our measurements compare with the initial research:**
| claim (initial research) | our measurement on the 64 CI objectives | note |
|---|---|---|
| Perplexity standard: 1.4s | web: p50 **2.2–2.7s**, p95 **9–19s**; fast: p50 **0.55s**, p95 1.1s (batch) | Standard is about 2× slower than claimed at the median and has a long tail. Only `fast` meets the latency budget. |
| Perplexity: 97.3% accuracy | 86% of objectives get ≥1 link naming the asset (queries mode); 52% using the objective text as the query | Not the same metric: niche pharma assets vs company news. Accuracy was not human-labelled yet. |
| `fast` vs standard | same coverage (86%), 0.65 URL overlap, 5× cheaper | `fast` wasn't in the original benchmark. |
| Jev check ~0.2–0.3s | Jev **web filter**: p50 0.37s / p95 0.51s for about 10 links in parallel | The diagram's number is for the vector check; the filter scores 10 links, so it's slightly slower. |
| Jev filter: rerank, abstain if no evidence | v2 keeps about 3 of 10 links, asset precision 46%→93%, abstains on 12–18% of lists | Works as designed once the prompt was fixed (section 4). |

## 2. Setup
| item | value |
|---|---|
| Dataset | `data/Web_Questions.csv`: 64 pharma/biotech CI objectives (`q001–q064`) and 210 pre-written sub-queries (1–5 per objective) |
| Objective types | 22 competitor-class ("competing agents…"), 8 approval/launch year, about 22 in-vivo efficacy (TGI, PDAC/HNSCC), plus safety, sponsor/stage, trial design |
| Search API | Perplexity Search API (`POST /search`), `max_results=10`; `web` ($5/1K) vs `fast` ($1/1K) |
| Filter | Jev (TypeSafe System One, `jev-latest` = jev-1.13.0), $0.042 per 1M input tokens, output free |
| Relevance proxy | **Anchor hit**: the asset name appears in title/URL/snippet. There is no human labelling yet (`review.csv` sheets exist). |

## 3. Search baseline: 2026-10-03, all 64 rows
| config | mode | requests | p50 ms | p95 ms | hit@1 | coverage* | unique domains | ≤12 mo old | cost $ |
|---|---|---|---|---|---|---|---|---|---|
| web | queries (1 req/sub-query) | 210 | 2,660 | 19,287 | 67% | **86%** | 547 | 56% | 1.05 |
| web | objective (objective text as query) | 64 | 2,330 | 16,232 | 38% | 52% | 173 | 48% | 0.32 |
| web | batch (≤5 sub-queries in 1 req) | 64 | 2,241 | 8,948 | 70% | 80% | 268 | 61% | 0.32 |
| fast | queries | 210 | 2,059 | 18,063 | 64% | **86%** | 551 | 54% | 0.21 |
| fast | objective | 64 | **547** | 2,393 | 39% | 52% | 170 | 47% | 0.064 |
| fast | batch | 64 | **554** | **1,139** | 67% | 80% | 258 | 60% | **0.064** |

\*Coverage = objectives with ≥1 anchor-hit link. Error rate was 0% and zero-result rate 0% in every run.

Findings:
- **The objective text as the query is poor:** coverage is 52% vs 86%, and 23 objectives are lost against the queries mode. Use the pre-written sub-queries.
- **Batch is 3.3× fewer requests than queries** and loses only 4 objectives (86%→80%: q036, q043, q046, q056 on web).
- **fast ≈ web in quality:** queries coverage is identical (86%), URL overlap is 0.65, and it's 5× cheaper.
- **Latency is much worse than the vendor's 1.4s.** Web p50 is 2.2–2.7s and p95 9–19s. A single ad-hoc query (SOR102) took 14.0s. **fast + batch is the only setup near the reference: p50 0.55s, p95 1.1s.**
- **Source mix:** literature is 28–54%, registries only about 2%, company/press 1–2%. About half the links are uncategorised ("other").
- 9 objectives get no anchor hit in queries mode, and 31 in objective mode.

## 4. Jev filter: 2026-10-04, on the saved web/queries links (210 lists, 2,084 links, no new search calls)
**What Jev does:** it scores each link in parallel, one call per link. Code then keeps the links that pass, up to `max_keep` (5), ranked; if none pass, Jev abstains (Luna gets "no web evidence"). It doesn't fetch pages or write answers; it only filters what Perplexity returned.

| version | prompt | keep rule |
|---|---|---|
| v1 `jev_default` | 1 yes/no: "does this result help answer the objective?" | score ≥ 0.5 |
| v2 `jev_v2` | `on_target` (yes/no: is it about the asset, not a lookalike name) + `evidence` (4 levels: nothing / background / partial facts incl. development stage / requested facts). Competitor objectives get target = "drugs competing with X". | on_target ≥ 0.6, evidence ≥ 0.5 |

Results (anchor metrics on the **42 non-competitor objectives**; competitor objectives are excluded because good links name rival drugs):

| metric | no Jev | v1 | v2 (on_target ≥0.5) | **v2 (≥0.6, default)** |
|---|---|---|---|---|
| Jev latency p50 / p95 | – | 369 / 489 ms | 372 / 515 ms | 372 / 515 ms |
| Total latency p50 (search + Jev) | 2,660 ms | 3,017 ms | 3,004 ms | 3,004 ms |
| Links passed per search | 9.9 | 3.2 | 3.3 | 3.2 |
| Links mentioning the asset (precision) | 46% | 70% | 90% | **93%** |
| First link mentions the asset (hit@1) | 63% | 56% | 74% | **74%** |
| Objectives covered | 88% | 64% | 81% | **81%** |
| Abstained although asset links existed | – | 14% | 0.7% | 1.5% |
| Passed links but none mention the asset | – | 9% | 5.2% | **2.2%** |
| Jev cost (210 searches) | – | $0.073 | $0.095 | (rescored offline, $0) |

Findings:
- **Jev adds about 0.37s (p50) / 0.5s (p95)**, about 12% of total time, steady across runs. It costs **about $0.45 per 1K searches** (vs $1–5 per 1K for search). Search latency, not Jev, is the bottleneck.
- **v1 wasn't useful:** it lost 10 objectives. Development stage ("preclinical") was treated as no evidence for approval-year questions, and on-asset partial evidence scored about 0.1. A config bug also meant its true/false criteria weren't sent: YAML read `true:` as a boolean, so Jev got "It does."/"It does not.". Fixed and covered by a test.
- **v2 is useful:** precision went 46%→93% and hit@1 63%→74%. The 3 objectives it loses are all correct drops: q016 (empty Patsnap page), q033 (DXP-007 = a James Bond card game), q056 (MNPS = nanoparticles). v1's misses are recovered: BM-013, CNP200137 and Compound 18l "preclinical" pages, an ONC201 PDAC paper, and Korean HM100714 sources.
- On competitor objectives, v2 abstained on 4 of 75 lists and kept 3.8 rival-drug links per list.
- **Gate sweep (offline):** on_target 0.6 is best. 0.5 lets generic pages through; 0.7 doubles false abstains for no gain. Lowering v1's cut-off doesn't fix v1 (≥0.2 gives 74% coverage).
- **`max_keep` is a context trade-off:** with 5, 61% of asset links are kept; with 10, 88% are kept and precision stays at 95%.

## 5. Recommendation so far
1. Search: **Perplexity `fast` + batch** (all sub-queries in one request): p50 0.55s, p95 1.1s, $1/1K. It costs about 4 objectives of coverage (86%→80%) versus one request per sub-query.
2. Filter: **Jev v2** (`configs/jev_v2.yaml`): about +0.4s, precision about 93%, a reliable abstain signal. Set `max_keep` to fit Luna's context.
3. Expected end-to-end web fallback: about **1.0s p50** (0.55 + 0.4). That needs a Jev run on the fast/batch links (about $0.02, not yet run).

## 6. Spend
| date | what | $ |
|---|---|---|
| 2026-10-03 | 6 baseline runs (684 requests) | 2.03 |
| 2026-10-03 | Partial web/queries run, stopped (62 requests; ignore `outputs/runs/20261003-183324…`) | ≈0.31 |
| 2026-10-03 | 1 ad-hoc query | 0.005 |
| 2026-10-04 | Jev v1 + v2 (one v2 attempt failed with a 401, $0; runs now abort on an auth error) | 0.17 |
| | **Total** | **≈2.51** |


## Where the data is
`outputs/runs/` (search runs) · `outputs/filters/` (Jev runs; `inspect.md` lists every link kept or dropped, with reasons) · `outputs/report.md` (leaderboard) · `outputs/comparisons/` · `docs/FINDINGS.md` (log)
