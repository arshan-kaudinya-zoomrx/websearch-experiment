"""Ad-hoc single search: `wsx query "text"` -> pretty print + outputs/queries/<ts>__...{json,md}."""

from __future__ import annotations

import asyncio
import json
import textwrap
from datetime import datetime, timezone
from pathlib import Path

import httpx

from . import QUERIES_DIR
from .metrics import anchor_hit, categorize, load_domain_categories
from .providers import Provider, get_provider
from .runner import slug


def run_query(cfg: dict, query: str | list[str], anchors: list[str] | None = None,
              transport: httpx.AsyncBaseTransport | None = None,
              out_dir: Path | None = None, jev_cfg: dict | None = None,
              objective: str | None = None) -> tuple[dict, Path, Path]:
    """One live search; with `jev_cfg`, the links are then filtered by Jev against `objective`
    (default: the query text) and the timing is split into search + jev."""
    from .filtering import filter_list, target_of
    from .filters import get_filter

    provider: Provider = get_provider(cfg["provider"], cfg["params"], cfg["run"]["timeout_s"])
    if isinstance(query, list) and len(query) > provider.max_queries_per_request:
        raise SystemExit(f"{provider.name} accepts at most {provider.max_queries_per_request} queries per request.")
    provider.check_ready()
    filt = get_filter(jev_cfg) if jev_cfg else None
    if filt:
        filt.check_ready()
    objective = objective or (query if isinstance(query, str) else " ".join(query))

    async def go():
        async with httpx.AsyncClient(transport=transport) as client:
            resp = await provider.search(client, query)
            jev = None
            if filt and resp.ok:
                jev = await filter_list(filt, client, objective, resp.results, jev_cfg["select"],
                                        target_of(objective, anchors, jev_cfg))
            return resp, jev

    started = datetime.now(timezone.utc)
    resp, jev = asyncio.run(go())
    categories = load_domain_categories()
    anchors = anchors or []
    found = jev.pop("results") if jev else resp.results  # with Jev: deduped, in Jev order
    results = [{**r, "category": categorize(r["domain"], categories),
                **({"anchor_hit": anchor_hit(r, anchors)} if anchors else {})} for r in found]

    record = {
        "ts": started.isoformat(timespec="seconds"),
        "provider": provider.name,
        "config_name": cfg["name"],
        "query": query,
        "anchors": anchors,
        "request": resp.request,
        "ok": resp.ok,
        "status": resp.status,
        "error": resp.error,
        "latency_ms": round(resp.latency_ms, 1),
        "n_results": len(results),
        "cost_usd": provider.cost_per_request(cfg["pricing"]) if resp.ok else 0.0,
        **({"jev": {"config_name": jev_cfg["name"], "granularity": jev_cfg["granularity"],
                    "objective": objective, "select": jev_cfg["select"], **jev,
                    "total_ms": round(resp.latency_ms + jev["jev_latency_ms"], 1)}} if jev else {}),
        "results": results,
        "raw": resp.raw if (cfg["run"].get("save_raw") or not resp.ok) else
               {k: v for k, v in (resp.raw or {}).items() if k != "results"},
    }

    out_dir = out_dir or QUERIES_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    first = query if isinstance(query, str) else query[0]
    stem = f"{datetime.now():%Y%m%d-%H%M%S}__{slug(provider.name)}-{slug(cfg['name'])}__{slug(first)[:60]}"
    json_path, md_path = out_dir / f"{stem}.json", out_dir / f"{stem}.md"
    json_path.write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")
    md_path.write_text(render(record, markdown=True), encoding="utf-8")
    return record, json_path, md_path


def render(rec: dict, markdown: bool = False, snippet_chars: int = 300) -> str:
    q = rec["query"] if isinstance(rec["query"], str) else " || ".join(rec["query"])
    params = {k: v for k, v in rec["request"].items() if k != "query"}
    status = "OK" if rec["ok"] else f"FAILED ({rec['error']})"
    hits = sum(1 for r in rec["results"] if r.get("anchor_hit"))
    head = [
        f"Query:    {q}",
        f"Provider: {rec['provider']} ({rec['config_name']})  params={json.dumps(params, ensure_ascii=False)}",
        f"Status:   {status}  latency={rec['latency_ms']:.0f} ms  results={rec['n_results']}  cost=${rec['cost_usd']}"
        + (f"  anchor hits={hits}/{rec['n_results']} {rec['anchors']}" if rec["anchors"] else ""),
    ]
    jev = rec.get("jev")
    if jev:
        verdict = "ABSTAIN (no link passed)" if jev["abstain"] else f"kept {jev['n_kept']}/{jev['n_candidates']}"
        head += [
            f"Jev:      {jev['config_name']} ({jev['granularity']}, keep >= {jev['select']['keep_threshold']}, "
            f"max {jev['select']['max_keep']})  {verdict}  calls={jev['calls']}  cost=${jev['cost_usd']}"
            + (f"  ERROR {jev['error']}" if jev["error"] else ""),
            f"Timing:   search {rec['latency_ms']:.0f} ms + jev {jev['jev_latency_ms']:.0f} ms "
            f"= {jev['total_ms']:.0f} ms",
            f"Objective: {jev['objective']}" + (f"  | target: {jev['target']}" if jev.get("target") else ""),
        ]
    lines = ([f"# Search: {q}", "", "```", *head, "```", ""] if markdown else [*head, "-" * 80])
    for r in rec["results"]:
        tag = " [anchor]" if r.get("anchor_hit") else ""
        if jev:
            score = "n/a" if r.get("jev_score") is None else f"{r['jev_score']:.2f}"
            ans = " ".join(f"{q}={v:.2f}" for q, v in (r.get("answers") or {}).items())
            verdict = "KEPT" if r.get("kept") else f"dropped: {r.get('reason', '-')}"
            tag += f" | jev {score} [{ans}] {verdict} (was #{r['orig_rank']})"
        meta = f"{r['domain']} | {r['category']} | {r.get('date') or 'no date'}{tag}"
        snippet = " ".join(r["snippet"].split())
        if len(snippet) > snippet_chars:
            snippet = snippet[:snippet_chars].rstrip() + "..."
        qi = f" (q{r['query_index'] + 1})" if r.get("query_index") is not None else ""
        rank = r.get("jev_rank", r["rank"])
        if markdown:
            lines += [f"### {rank}{qi}. {r['title'] or '(no title)'}", "",
                      f"{meta}  ", f"<{r['url']}>", "", f"> {snippet}", ""]
        else:
            lines += [f"{rank:>2}{qi}. {r['title'] or '(no title)'}",
                      f"    {meta}",
                      f"    {r['url']}",
                      *textwrap.wrap(snippet, width=96, initial_indent="    ", subsequent_indent="    "),
                      ""]
    return "\n".join(lines) + "\n"
