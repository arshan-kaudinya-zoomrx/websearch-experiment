# Web-search + Jev research summary

Scope: the **web-search fallback** of the pipeline: question → registry / vector RAG → (low confidence) **web search → Jev filter → Luna**. Luna answers are generated from saved links with the production prompt (section 5).

**TL;DR (2026-10-07):**
- Use **Perplexity `fast`** with every sub-query in one request: p50 0.55s, $1 per 1K rows. It gave the best Luna answers of the 4 setups tested (§5).
- **Jev** cleans the links (asset precision 44%→93%) but doesn't improve Luna's answers on Perplexity. It's optional, as a +0.4s early "no evidence" exit (§5).
- **End-to-end time is Luna's** (p50 ≈13s). Luna needs `max_completion_tokens` ≥16K (§5).
- Migrating from Parallel costs the same at 10 results. Watch the fixed 50 queries/s limit (§8).

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
| Objective types | 22 competitor-class ("competing agents…"), about 8 approval/launch year, about 22 in-vivo efficacy (TGI, PDAC/HNSCC), plus safety, sponsor/stage, trial design |
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
- **Jev adds about 0.37s (p50) / 0.5s (p95)**, about 12% of total time, steady across runs. It costs **about $0.45 per 1K searches** (≈$0.41 on the fast/batch lists) (vs $1–5 per 1K for search). Search latency, not Jev, is the bottleneck.
- **v1 wasn't useful:** it lost 10 objectives. Development stage ("preclinical") was treated as no evidence for approval-year questions, and on-asset partial evidence scored about 0.1. A config bug also meant its true/false criteria weren't sent: YAML read `true:` as a boolean, so Jev got "It does."/"It does not.". Fixed and covered by a test.
- **v2 is useful:** precision went 46%→93% and hit@1 63%→74%. The 3 objectives it loses are all correct drops: q016 (empty Patsnap page), q033 (DXP-007 = a James Bond card game), q056 (MNPS = nanoparticles). v1's misses are recovered: BM-013, CNP200137 and Compound 18l "preclinical" pages, an ONC201 PDAC paper, and Korean HM100714 sources.
- On competitor objectives, v2 abstained on 4 of 75 lists and kept 3.8 rival-drug links per list.
- **Gate sweep (offline):** on_target 0.6 is best. 0.5 lets generic pages through; 0.7 doubles false abstains for no gain. Lowering v1's cut-off doesn't fix v1 (≥0.2 gives 74% coverage).
- **`max_keep` is a context trade-off:** with 5, 61% of asset links are kept; with 10, 88% are kept and precision stays at 95% (measured at on_target ≥0.7).

## 5. Luna answers: 2026-10-06, 4 arms × 64 rows
**Question:** does Jev make Luna's final answers better? Luna = `gpt-6-luna` with the production prompt (`data/prompts.py`, enrich-v8, unchanged), up to 10 links as `[E1]..`, output cap 16K tokens. The judge is the same model, blind (shuffled, unlabelled answers, union of all arms' evidence).

| arm | search | filter |
|---|---|---|
| A | Perplexity `fast`, batch (`181326`) | none (10 links) |
| B | Parallel `fast`, batch (`174729`, new) | none (10 links) |
| C | Perplexity `fast`, batch | Jev v2, max 10 kept (`174803`) |
| D | Parallel `fast`, batch | Jev v2, max 10 kept (`174818`) |

**Links (anchor proxy, 42 non-competitor objectives):**

| | Perplexity | Perplexity + Jev | Parallel | Parallel + Jev |
|---|---|---|---|---|
| Search p50 / p95 | 0.55 / 1.1s | | 1.06 / 1.6s | |
| Links naming the asset | 44% | 93% | 33% | 82% |
| First link names it (hit@1) | 67% | 76% | 29% | 64% |
| Objectives covered | 79% | 76% | 86% | 74% |

**Answers (all 64 rows; judge 1-5 on 62 rows):**

| | A Perplexity | C Perplexity + Jev | B Parallel | D Parallel + Jev |
|---|---|---|---|---|
| Answered | 61% | **66%** | 63% | 56% |
| Jev abstained (Luna not called) | – | 14% | – | 12.5% |
| Names/numbers not in evidence | 2.8% | 2.4% | 2.4% | 2.1% |
| Input tokens per Luna call | 9.6K | 8.1K | 10.8K | 8.3K |
| Luna p50 when called | 12.4s | 21.5s | 17.0s | 14.9s |
| Total p50 / p95 | 13.1 / 57s | 17.5 / 56s | 18.1 / 60s | 11.6 / 49s |
| Judge: correct | **4.65** | 4.63 | 4.40 | 4.47 |
| Judge: complete | **3.68** | 3.63 | 3.11 | 3.16 |
| Judge: right subject | 4.44 | 4.40 | 4.15 | 4.44 |
| Judge: useful | **3.48** | 3.42 | 2.98 | 3.23 |

**Jev, paired per row (judge "useful"):**

| | Jev better | worse | tie | mean | sign test p |
|---|---|---|---|---|---|
| on Perplexity | 18 | 22 | 22 | -0.06 | 0.64 |
| on Parallel | 21 | 12 | 29 | **+0.24** | 0.16 |
| Parallel, "right subject" only | 16 | 4 | 42 | +0.29 | **0.01** |
| Parallel, competitor rows (n=22) | | | | +0.64 | |
| Parallel, other rows (n=40) | | | | +0.03 | |

Findings:
- **Best arm is plain Perplexity `fast` (A).** It leads on correct, complete and useful. Parallel without Jev is worst (useful 2.98).
- **Jev does not improve Perplexity answers** (useful -0.06, p=0.64). Luna's prompt already discards off-subject items, so cleaning Perplexity's mostly on-topic list adds nothing. It did turn 3 "no" rows into answers (q002, q015, q019) and lost none.
- **Jev helps Parallel, mostly by keeping Luna on the right drug** (subject +0.29, p=0.01), almost all of it on competitor objectives (+0.64). Parallel + Jev still trails plain Perplexity (3.23 vs 3.48).
- **Jev's abstains are reliable on Perplexity:** all 9 rows it abstained on were rows where Luna, given all 10 links, also answered "no". On Parallel, 6 of 8 were; the other 2 (q040 GUT-1, q041 DB-3Q) were a target bug: for competitor objectives v2 asked about "drugs competing with X" and rejected pages about X itself, which the positioning contract needs. Fixed in **Jev v3** (`configs/jev_v3.yaml`, target "X itself, or drugs competing with X"): on Parallel, 0 competitor abstains (was 2) and 6.8 links kept per competitor list (was 4.4); on Perplexity, 8 abstains (12.5%, all among v2's 9) and 7.6 links per competitor list. Other objectives barely change (Parallel: one abstain fewer, q032), but Jev p95 rose to 1.37s on that run. Not yet run through Luna.
- **Latency is Luna's, not search or Jev.** Luna takes 2–70s (p95 48–59s), set by how much it writes (median 1-2K output tokens, max 6.8K). Jev's 0.4s is 1-3% of total. Jev trims only 16-23% of input tokens, because the ~6K-token system prompt dominates. With a 4K output cap, 3/19 calls returned nothing (all reasoning, no JSON); 16K fixed it.
- **The differences are small.** All pairwise win rates are 45-55%. The judge picked the same winner in 7 of 10 rows when the answer order was reversed (rank ρ 0.84). Luna runs without a seed and is not deterministic (q002 answered in the 5-row trial, not in the full run). Only the Parallel "right subject" gain is clearly beyond noise.

## 6. Recommendation (updated 2026-10-06)
1. Search: **Perplexity `fast` + batch.** It gives the best Luna answers, at p50 0.55s and $1/1K. Parallel `fast` is slower (p50 1.06s) and its answers are worse, with or without Jev.
2. Jev: **not needed for answer quality on Perplexity.** Keep it only for an early "no web evidence" exit (12.5–14% of rows, all correct here), which skips a Luna call. If Parallel is used, use Jev v3.
3. Luna: set `max_completion_tokens` well above 4K. End-to-end latency is Luna's (p50 about 13s, p95 about 57s), so that is where to optimise, not search or Jev.
4. Next: a human spot-check of the judge (`outputs/judge/20261006-183425…/human_review.csv`, 16 rows). Luna on Jev v3 competitor rows (22 rows × 2).

## 7. Spend
| date | what | $ |
|---|---|---|
| 2026-10-03 | 6 baseline runs (676 requests) | 2.03 |
| 2026-10-03 | Partial web/queries run, stopped (62 requests; ignore `outputs/runs/20261003-183324…`) | ≈0.31 |
| 2026-10-03 | 1 ad-hoc query | 0.005 |
| 2026-10-04 | Jev v1 + v2 (one v2 attempt failed with a 401, $0; runs now abort on an auth error) | 0.17 |
| 2026-10-06 | Parallel `fast` search, 64 requests | 0.064 |
| 2026-10-06 | Jev v2 k10 + v3 on Perplexity fast and Parallel (4 × 640 links) | 0.11 |
| 2026-10-06 | OpenAI `gpt-6-luna`: Luna (5-row trial 20 rows, full 4 × 64 = 239 calls + 12 retries) and judge (74 calls, ≈0.6M input tokens) | not priced (set `llm.pricing`) |
| | **Total (search + Jev)** | **≈2.68** |


## Where the data is
`outputs/runs/` (search runs) · `outputs/filters/` (Jev runs; `inspect.md` lists every link kept or dropped, with reasons) · `outputs/synth/` (Luna answers; `answers.md` per arm) · `outputs/judge/` (`compare.md`, `human_review.csv`) · `outputs/report.md` (leaderboard) · `outputs/comparisons/` · `docs/FINDINGS.md` (log)

## 8. Migration: Parallel `fast` → Perplexity `fast`
**What changes:** only the search call. Registry, RAG, Jev and Luna stay. Each fallback row = **1 request** with its sub-queries (≤5) as a `query` array, `search_type: "fast"`, `max_results: 10`.

**Why:** better Luna answers (judge useful 3.48 vs 2.98) and 2× faster search (p50 0.55s vs 1.06s). Search is only ≈5% of end-to-end time; Luna is the rest (§5).

**Billing vs rate limit (Perplexity docs):** a request is **billed once** however many queries it holds, but **each query uses one rate-limit "query unit"**.

| per 1K fallback rows (10 results) | Parallel `fast` (today) | Perplexity `fast` |
|---|---|---|
| Search | $1 | $1 (one billed request per row) |
| Search at 20 results | $11 (+$1 per 1K extra results) | $1 |
| Jev v3, 10 links (optional) | ≈$0.41 | ≈$0.41 |
| Rate limit | 600 requests/min | 50 query units/s ≈ 15 rows/s ≈ 900 rows/min (at our 3.3 sub-queries per row) |

No saving at 10 results. Perplexity bills successful requests only (docs); whether a zero-result response counts as successful isn't stated. Parallel's $5/month free credit goes away.

**Enterprise / plan nuances (Perplexity):**
- The Search API limit (50 units/s, burst 50) is the **same for every account and usage tier**. The docs give no route to raise it; the increase form covers tiers beyond 5, not Search explicitly. If peak traffic may exceed it, ask Perplexity sales before cutover.
- The API is **pay-as-you-go and billed separately** from any Perplexity Enterprise Pro seats; seats don't include API credit (third-party pricing guides; confirm with sales).
- Data: the API "does not retain any query data and does not train on it". Perplexity holds a SOC 2 Type II report (Trust Center). No public SLA; negotiate one if needed.


**Fallback (proposed, not tested):**
1. Timeout (≈3s, about 3× the measured p95), 5xx or 429 → retry once with `Retry-After` → Parallel `fast` + Jev v3. Keep that key and code path.
2. No results or a Jev abstain → Luna gets "no web evidence".
3. A provider feature flag, so the change can be reverted without a deploy.

**Before cutover:**
1. Get two production numbers: peak fallback rows/min and Parallel's current `max_results`.
2. Shadow-run on live traffic. Expected: search p50 ≈0.55s, 0% errors, Jev abstain 12–14%, Luna answer rate 61–66%, no `finish_reason=length`.

**Open risks:** the results come from 64 CI objectives, not production traffic. The judge isn't human-checked yet. Arm gaps are small (win rates 45–55%) and Luna is unseeded. `gpt-6-luna` cost is unpriced. Jev v3 hasn't been run through Luna.
