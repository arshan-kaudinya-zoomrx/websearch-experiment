import csv
import json

import httpx
import pytest

from wsx import compare, config, dataset, metrics, review, runner
from wsx.providers.perplexity import PerplexityProvider


# ---------- dataset ----------

def test_parse_queries_json_list():
    assert dataset.parse_queries('["a b", "c"]') == ["a b", "c"]


def test_normalize_ignores_punctuation_and_case():
    assert dataset.normalize("SOR-102") == dataset.normalize("sor 102") == "sor102"


@pytest.mark.parametrize("queries, expected_first", [
    (["Tamuzimod safety UC", "Tamuzimod AEs"], "Tamuzimod"),
    (["Sirpiglenastat PDAC", "DRP-104 pancreatic"], "Sirpiglenastat"),
    (["Compound 18l ALKBH5 AML"], "Compound 18l"),
])
def test_derive_anchors(queries, expected_first):
    assert dataset.derive_anchors(queries)[0] == expected_first


def test_derive_anchors_skips_plain_words():
    anchors = dataset.derive_anchors(["EOM613 Crohn's disease status", "EOM613 Crohn's disease trial"])
    assert "EOM613" in anchors and "disease" not in anchors


def test_real_csv_loads():
    qs = dataset.build_questions()
    assert len(qs) == 64
    assert all(q["queries"] and q["anchors"] for q in qs)


def test_select_rows():
    qs = [{"id": f"q{i:03d}"} for i in range(1, 11)]
    assert [q["id"] for q in dataset.select_rows(qs, "2-3,q007")] == ["q002", "q003", "q007"]
    assert len(dataset.select_rows(qs, "all", sample=4)) == 4


# ---------- config ----------

def test_config_extends_and_set():
    cfg = config.build_config("pplx_fast", ["params.max_results=20"], mode="objective")
    assert cfg["params"]["search_type"] == "fast"
    assert cfg["params"]["max_results"] == 20
    assert cfg["mode"] == "objective"


# ---------- runner ----------

def test_build_cases_modes():
    q = [{"id": "q001", "objective": "obj", "anchors": ["X"], "queries": [f"X {i}" for i in range(7)]}]
    assert len(runner.build_cases(q, "queries")) == 7
    assert len(runner.build_cases(q, "objective")) == 1
    batch = runner.build_cases(q, "batch", max_batch=5)
    assert [len(c["query"]) for c in batch] == [5, 2]


# ---------- provider ----------

def test_perplexity_parse_flat_and_nested():
    p = PerplexityProvider({"search_type": "web", "max_results": None})
    assert p.params == {"search_type": "web"}  # None dropped
    flat = p.parse_results({"results": [{"title": "t", "url": "https://www.a.com/x", "snippet": "s"}]})
    assert flat[0]["domain"] == "a.com" and flat[0]["rank"] == 1
    nested = p.parse_results({"results": [[{"url": "https://a.com"}], [{"url": "https://b.com"}]]})
    assert [(r["query_index"], r["rank"]) for r in nested] == [(0, 1), (1, 1)]


def test_cost_by_tier():
    pricing = {"per_1k_requests": {"web": 5.0, "fast": 1.0}}
    assert PerplexityProvider({"search_type": "fast"}).cost_per_request(pricing) == 0.001
    assert PerplexityProvider({}).cost_per_request(pricing) == 0.005


# ---------- metrics ----------

def _rec(case_id, row_id, results, ok=True, latency=1000.0, anchors=("ABC-1",)):
    return {"case_id": case_id, "row_id": row_id, "anchors": list(anchors), "ok": ok, "repeat": 0,
            "latency_ms": latency, "n_results": len(results), "results": results,
            "error": None if ok else "HTTP 500", "query": "q", "objective": "o"}


def _res(rank, title, domain="pubmed.ncbi.nlm.nih.gov", date="2026-01-01"):
    return {"rank": rank, "title": title, "url": f"https://{domain}/{rank}", "domain": domain,
            "snippet": "", "date": date, "last_updated": None}


def test_summarize_records():
    recs = [
        _rec("q001-1", "q001", [_res(1, "ABC1 trial"), _res(2, "other")]),
        _rec("q001-2", "q001", [_res(1, "other"), _res(2, "other"), _res(3, "abc-1 results")]),
        _rec("q002-1", "q002", [_res(1, "nothing", "example.com")], anchors=("ZZZ9",)),
        _rec("q002-2", "q002", [], ok=False),
    ]
    cats = {"literature": ["ncbi.nlm.nih.gov"]}
    s = metrics.summarize_records(recs, cats, 0.005)
    assert s["error_rate"] == 0.25
    assert s["anchor"]["hit_at_1"] == round(1 / 3, 4)
    assert s["anchor"]["hit_at_3"] == round(2 / 3, 4)
    assert s["objective_coverage"] == 0.5
    assert s["rows_without_hit"] == ["q002"]
    assert s["source_mix"]["literature"] == round(5 / 6, 4)
    assert s["cost_usd"] == 0.015  # only ok requests billed


# ---------- end to end with a mocked API ----------

def test_end_to_end_mocked(tmp_path, monkeypatch):
    monkeypatch.setenv("PERPLEXITY_API_KEY", "test")
    monkeypatch.setattr(compare, "COMPARISONS_DIR", tmp_path / "cmp")
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        body = json.loads(request.content)
        calls.append(body)
        if len(calls) == 1:
            return httpx.Response(429, json={"error": "rate"})  # exercises retry
        q = body["query"] if isinstance(body["query"], str) else body["query"][0]
        return httpx.Response(200, json={"id": "x", "results": [
            {"title": q, "url": "https://clinicaltrials.gov/a", "snippet": "s", "date": "2026-05-01"},
            {"title": "unrelated", "url": "https://example.com/b", "snippet": "s", "date": None},
        ]})

    monkeypatch.setattr(runner.asyncio, "sleep", _no_sleep)
    cfg = config.build_config("pplx_web_default", rows="1-2", concurrency=1)
    d1 = runner.execute(cfg, transport=httpx.MockTransport(handler), runs_dir=tmp_path)
    cfg2 = config.build_config("pplx_fast", rows="1-2", mode="batch")
    d2 = runner.execute(cfg2, transport=httpx.MockTransport(handler), runs_dir=tmp_path)

    for d in (d1, d2):
        assert {p.name for p in d.iterdir()} == {"run.json", "results.jsonl", "summary.json", "review.csv"}
    s1 = json.loads((d1 / "summary.json").read_text(encoding="utf-8"))
    assert s1["n_requests"] == 9 and s1["error_rate"] == 0
    assert s1["anchor"]["hit_at_1"] == 1.0
    assert s1["source_mix"]["registry"] == 0.5

    # review: label the sheet, score it
    sheet = d1 / "review.csv"
    with sheet.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["relevant"] = "Y" if r["rank"] == "1" else "N"
        r["answers_objective"] = "Y" if r["row_id"] == "q001" and r["rank"] == "1" else ""
    with sheet.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=review.COLUMNS)
        w.writeheader()
        w.writerows(rows)
    rv = review.score_review(d1)
    assert rv["precision"] == 0.5
    assert rv["anchor_proxy_vs_human"]["agreement"] == 1.0
    with pytest.raises(SystemExit):
        review.export_review(d1)  # refuses to clobber labels

    j, m = compare.compare_runs([d1, d2])
    out = json.loads(j.read_text(encoding="utf-8"))
    assert out["pairwise_vs_baseline"][0]["rows_compared"] == 2
    assert "anchor hit@1" in m.read_text(encoding="utf-8")


async def _no_sleep(*_a, **_k):
    return None


# ---------- ad-hoc single query ----------

def test_adhoc_query_mocked(tmp_path, monkeypatch):
    from wsx import adhoc
    monkeypatch.setenv("PERPLEXITY_API_KEY", "test")

    def handler(request):
        return httpx.Response(200, json={"id": "x", "results": [
            {"title": "SOR102 Phase 1 safety", "url": "https://www.clinicaltrials.gov/s", "snippet": "AEs ...",
             "date": "2026-02-01"},
            {"title": "Unrelated", "url": "https://example.com/u", "snippet": "x", "date": None},
        ]})

    cfg = config.build_config("pplx_fast")
    rec, j, m = adhoc.run_query(cfg, "SOR102 safety", ["SOR-102"], transport=httpx.MockTransport(handler),
                                out_dir=tmp_path)
    assert rec["ok"] and rec["n_results"] == 2 and rec["cost_usd"] == 0.001
    assert [r["anchor_hit"] for r in rec["results"]] == [True, False]
    assert rec["results"][0]["category"] == "registry"
    assert json.loads(j.read_text(encoding="utf-8"))["query"] == "SOR102 safety"
    assert "### 1. SOR102 Phase 1 safety" in m.read_text(encoding="utf-8")
    text = adhoc.render(rec)
    assert "[anchor]" in text and "anchor hits=1/2" in text
    print(text)


# ---------- Jev filter (mocked TypeSafe API) ----------

def _jev_answer(question, link):
    good = "ABC" in link["title"]
    if question["type"] == "score":  # 4 levels -> top level for good links
        return {"type": "score", "score": 3.0 if good else 0.6}
    return {"type": "noul", "noul": 0.9 if good else 0.1}


def _jev_handler(calls, fail_first=False):
    """Links whose title mentions ABC score high on every question. Handles per_link and per_list."""
    def handler(request):
        body = json.loads(request.content)
        calls.append(body)
        if fail_first and len(calls) == 1:
            return httpx.Response(529, json={"error": "overloaded"})
        st = body["state"]
        if "result" in st:
            answers = {qid: _jev_answer(q, st["result"]) for qid, q in body["questions"].items()}
        else:
            answers = {qid: _jev_answer(q, st["results"][qid.split("__")[0]])
                       for qid, q in body["questions"].items()}
        return httpx.Response(200, json={"model": "jev-1.13.0", "answers": answers,
                                         "usage": {"input_tokens": 100, "output_tokens": 2}})
    return handler


def test_jev_request_bodies():
    from wsx.filtering import build_filter_config
    from wsx.filters import get_filter
    res = [{"title": "t1", "url": "u1", "snippet": "x" * 3000}, {"title": "t2", "url": "u2", "snippet": "s"}]
    per_link = get_filter(build_filter_config("jev_default")).build_bodies("obj", res, "ABC-1")
    assert len(per_link) == 2 and per_link[0]["questions"]["evidence"]["type"] == "noul"
    assert len(per_link[0]["state"]["result"]["snippet"]) == 1500 and "target" not in per_link[0]["state"]
    # regression: YAML `true:` keys parse as booleans; the configured criteria text must reach Jev
    assert per_link[0]["questions"]["evidence"]["criteria"]["true"].startswith("The result is about")
    crit = get_filter(build_filter_config(None, ["question={instructions: q, criteria: {true: kept, false: dropped}}"]))
    assert crit.build_bodies("o", res[:1])[0]["questions"]["evidence"]["criteria"] == {"true": "kept", "false": "dropped"}
    per_list = get_filter(build_filter_config("jev_per_list")).build_bodies("obj", res)
    assert len(per_list) == 1 and set(per_list[0]["questions"]) == {"r1__evidence", "r2__evidence"}
    v2 = get_filter(build_filter_config("jev_v2")).build_bodies("obj", res, "ABC-1")
    assert v2[0]["state"]["target"] == "ABC-1"
    assert v2[0]["questions"]["evidence"]["type"] == "score"
    assert len(v2[0]["questions"]["evidence"]["criteria"]) == 4


def test_target_for_competitor_objectives():
    from wsx.filtering import FILTER_DEFAULTS, target_of
    assert target_of("ABC-1 safety in UC", ["ABC-1", "ABC-1"], FILTER_DEFAULTS) == "ABC-1"
    assert target_of("UC competing agents in the same class as ABC-1", ["ABC-1"], FILTER_DEFAULTS).startswith(
        "drugs competing with ABC-1")


def test_select_gates_reasons_and_abstain():
    from wsx.filtering import candidates, select
    c = candidates([{"url": "a"}, {"url": "b"}, {"url": "a"}, {"url": "c"}, {"url": "d"}])
    assert [x["url"] for x in c] == ["a", "b", "c", "d"]
    answers = [{"on": 0.2, "ev": 0.9}, {"on": 0.9, "ev": 0.9}, None, {"on": 0.9, "ev": 0.3}]
    for x, a in zip(c, answers):
        x["answers"], x["jev_score"] = a, (a["on"] * a["ev"] if a else None)
    ranked = select(c, {"gates": {"on": 0.5, "ev": 0.5}, "max_keep": 5})
    assert {x["url"]: x["reason"] for x in ranked} == {"a": "low_on", "b": "kept", "c": "error", "d": "low_ev"}
    assert ranked[0]["url"] == "b"
    assert not any(x["kept"] for x in select(c, {"keep_threshold": 0.95, "max_keep": 5}))


@pytest.mark.parametrize("cfg_name", ["jev_default", "jev_per_list", "jev_v2"])
def test_apply_filter_mocked(tmp_path, monkeypatch, cfg_name):
    from wsx import filtering
    from wsx.filters import jev
    monkeypatch.setenv("TYPESAFE_API_KEY", "test")
    monkeypatch.setattr(jev.asyncio, "sleep", _no_sleep)
    src = tmp_path / "20260101-000000__perplexity-x__queries"
    src.mkdir()
    recs = [
        {**_rec("q001-1", "q001", [_res(1, "other"), _res(2, "ABC-1 data"), _res(3, "more")]), "mode": "queries"},
        {**_rec("q002-1", "q002", [_res(1, "nothing", "example.com")]), "mode": "queries"},
        {**_rec("q003-1", "q003", [_res(1, "rival drug")]), "mode": "queries",
         "objective": "UC competing agents in the same class as ABC-1"},
    ]
    (src / "results.jsonl").write_text("".join(json.dumps(r) + "\n" for r in recs), encoding="utf-8")
    cfg = filtering.build_filter_config(cfg_name)
    out = filtering.apply_filter(src, cfg, cli_args=[], out_root=tmp_path / "filters",
                                 transport=httpx.MockTransport(_jev_handler([], fail_first=True)))
    assert {p.name for p in out.iterdir()} == {"filter.json", "results.jsonl", "summary.json", "inspect.md"}
    s = json.loads((out / "summary.json").read_text(encoding="utf-8"))
    assert s["error_rate"] == 0 and s["n_scored"] == 3
    q = s["quality"]
    assert q["competitor_lists_excluded"] == 1 and q["rows_judged"] == 2
    assert q["hit_at_1"] == {"without_jev": 0.0, "with_jev": 0.5, "rerank_only": 0.5}
    assert q["anchor_precision"] == {"without_jev": 0.25, "with_jev": 1.0}
    assert s["selection"]["abstain_rate"] == round(2 / 3, 4) and q["abstain_no_anchor_hits"] == 0.5
    assert q["anchor_recall_retained"] == 1.0 and q["rows_lost"] == []
    assert s["timing_ms"]["total"]["p50"] >= s["timing_ms"]["search"]["p50"]
    assert s["calls_per_request_mean"] == (1.0 if cfg_name == "jev_per_list" else round(5 / 3, 2))
    assert "q001-1" in (out / "inspect.md").read_text(encoding="utf-8")
    if cfg_name == "jev_v2":
        assert s["selection"]["reasons"]["kept"] == 1 and "low_on_target" in s["selection"]["reasons"]

    # offline threshold sweep: nothing passes 0.95 -> all abstain
    key = "select.gates.on_target=0.95" if cfg_name == "jev_v2" else "select.keep_threshold=0.95"
    r2 = filtering.rescore(out, [key], out_root=tmp_path / "filters")
    s2 = json.loads((r2 / "summary.json").read_text(encoding="utf-8"))
    assert s2["selection"]["abstain_rate"] == 1.0 and s2["rescored_from"] == out.name


def test_rescore_v1_folder_without_answers(tmp_path):
    from wsx import filtering
    d = tmp_path / "20260101-000000__jev-jev_default__on__src"
    d.mkdir()
    cfg = filtering.build_filter_config("jev_default")
    (d / "filter.json").write_text(json.dumps({"filter_id": d.name, "source_run_id": "src", "config": cfg}))
    rec = {**_rec("q001-1", "q001", []), "search_latency_ms": 1000.0, "jev_latency_ms": 300.0, "total_ms": 1300.0,
           "calls": 1, "usage": {"input_tokens": 1, "output_tokens": 0}, "cost_usd": 0.0, "n_candidates": 1,
           "results": [{**_res(1, "ABC-1 x"), "orig_rank": 1, "jev_rank": 1, "jev_score": 0.4, "kept": False}]}
    (d / "results.jsonl").write_text(json.dumps(rec) + "\n")
    out = filtering.rescore(d, ["select.keep_threshold=0.3"], out_root=tmp_path)
    s = json.loads((out / "summary.json").read_text(encoding="utf-8"))
    assert s["selection"]["kept_mean"] == 1.0 and "jev_default-t0.3-k5" in out.name


def test_adhoc_query_with_jev(tmp_path, monkeypatch):
    from wsx import adhoc, filtering
    monkeypatch.setenv("PERPLEXITY_API_KEY", "test")
    monkeypatch.setenv("TYPESAFE_API_KEY", "test")
    jev_handler = _jev_handler([])

    def handler(request):
        if "typesafe" in request.url.host:
            return jev_handler(request)
        return httpx.Response(200, json={"results": [
            {"title": "Unrelated", "url": "https://example.com/u", "snippet": "x"},
            {"title": "ABC-1 Phase 1 safety", "url": "https://clinicaltrials.gov/s", "snippet": "AEs"},
        ]})

    rec, j, m = adhoc.run_query(config.build_config("pplx_fast"), "ABC-1 safety", ["ABC-1"],
                                transport=httpx.MockTransport(handler), out_dir=tmp_path,
                                jev_cfg=filtering.build_filter_config("jev_v2"))
    assert rec["jev"]["n_kept"] == 1 and rec["jev"]["objective"] == "ABC-1 safety"
    assert rec["jev"]["target"] == "ABC-1"
    assert rec["results"][0]["title"].startswith("ABC-1") and rec["results"][0]["orig_rank"] == 2
    text = adhoc.render(rec)
    assert "Timing:   search" in text and "KEPT" in text and "dropped: low_on_target" in text


def test_filter_aborts_on_auth_error(tmp_path, monkeypatch):
    from wsx import filtering
    monkeypatch.setenv("TYPESAFE_API_KEY", "bad")
    src = tmp_path / "20260101-000000__perplexity-x__queries"
    src.mkdir()
    recs = [{**_rec(f"q00{i}-1", f"q00{i}", [_res(1, "x")]), "mode": "queries"} for i in range(1, 6)]
    (src / "results.jsonl").write_text("".join(json.dumps(r) + "\n" for r in recs), encoding="utf-8")
    calls = []

    def handler(request):
        calls.append(1)
        return httpx.Response(401, json={"detail": "bad key"})

    cfg = filtering.build_filter_config("jev_v2", ["run.concurrency=1"])
    with pytest.raises(SystemExit, match="auth failed"):
        filtering.apply_filter(src, cfg, cli_args=[], out_root=tmp_path / "f", transport=httpx.MockTransport(handler))
    assert len(calls) < 5
