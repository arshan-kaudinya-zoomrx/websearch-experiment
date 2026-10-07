"""OpenAI Chat Completions client (httpx, JSON mode) shared by Luna synthesis and the judge.

Config block (`llm:` in configs/luna_openai.yaml, configs/judge_openai.yaml):
  model, temperature (null = omit; reasoning models reject it), reasoning_effort (null = omit),
  max_completion_tokens, timeout_s, retries, pricing {per_1m_input_tokens, per_1m_cached_input_tokens,
  per_1m_output_tokens}.
"""

from __future__ import annotations

import asyncio
import json
import os
import random
import time
from dataclasses import asdict, dataclass, field

import httpx

URL = "https://api.openai.com/v1/chat/completions"
ENV_KEY = "OPENAI_API_KEY"
RETRYABLE = {408, 409, 425, 429, 500, 502, 503, 504}


@dataclass
class LLMResponse:
    ok: bool
    latency_ms: float
    text: str = ""
    parsed: dict | None = None
    usage: dict = field(default_factory=lambda: {"input_tokens": 0, "cached_input_tokens": 0, "output_tokens": 0})
    attempts: int = 0
    status: int | None = None
    error: str | None = None
    wall_ms: float | None = None         # including failed attempts and backoff

    def to_dict(self) -> dict:
        return asdict(self)


def check_ready(llm_cfg: dict) -> None:
    if not os.environ.get(ENV_KEY):
        raise SystemExit(f"{ENV_KEY} is not set. Add it to .env (see .env.example).")
    if not llm_cfg.get("model"):
        raise SystemExit("llm.model is not set: put the model name in the config or pass --set llm.model=<name>.")


def estimate_tokens(text: str) -> int:
    return len(text) // 4 + 1


def cost_usd(llm_cfg: dict, usage: dict) -> float:
    p = llm_cfg.get("pricing") or {}
    cached = int(usage.get("cached_input_tokens", 0))
    fresh = int(usage.get("input_tokens", 0)) - cached
    cached_price = p.get("per_1m_cached_input_tokens")
    cached_price = float(p.get("per_1m_input_tokens", 0) if cached_price is None else cached_price)
    return (fresh * float(p.get("per_1m_input_tokens", 0)) + cached * cached_price
            + int(usage.get("output_tokens", 0)) * float(p.get("per_1m_output_tokens", 0))) / 1e6


def request_body(llm_cfg: dict, system: str, user: str) -> dict:
    body = {"model": llm_cfg["model"],
            "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
            "response_format": {"type": "json_object"}}
    for key in ("temperature", "reasoning_effort", "max_completion_tokens", "seed"):
        if llm_cfg.get(key) is not None:
            body[key] = llm_cfg[key]
    return body


def parse_json(text: str) -> dict | None:
    text = (text or "").strip()
    if text.startswith("```"):
        text = text.strip("`").removeprefix("json").strip()
    try:
        out = json.loads(text)
    except ValueError:
        start, end = text.find("{"), text.rfind("}")
        if start < 0 or end <= start:
            return None
        try:
            out = json.loads(text[start:end + 1])
        except ValueError:
            return None
    return out if isinstance(out, dict) else None


async def complete(client: httpx.AsyncClient, llm_cfg: dict, system: str, user: str) -> LLMResponse:
    headers = {"Authorization": f"Bearer {os.environ.get(ENV_KEY, '')}", "Content-Type": "application/json"}
    body = request_body(llm_cfg, system, user)
    retries, timeout = int(llm_cfg.get("retries", 2)), float(llm_cfg.get("timeout_s", 120))
    # latency_ms = the final attempt only (like search latency in runner.py); wall_ms adds retries + backoff.
    attempts, t_start = 0, time.perf_counter()
    while True:
        attempts += 1
        t0 = time.perf_counter()
        try:
            resp = await client.post(URL, headers=headers, json=body, timeout=timeout)
            status, err = resp.status_code, None if resp.status_code == 200 else f"HTTP {resp.status_code}: {resp.text[:300]}"
        except httpx.HTTPError as e:
            resp, status, err = None, None, f"{type(e).__name__}: {e}"
        latency = (time.perf_counter() - t0) * 1000
        if err is None or (status is not None and status not in RETRYABLE) or attempts > retries:
            break
        wait = min(60, 2 ** attempts)
        if resp is not None and status == 429:  # rate limit: honour Retry-After, else back off longer
            try:
                wait = max(wait, float(resp.headers.get("retry-after", 0)), 10 * attempts)
            except ValueError:
                wait = max(wait, 10 * attempts)
        await asyncio.sleep(wait + random.random())
    wall = (time.perf_counter() - t_start) * 1000
    if err:
        return LLMResponse(False, latency, attempts=attempts, status=status, error=err, wall_ms=wall)
    try:
        data = resp.json()
    except ValueError:  # 200 with a non-JSON body (proxy page, truncated): fail this row, not the run
        return LLMResponse(False, latency, resp.text[:300], attempts=attempts, status=status,
                           error="HTTP 200 with a non-JSON body", wall_ms=wall)
    u = data.get("usage") or {}
    usage = {"input_tokens": int(u.get("prompt_tokens", 0)),
             "cached_input_tokens": int((u.get("prompt_tokens_details") or {}).get("cached_tokens", 0)),
             "output_tokens": int(u.get("completion_tokens", 0))}
    text = ((data.get("choices") or [{}])[0].get("message") or {}).get("content") or ""
    parsed = parse_json(text)
    return LLMResponse(parsed is not None, latency, text, parsed, usage, attempts, status,
                       None if parsed is not None else "invalid JSON", wall)
