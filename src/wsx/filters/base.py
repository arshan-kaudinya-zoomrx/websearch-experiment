"""Filter interface: score fetched links against an objective (rerank / select / abstain)."""

from __future__ import annotations

import os
from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass, field

import httpx


@dataclass
class FilterResponse:
    ok: bool
    latency_ms: float                    # wall time for scoring the whole list
    answers: list[dict | None]           # per input result: {question: value in [0, 1]}, None if its call failed
    calls: int = 0                       # HTTP calls made (excluding retries)
    attempts: int = 0                    # HTTP calls made (including retries)
    usage: dict = field(default_factory=lambda: {"input_tokens": 0, "output_tokens": 0})
    error: str | None = None

    def to_dict(self) -> dict:
        return asdict(self)


class Filter(ABC):
    name: str = ""
    env_key: str = ""

    def __init__(self, cfg: dict):
        self.cfg = cfg
        self.api_key = os.environ.get(self.env_key, "")

    def check_ready(self) -> None:
        if not self.api_key:
            raise SystemExit(f"{self.env_key} is not set. Add it to .env (see .env.example).")

    @abstractmethod
    async def score(self, client: httpx.AsyncClient, objective: str, results: list[dict],
                    target: str | None = None) -> FilterResponse:
        """Answer every configured question for every result, each normalized to [0, 1]."""

    @abstractmethod
    def estimate_input_tokens(self, objective: str, results: list[dict], target: str | None = None) -> int:
        """Rough token estimate for --dry-run cost."""

    def cost_usd(self, input_tokens: int, output_tokens: int = 0) -> float:
        pricing = self.cfg.get("pricing") or {}
        return (input_tokens * float(pricing.get("per_1m_input_tokens", 0))
                + output_tokens * float(pricing.get("per_1m_output_tokens", 0))) / 1e6
