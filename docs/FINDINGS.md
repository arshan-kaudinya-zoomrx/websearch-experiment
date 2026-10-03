# Findings

Keep each entry short: what was run, the key numbers, and a one-line takeaway. Raw numbers live in `outputs/report.md` and `outputs/comparisons/`.

## Log
| date | experiment | runs (folder names) | key numbers | takeaway |
|---|---|---|---|---|
| _pending_ | Baseline: Perplexity web vs fast × queries/objective/batch, all 64 rows | | | |

## Open questions
- Does the `objective` text (long, many repeated terms) retrieve as well as the hand-written sub-queries?
- Does `batch` (5 queries, billed once) keep coverage while cutting cost about 3×?
- Is `fast` ($1/1K) good enough for this niche content, compared with `web` ($5/1K)?
- Does a biomedical domain allow-list raise precision without losing company/press-release sources?
- How well does the anchor-hit proxy track human relevance? Check with `review score`.
