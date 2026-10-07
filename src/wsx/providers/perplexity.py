"""Perplexity Search API: POST https://api.perplexity.ai/search

Docs: https://docs.perplexity.ai/api-reference/search-post
All keys under `params:` in the run config are passed through as-is, e.g.
search_type (web|fast), max_results (1-20), search_context_size (low|medium|high),
max_tokens, max_tokens_per_page, country, search_language_filter,
search_domain_filter (<=20), search_recency_filter (hour|day|week|month|year),
search_after_date_filter / search_before_date_filter (MM/DD/YYYY),
last_updated_after_filter / last_updated_before_filter.
"""

from __future__ import annotations

from typing import Any

from .base import Provider, normalized_result

URL = "https://api.perplexity.ai/search"


class PerplexityProvider(Provider):
    name = "perplexity"
    env_key = "PERPLEXITY_API_KEY"
    max_queries_per_request = 5  # multi-query: billed as one request

    def build_request(self, query: str | list[str], objective: str | None = None) -> tuple[str, dict, dict]:
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        return URL, headers, {"query": query, **self.params}

    def parse_results(self, data: Any) -> list[dict]:
        items = data.get("results") or []
        out: list[dict] = []
        # Multi-query responses may be flat or grouped per query; handle both.
        if items and isinstance(items[0], list):
            for qi, group in enumerate(items):
                for rank, r in enumerate(group, start=1):
                    out.append(self._one(r, rank, qi))
        else:
            for rank, r in enumerate(items, start=1):
                out.append(self._one(r, rank, None))
        return out

    @staticmethod
    def _one(r: dict, rank: int, qi: int | None) -> dict:
        return normalized_result(rank, r.get("title"), r.get("url"), r.get("snippet"),
                                 r.get("date"), r.get("last_updated"), qi)

    def price_key(self) -> str:
        return self.params.get("search_type", "web")
