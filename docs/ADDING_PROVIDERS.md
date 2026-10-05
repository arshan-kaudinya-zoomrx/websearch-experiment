# Adding a provider

Candidates from the vendor comparison: Linkup (fast), Brave (LLM Context), Parallel Search, and Tavily.

1. Create `src/wsx/providers/<name>.py` with a subclass of `Provider`:
   ```python
   from .base import Provider, normalized_result

   class LinkupProvider(Provider):
       name = "linkup"
       env_key = "LINKUP_API_KEY"
       max_queries_per_request = 1          # >1 only if the API takes a list of queries

       def build_request(self, query):
           headers = {"Authorization": f"Bearer {self.api_key}"}
           return "https://api.linkup.so/v1/search", headers, {"q": query, **self.params}

       def parse_results(self, data):
           return [normalized_result(i, r.get("name"), r.get("url"), r.get("content"))
                   for i, r in enumerate(data.get("results", []), start=1)]

       def price_key(self):                 # optional: which pricing tier applies
           return self.params.get("depth", "default")
   ```
   For a GET API, or one that needs a special client, override `search()` instead. It must return a `SearchResponse`; copy the timing and error handling from `base.Provider.search`.
2. Register it in `src/wsx/providers/__init__.py` → `PROVIDERS`.
3. Add the key to `.env.example`, then add a config such as `configs/linkup_fast.yaml` with `provider: linkup`, its `params`, and `pricing.per_1k_requests`.
4. Add a `parse_results` test to `tests/test_wsx.py` that uses a saved sample response.
5. Compare it on the same rows: `uv run wsx matrix -c pplx_web_default -c linkup_fast --modes queries`.

Every metric, the review sheet and comparisons work on the normalized results, so nothing else changes.

## Adding a filter / reranker (alongside Jev)
Filters work the same way, in `src/wsx/filters/`. Subclass `Filter` from `base.py` and implement:
- `score(client, objective, results)`: returns a `FilterResponse` with one score from 0 to 1 per link.
- `estimate_input_tokens()`: used by `--dry-run`.

Register the class in `filters/__init__.py`, then add a `configs/<name>.yaml` with `filter: <name>`. Selection, metrics, `rescore` and the report then work unchanged.
