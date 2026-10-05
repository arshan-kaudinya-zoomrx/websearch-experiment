# Findings

Keep each entry short: what was run, the key numbers, and a one-line takeaway. Raw numbers live in `outputs/report.md` and `outputs/comparisons/`.

## Log
| date | experiment | runs (folder names) | key numbers | takeaway |
|---|---|---|---|---|
| _pending_ | Baseline: Perplexity web vs fast × queries/objective/batch, all 64 rows | | | |
| 2026-10-04 | Jev v1 (`jev_default`, per_link, ≥0.5, max 5) on web/queries | `20261004-164721__jev-jev_default__on__20261003-175621…` | Jev p50 369 ms / p95 489 ms (12% of total); kept 3.2 of 9.9 links; abstain 18%; on 42 non-competitor rows: anchor precision 46%→70%, coverage 88%→64%; $0.073 | Fast and cheap, but **the criteria were not sent** (YAML bool-key bug, so Jev got "It does."/"It does not."). It dropped too much: development stage counted as no evidence for approval questions, and partial or on-asset preclinical pages scored about 0.1. It did correctly drop name collisions (DXP-007 = a card game, MNPS = nanoparticles). Lowering the cut-off alone doesn't help (≥0.2 gives 74% coverage) → v2 prompt. |
| 2026-10-04 | Jev v2 (`jev_v2`: on_target noul + 4-level evidence score, gates in code), same links | `20261004-174606__jev-jev_v2__on__…175621…`; offline sweeps `174759/174800/174801` | Jev p50 372 / p95 515 ms (12% of total), $0.095. On 42 non-competitor rows: anchor precision 46%→90%, hit@1 63%→74%, coverage 88%→81%. The 3 rows lost (q016 empty Patsnap page, q033 DXP-007 card game, q056 MNPS nanoparticles) are all correct drops. 1 false abstain in 135 lists. Competitor rows: abstained on 4 of 75 lists, keeping 3.8 rival-drug links per list. Gate sweep: on_target ≥0.6 is best (pages kept with no asset mention 5.2%→2.2%, false abstains 0.7%→1.5%); ≥0.7 adds nothing. `max_keep` 5→10 raises asset links kept from 61% to 88%. | **Useful.** v2 fixes v1's misses: preclinical status now counts for approval questions, on-asset partial evidence is kept (ONC201, HM100714), and Korean/Chinese sources work. Default is now on_target ≥0.6, evidence ≥0.5. The remaining choice is `max_keep` (how much context Luna gets). |

## Open questions
- Does the `objective` text (long, many repeated terms) retrieve as well as the hand-written sub-queries?
- Does `batch` (5 queries, billed once) keep coverage while cutting cost about 3×?
- Is `fast` ($1/1K) good enough for this niche content, compared with `web` ($5/1K)?
- Does a biomedical domain allow-list raise precision without losing company/press-release sources?
- How well does the anchor-hit proxy track human relevance? Check with `review score`.
- Jev: how many ms does it add (p50/p95), `per_link` vs `per_list`?
- Jev: does it raise precision of what reaches Luna without losing rows (`rows_lost`, `anchor_recall_retained`)?
- Jev: which `keep_threshold` gives the best precision/coverage trade-off (`wsx rescore`, free)?
- Jev: are its abstains sensible (`abstain_no_anchor_hits` vs `abstain_with_anchor_hits`)?
