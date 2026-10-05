"""Jev (TypeSafe System One): POST https://api.typesafe.ai/v1/systemone

Docs: https://docs.typesafe.ai/api.md, rerank pattern: https://docs.typesafe.ai/cookbooks/rerank_typesafe.md
Every link is asked the config's `questions` (Noul -> probability, Score -> expected level), each
normalized to [0, 1]; selection/gating happens in code (filtering.select).
granularity:
  per_link  one call per link (all questions in it), fired in parallel (the cookbook pattern)
  per_list  one call per list; state holds every link, questions are repeated per link (r1__x, r2__x, ...)
"""

from __future__ import annotations

import asyncio
import json
import random
import time

import httpx

from .base import Filter, FilterResponse

URL = "https://api.typesafe.ai/v1/systemone"
RETRYABLE = {408, 409, 425, 429, 500, 502, 503, 504, 529}


def configured_questions(cfg: dict) -> dict[str, dict]:
    """`questions:` (named, noul or score); falls back to the v1 single `question:` (one noul, 'evidence')."""
    if cfg.get("questions"):
        return cfg["questions"]
    return {"evidence": {"type": "noul", **cfg["question"]}}


class JevFilter(Filter):
    name = "jev"
    env_key = "TYPESAFE_API_KEY"

    def __init__(self, cfg: dict):
        super().__init__(cfg)
        run = cfg.get("run", {})
        self.timeout_s = float(run.get("timeout_s", 15))
        self.retries = int(run.get("retries", 2))
        self.link_sem = asyncio.Semaphore(int(run.get("link_concurrency", 20)))
        self.questions = configured_questions(cfg)

    # ---------- request building ----------

    def _link(self, r: dict) -> dict:
        n = int(self.cfg.get("max_snippet_chars") or 0)
        snippet = " ".join((r.get("snippet") or "").split())
        return {"title": r.get("title", ""), "url": r.get("url", ""), "date": r.get("date"),
                "snippet": snippet[:n] if n else snippet}

    def _question(self, q: dict, prefix: str = "") -> dict:
        body = {"type": q.get("type", "noul"), "instructions": prefix + q["instructions"]}
        if body["type"] == "noul":
            # YAML reads bare `true:`/`false:` keys as booleans; accept both spellings.
            crit = {str(k).lower(): v for k, v in q["criteria"].items()}
            body["criteria"] = {"true": crit["true"], "false": crit["false"]}
        else:
            body["criteria"] = list(q["criteria"])
        return body

    def _state(self, objective: str, target: str | None) -> dict:
        state = {"objective": objective}
        if target and self.cfg.get("send_target"):
            state["target"] = target
        return state

    def build_bodies(self, objective: str, results: list[dict], target: str | None = None) -> list[dict]:
        """Request bodies for one list of results (one per link, or a single one for per_list)."""
        model = self.cfg.get("model", "jev-latest")
        if self.cfg.get("granularity", "per_link") == "per_list":
            state = {**self._state(objective, target),
                     "results": {f"r{i}": self._link(r) for i, r in enumerate(results, 1)}}
            questions = {f"r{i}__{name}": self._question(q, f"Judge only `results.r{i}` (it is `result` below). ")
                         for i in range(1, len(results) + 1) for name, q in self.questions.items()}
            return [{"state": state, "model": model, "questions": questions}]
        return [{"state": {**self._state(objective, target), "result": self._link(r)}, "model": model,
                 "questions": {name: self._question(q) for name, q in self.questions.items()}}
                for r in results]

    def estimate_input_tokens(self, objective: str, results: list[dict], target: str | None = None) -> int:
        if not results:
            return 0
        bodies = self.build_bodies(objective, results, target)
        return sum(len(json.dumps(b, ensure_ascii=False)) for b in bodies) // 2  # calibrated on run 175621

    # ---------- calling ----------

    async def _post(self, client: httpx.AsyncClient, body: dict) -> tuple[dict | None, str | None, int]:
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        attempts = 0
        while True:
            attempts += 1
            status, error, data = None, None, None
            try:
                resp = await client.post(URL, headers=headers, json=body, timeout=self.timeout_s)
                status = resp.status_code
                if status == 200:
                    data = resp.json()
                else:
                    error = f"HTTP {status}: {resp.text[:200]}"
            except (httpx.HTTPError, ValueError) as e:
                error = f"{type(e).__name__}: {e}"
            if data is not None:
                return data, None, attempts
            if not (status is None or status in RETRYABLE) or attempts > self.retries:
                return None, error, attempts
            await asyncio.sleep(min(8, 0.5 * 2 ** attempts) + random.random() * 0.2)

    async def _post_limited(self, client, body):
        async with self.link_sem:
            return await self._post(client, body)

    def _value(self, name: str, answer: dict | None) -> float | None:
        """Noul -> probability; Score -> expected level / top level. Both in [0, 1]."""
        if not isinstance(answer, dict):
            return None
        if answer.get("noul") is not None:
            return round(float(answer["noul"]), 4)
        if answer.get("score") is not None:
            top = max(len(self.questions[name].get("criteria") or []) - 1, 1)
            return round(float(answer["score"]) / top, 4)
        return None

    def _answers(self, raw: dict, prefix: str = "") -> dict | None:
        vals = {name: self._value(name, raw.get(prefix + name)) for name in self.questions}
        return None if any(v is None for v in vals.values()) else vals

    async def score(self, client: httpx.AsyncClient, objective: str, results: list[dict],
                    target: str | None = None) -> FilterResponse:
        if not results:
            return FilterResponse(True, 0.0, [])
        bodies = self.build_bodies(objective, results, target)
        t0 = time.perf_counter()
        outs = await asyncio.gather(*(self._post_limited(client, b) for b in bodies))
        latency_ms = (time.perf_counter() - t0) * 1000

        usage = {"input_tokens": 0, "output_tokens": 0}
        errors = [err for _, err, _ in outs if err]
        for data, _, _ in outs:
            for k in usage:
                usage[k] += int(((data or {}).get("usage") or {}).get(k) or 0)

        if self.cfg.get("granularity") == "per_list":
            raw = (outs[0][0] or {}).get("answers") or {}
            answers = [self._answers(raw, f"r{i}__") for i in range(1, len(results) + 1)]
        else:
            answers = [self._answers((data or {}).get("answers") or {}) for data, _, _ in outs]

        error = errors[0] if errors else None
        if not errors and any(a is None for a in answers):
            error = "missing answer in response"
        return FilterResponse(ok=error is None, latency_ms=latency_ms, answers=answers, calls=len(bodies),
                              attempts=sum(a for _, _, a in outs), usage=usage, error=error)
