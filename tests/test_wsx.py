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
