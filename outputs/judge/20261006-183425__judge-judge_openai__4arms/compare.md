# Luna answer quality by arm: `20261006-183425__judge-judge_openai__4arms`

Judge `gpt-6-luna` on 62/64 rows (0 rows not judged: an arm errored []) · position check: same winner 70%, rank ρ 0.84 (n=10) · judge cost $0.0

| arm | answered | jev abstain | complete | ungrounded tok | search-talk | bad tags | names subject | judge correct | complete | subject | useful | mean rank | wins | total p50 ms | total p95 ms | $ / answer |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| perplexity-fast/batch | 61% | 0% | 0% | 3% | 0% | 0% | 95% | 4.65 | 3.68 | 4.44 | 3.48 | 2.4 | 26% | 13129.2 | 57013.8 | 0.001 |
| parallel-fast/batch | 62% | 0% | 2% | 2% | 0% | 0% | 95% | 4.4 | 3.11 | 4.15 | 2.98 | 2.53 | 18% | 18145.0 | 60168.8 | 0.001 |
| perplexity-fast/batch + jev | 66% | 14% | 5% | 2% | 2% | 0% | 87% | 4.63 | 3.63 | 4.4 | 3.42 | 2.53 | 24% | 17458.2 | 56282.8 | 0.00141 |
| parallel-fast/batch + jev | 56% | 12% | 3% | 2% | 0% | 0% | 94% | 4.47 | 3.16 | 4.44 | 3.23 | 2.53 | 32% | 11558.8 | 49105.2 | 0.00142 |

Pairwise (row beats column, share of rows):

| | perplexity-fast/batch | parallel-fast/batch | perplexity-fast/batch + jev | parallel-fast/batch + jev |
|---|---|---|---|---|
| perplexity-fast/batch | - | 55% | 52% | 53% |
| parallel-fast/batch | 45% | - | 50% | 52% |
| perplexity-fast/batch + jev | 48% | 50% | - | 48% |
| parallel-fast/batch + jev | 47% | 48% | 52% | - |

Judge `useful` by facet:

| facet | perplexity-fast/batch | parallel-fast/batch | perplexity-fast/batch + jev | parallel-fast/batch + jev |
|---|---|---|---|---|
| catalysts | 3.78 | 3.22 | 3.33 | 3.44 |
| commercial | 3.04 | 2.52 | 3.04 | 3.09 |
| core | 2.25 | 3.5 | 2.75 | 4.0 |
| readout | 3.96 | 3.23 | 3.88 | 3.15 |
