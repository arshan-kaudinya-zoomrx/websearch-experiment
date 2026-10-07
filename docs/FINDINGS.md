# Findings

Keep each entry short: what was run, the key numbers, and a one-line takeaway. Raw numbers live in `outputs/report.md` and `outputs/comparisons/`.

## Log
| date | experiment | runs (folder names) | key numbers | takeaway |
|---|---|---|---|---|
| 2026-10-03 | Baseline: Perplexity web vs fast × queries/objective/batch, all 64 rows | `175621`, `180323`, `180530`, `180640`, `181307`, `181326` | Coverage: queries 86%, batch 80%, objective 52%. p50: web 2.2–2.7s; fast+batch 0.55s (p95 1.1s). $2.03 for 676 requests. | **Use `fast` + batch** with the sub-queries. Never the objective text alone. |
| 2026-10-04 | Jev v1 (`jev_default`, per_link, ≥0.5, max 5) on web/queries | `20261004-164721__jev-jev_default__on__20261003-175621…` | Jev p50 369 ms / p95 489 ms (12% of total); kept 3.2 of 9.9 links; abstain 18%; on 42 non-competitor rows: anchor precision 46%→70%, coverage 88%→64%; $0.073 | Fast and cheap, but **the criteria were not sent** (YAML bool-key bug, so Jev got "It does."/"It does not."). It dropped too much: development stage counted as no evidence for approval questions, and partial or on-asset preclinical pages scored about 0.1. It did correctly drop name collisions (DXP-007 = a card game, MNPS = nanoparticles). Lowering the cut-off alone doesn't help (≥0.2 gives 74% coverage) → v2 prompt. |
| 2026-10-04 | Jev v2 (`jev_v2`: on_target noul + 4-level evidence score, gates in code), same links | `20261004-174606__jev-jev_v2__on__…175621…`; offline sweeps `174759/174800/174801` | Jev p50 372 / p95 515 ms (12% of total), $0.095. On 42 non-competitor rows: anchor precision 46%→90% (gates 0.5; 93% at the 0.6 default), hit@1 63%→74%, coverage 88%→81%. The 3 rows lost (q016 empty Patsnap page, q033 DXP-007 card game, q056 MNPS nanoparticles) are all correct drops. 1 false abstain in 135 lists. Competitor rows: abstained on 4 of 75 lists, keeping 3.8 rival-drug links per list. Gate sweep: on_target ≥0.6 is best (pages kept with no asset mention 5.2%→2.2%, false abstains 0.7%→1.5%); ≥0.7 adds nothing. `max_keep` 5→10 raises asset links kept from 61% to 88%. | **Useful.** v2 fixes v1's misses: preclinical status now counts for approval questions, on-asset partial evidence is kept (ONC201, HM100714), and Korean/Chinese sources work. Default is now on_target ≥0.6, evidence ≥0.5. The remaining choice is `max_keep` (how much context Luna gets). |
| 2026-10-06 | Luna answers, 4 arms × 64 rows: Perplexity fast / Parallel fast × no Jev / Jev v2 k10; blind judge (gpt-6-luna) | synth `181920`, `182225`, `182546`, `182855`; judge `20261006-183425…` | Judge useful: Perplexity 3.48, +Jev 3.42, Parallel 2.98, +Jev 3.23. Paired Jev effect: Perplexity -0.06 (p=0.64), Parallel +0.24 (p=0.16; right-subject +0.29, p=0.01; competitor rows +0.64). Jev abstains: 9/9 correct on Perplexity, 6/8 on Parallel (2 = competitor-target bug → v3). Total p50 11.6-18.1s, Luna-dominated; Jev 0.4s. 4K output cap failed 3/19 calls. | **Jev doesn't improve answers on Perplexity; helps Parallel stay on-subject.** Best arm is plain Perplexity fast. Jev's value on Perplexity is a reliable early abstain. |
| 2026-10-06 | Parallel `fast` search (batch, 64 rows) + Jev v3 (wider competitor target) on both providers | search `174729`; Jev v3 `183526` (Parallel), `183548` (Perplexity) | Parallel p50 1.06s / p95 1.6s, $0.064. v3: 0 competitor abstains on Parallel (was 2); Perplexity 8/64 abstains, all among v2's. Jev p95 0.6–1.4s. | v3 fixes the competitor-target bug; Luna on v3 not run yet. |

## Answered (details in RESEARCH.md)
- Objective text as the query: no, coverage 52% vs 86% with the sub-queries.
- `batch`: yes, 3.3× fewer requests, coverage 86% → 80%.
- `fast` vs `web`: same coverage (86%), 5× cheaper; `fast` + batch p50 0.55s.
- Jev time: +0.37-0.40s p50, +0.5-1.4s p95 (`per_link`).
- Jev precision: 44% → 93% (Perplexity), 33% → 82% (Parallel); thresholds swept offline, on_target ≥0.6.
- Jev abstains: on Perplexity 9/9 matched Luna's own "no"; on Parallel 6/8 (2 = competitor-target bug, fixed in v3).
- Does Jev improve Luna's answers? Not on Perplexity (useful -0.06, p=0.64); on Parallel +0.24, mainly right-subject (p=0.01).
- Perplexity vs Parallel (`fast`): Perplexity gives better answers (useful 3.48 vs 2.98) and is ~2× faster.

## Open questions
- Does the judge agree with humans? Fill `outputs/judge/20261006-183425…/human_review.csv`, then `wsx judge-score latest`.
- Does Jev v3 recover the Parallel competitor answers through Luna (22 rows × 2 providers)?
- How much do Luna's answers vary run to run (repeat one arm, compare answer status and judge scores)?
- What does `gpt-6-luna` cost per answer (set `llm.pricing`)?
- Can Luna's latency (p50 ~13s, p95 ~57s) come down (reasoning effort, output length) without losing quality?
- Does a biomedical domain allow-list raise precision without losing company/press-release sources?
- How well does the anchor-hit proxy track human relevance? Check with `review score`.
