"""Parallel Search API: POST https://api.parallel.ai/v1/search

Docs: https://docs.parallel.ai/search/best-practices, modes: https://docs.parallel.ai/search/modes
Body: {objective, search_queries (1-5), mode (turbo|fast|basic|advanced), max_chars_total,
advanced_settings: {max_results (1-20, default 10), excerpt_settings: {max_chars_per_result},
source_policy, location}}. Keys under `params:` in the run config are passed through as-is.
One request takes the row objective plus up to 5 queries and returns one ranked list, so it
maps to `batch` mode. Results carry `excerpts` (several passages), joined into `snippet`.
"""

from __future__ import annotations

from typing import Any

from .base import Provider, normalized_result

URL = "https://api.parallel.ai/v1/search"


class ParallelProvider(Provider):
    name = "parallel"
    env_key = "PARALLEL_API_KEY"
    max_queries_per_request = 5

    def build_request(self, query: str | list[str], objective: str | None = None) -> tuple[str, dict, dict]:
        headers = {"x-api-key": self.api_key, "Content-Type": "application/json"}
        queries = [query] if isinstance(query, str) else list(query)
        body = {"search_queries": queries, **self.params}
        if objective:
            body["objective"] = objective
        return URL, headers, body

    def parse_results(self, data: Any) -> list[dict]:
        out = []
        for rank, r in enumerate(data.get("results") or [], start=1):
            excerpts = [e for e in (r.get("excerpts") or []) if e]
            out.append(normalized_result(rank, r.get("title"), r.get("url"), "\n\n".join(excerpts),
                                         r.get("publish_date")))
        return out

    def price_key(self) -> str:
        return self.params.get("mode", "advanced")
