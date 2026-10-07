"""Provider interface. One file per search API; see docs/ADDING_PROVIDERS.md."""

from __future__ import annotations

import os
import time
from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass, field
from typing import Any
from urllib.parse import urlparse

import httpx


@dataclass
class SearchResponse:
    ok: bool
    status: int | None
    latency_ms: float
    request: dict
    results: list[dict] = field(default_factory=list)  # normalized, see normalized_result()
    raw: Any = None
    error: str | None = None

    def to_dict(self) -> dict:
        return asdict(self)


def domain_of(url: str) -> str:
    host = urlparse(url or "").netloc.lower()
    return host[4:] if host.startswith("www.") else host


def normalized_result(rank: int, title: str | None, url: str | None, snippet: str | None,
                      date: str | None = None, last_updated: str | None = None,
                      query_index: int | None = None) -> dict:
    """The common result shape every provider maps to."""
    return {
        "rank": rank,
        "query_index": query_index,
        "title": title or "",
        "url": url or "",
        "domain": domain_of(url or ""),
        "snippet": snippet or "",
        "date": date,
        "last_updated": last_updated,
    }


class Provider(ABC):
    name: str = ""
    env_key: str = ""
    max_queries_per_request: int = 1  # >1 enables "batch" mode natively

    def __init__(self, params: dict, timeout_s: float = 30.0):
        self.params = {k: v for k, v in (params or {}).items() if v not in (None, [], "", {})}
        self.timeout_s = timeout_s
        self.api_key = os.environ.get(self.env_key, "")

    def check_ready(self) -> None:
        if not self.api_key:
            raise SystemExit(f"{self.env_key} is not set. Add it to .env (see .env.example).")

    @abstractmethod
    def build_request(self, query: str | list[str], objective: str | None = None) -> tuple[str, dict, dict]:
        """Return (url, headers, json_body). `objective` is the row's objective; providers may ignore it."""

    @abstractmethod
    def parse_results(self, data: Any) -> list[dict]:
        """Map the provider's JSON response to a list of normalized_result()."""

    def price_key(self) -> str:
        """Key into config pricing.per_1k_requests when prices differ by tier."""
        return "default"

    def cost_per_request(self, pricing: dict) -> float:
        per_1k = (pricing or {}).get("per_1k_requests", 0)
        if isinstance(per_1k, dict):
            per_1k = per_1k.get(self.price_key(), per_1k.get("default", 0))
        return float(per_1k) / 1000.0

    def public_request(self, query: str | list[str], objective: str | None = None) -> dict:
        """Request body as saved to disk (never includes credentials)."""
        return self.build_request(query, objective)[2]

    async def search(self, client: httpx.AsyncClient, query: str | list[str],
                     objective: str | None = None) -> SearchResponse:
        url, headers, body = self.build_request(query, objective)
        t0 = time.perf_counter()
        try:
            resp = await client.post(url, headers=headers, json=body, timeout=self.timeout_s)
        except httpx.HTTPError as e:
            return SearchResponse(False, None, (time.perf_counter() - t0) * 1000, body,
                                  error=f"{type(e).__name__}: {e}")
        latency_ms = (time.perf_counter() - t0) * 1000
        try:
            data = resp.json()
        except ValueError:
            data = {"text": resp.text[:2000]}
        if resp.status_code != 200:
            return SearchResponse(False, resp.status_code, latency_ms, body, raw=data,
                                  error=f"HTTP {resp.status_code}")
        try:
            results = self.parse_results(data)
        except Exception as e:  # malformed payload: keep raw for debugging
            return SearchResponse(False, resp.status_code, latency_ms, body, raw=data,
                                  error=f"parse error: {e}")
        return SearchResponse(True, resp.status_code, latency_ms, body, results=results, raw=data)
