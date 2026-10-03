# Comparison (2026-10-03T18:13:37)

Baseline: `perplexity-pplx_web_default__queries`

| metric | `perplexity-pplx_web_default__queries` | `perplexity-pplx_web_default__objective` | `perplexity-pplx_web_default__batch` | `perplexity-pplx_fast__queries` | `perplexity-pplx_fast__objective` | `perplexity-pplx_fast__batch` |
|---|---|---|---|---|---|---|
| mode | queries | objective | batch | queries | objective | batch |
| search_type | web | web | web | fast | fast | fast |
| max_results | 10 | 10 | 10 | 10 | 10 | 10 |
| requests | 210 | 64 | 64 | 210 | 64 | 64 |
| error rate | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| zero-result rate | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% | 0.0% |
| latency p50 ms | 2660.0 | 2330.4 | 2241.3 | 2059.2 | 546.8 | 553.6 |
| latency p95 ms | 19287.0 | 16231.9 | 8948.2 | 18062.6 | 2392.6 | 1138.6 |
| results / request | 9.92 | 10.0 | 10.0 | 9.9 | 10.0 | 10.0 |
| anchor hit@1 | 67.1% | 37.5% | 70.3% | 63.8% | 39.1% | 67.2% |
| anchor hit@3 | 72.4% | 43.8% | 75.0% | 72.4% | 43.8% | 73.4% |
| anchor hit@k | 81.0% | 51.6% | 79.7% | 81.4% | 51.6% | 79.7% |
| objective coverage | 85.9% | 51.6% | 79.7% | 85.9% | 51.6% | 79.7% |
| registry share | 2.5% | 1.7% | 2.3% | 2.6% | 1.7% | 2.5% |
| literature share | 32.7% | 53.8% | 28.1% | 32.3% | 54.1% | 28.7% |
| company/press share | 1.4% | 0.8% | 1.4% | 1.5% | 1.6% | 1.6% |
| dated within 12m | 55.7% | 47.7% | 60.6% | 54.1% | 47.0% | 59.5% |
| cost USD | 1.05 | 0.32 | 0.32 | 0.21 | 0.064 | 0.064 |
| review precision | - | - | - | - | - | - |

## vs baseline (row level)

| candidate | rows | URL Jaccard | coverage wins | coverage losses |
|---|---|---|---|---|
| `perplexity-pplx_web_default__objective` | 64 | 0.082 | 1 q051 | 23 q002, q006, q009, q016, q018, q024, q025, q026, q027, q034, q036, q039, q040, q042, q043, q044, q046, q054, q056, q058, q059, q061, q064 |
| `perplexity-pplx_web_default__batch` | 64 | 0.364 | 0  | 4 q036, q043, q046, q056 |
| `perplexity-pplx_fast__queries` | 64 | 0.65 | 0  | 0  |
| `perplexity-pplx_fast__objective` | 64 | 0.079 | 1 q051 | 23 q002, q006, q009, q016, q018, q024, q026, q027, q033, q034, q036, q039, q040, q042, q043, q044, q052, q054, q056, q058, q059, q061, q064 |
| `perplexity-pplx_fast__batch` | 64 | 0.37 | 0  | 4 q033, q036, q056, q061 |
