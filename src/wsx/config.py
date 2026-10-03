"""Run config: YAML file (optionally `extends:` another) + CLI overrides over DEFAULTS."""

from __future__ import annotations

import copy
from pathlib import Path

import yaml

from . import CONFIG_DIR

MODES = ("queries", "objective", "batch")

DEFAULTS: dict = {
    "name": "unnamed",
    "provider": "perplexity",
    "mode": "queries",
    "selection": {"rows": "all", "sample": None, "seed": 42},
    "params": {},
    "run": {
        "concurrency": 4,
        "timeout_s": 30,
        "retries": 2,
        "repeat": 1,
        "max_cost_usd": 10.0,  # abort if the estimate is higher (override with --set)
        "save_raw": False,     # store full raw provider responses in results.jsonl
        "review_top_k": 5,     # rows per request in the auto-exported review.csv
    },
    "pricing": {"per_1k_requests": {"web": 5.0, "fast": 1.0, "default": 5.0}},
}


def deep_merge(base: dict, override: dict) -> dict:
    out = copy.deepcopy(base)
    for k, v in (override or {}).items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = deep_merge(out[k], v)
        else:
            out[k] = copy.deepcopy(v)
    return out


def resolve_path(path: str | Path) -> Path:
    p = Path(path)
    if p.exists():
        return p
    for cand in (CONFIG_DIR / p, CONFIG_DIR / f"{p}.yaml"):
        if cand.exists():
            return cand
    raise SystemExit(f"Config not found: {path}")


def load_file(path: str | Path) -> dict:
    p = resolve_path(path)
    data = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    parent = data.pop("extends", None)
    if parent:
        parent_path = (p.parent / parent) if (p.parent / parent).exists() else parent
        data = deep_merge(load_file(parent_path), data)
    return data


def set_dotted(cfg: dict, dotted: str) -> None:
    """Apply "a.b.c=value" (value parsed as YAML, so 20 -> int, [a,b] -> list)."""
    if "=" not in dotted:
        raise SystemExit(f"--set expects key=value, got: {dotted}")
    key, raw = dotted.split("=", 1)
    node = cfg
    parts = key.strip().split(".")
    for part in parts[:-1]:
        node = node.setdefault(part, {})
    node[parts[-1]] = yaml.safe_load(raw)


def build_config(path: str | Path | None, sets: list[str] | None = None, **direct) -> dict:
    cfg = deep_merge(DEFAULTS, load_file(path) if path else {})
    for s in sets or []:
        set_dotted(cfg, s)
    # Convenience flags (--mode, --rows, --sample, --name, ...) win over everything.
    if direct.get("mode"):
        cfg["mode"] = direct["mode"]
    if direct.get("name"):
        cfg["name"] = direct["name"]
    for key in ("rows", "sample", "seed"):
        if direct.get(key) is not None:
            cfg["selection"][key] = direct[key]
    if direct.get("repeat"):
        cfg["run"]["repeat"] = direct["repeat"]
    if direct.get("concurrency"):
        cfg["run"]["concurrency"] = direct["concurrency"]
    if cfg["mode"] not in MODES:
        raise SystemExit(f"mode must be one of {MODES}, got {cfg['mode']}")
    return cfg
