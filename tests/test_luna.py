"""Parallel provider, Luna synthesis, objective answer metrics, judge (all offline, mocked)."""

import csv
import json

import httpx
import pytest

from test_wsx import _no_sleep, _rec, _res
from wsx import config, metrics


# ---------- Parallel provider ----------

def test_parallel_request_and_parse():
    from wsx.providers import get_provider
    cfg = config.build_config("parallel_fast")
    p = get_provider(cfg["provider"], cfg["params"], 30)
    url, headers, body = p.build_request(["ABC-1 safety", "ABC-1 AEs"], "ABC-1 safety in UC")
    assert url.endswith("/v1/search") and "x-api-key" in headers
    assert body == {"search_queries": ["ABC-1 safety", "ABC-1 AEs"], "mode": "fast",
                    "advanced_settings": {"max_results": 10}, "objective": "ABC-1 safety in UC"}
    res = p.parse_results({"results": [{"url": "https://www.x.org/a", "title": "T", "publish_date": "2026-01-02",
                                        "excerpts": ["one", "two"]}]})
    assert res[0]["snippet"] == "one\n\ntwo" and res[0]["domain"] == "x.org" and res[0]["date"] == "2026-01-02"
    assert p.cost_per_request(cfg["pricing"]) == 0.001


# ---------- Luna synthesis ----------

def _luna_cfg(*sets):
    from wsx.luna import build_luna_config
    return build_luna_config("luna_openai", ["llm.model=test-model", "llm.pricing.per_1m_input_tokens=1",
                                             "llm.pricing.per_1m_output_tokens=4", *sets])


def test_facets_and_messages():
    from wsx.luna import build_messages, facet_of, load_prompts
    cfg = _luna_cfg()
    assert facet_of("q1", "UC competing agents in the same class as ABC-1", cfg) == ("commercial", None)
    assert facet_of("q1", "KRAS G12D drugs approved against the target", cfg) == ("commercial", "target")
    assert facet_of("q1", "ABC-1 first regulatory approval or market launch year in AML", cfg)[0] == "catalysts"
    assert facet_of("q1", "ABC-1 in vivo monotherapy TGI in PDAC animal models", cfg)[0] == "readout"
    assert facet_of("q1", "ABC-1 sponsor development stage", cfg) == (None, None)
    assert facet_of("q1", "ABC-1 safety", cfg, {"q1": {"facet": "corporate"}}) == ("corporate", None)
    prompts = load_prompts(cfg)
    row = {"row_id": "q1", "objective": "ABC-1 safety in UC", "anchors": ["ABC-1", "ABC1"],
           "items": [{**_res(1, "ABC-1 trial"), "snippet": "x " * 2500}]}
    m = build_messages(prompts, row, cfg)
    assert m["system"] == prompts.build_system("readout", None)
    assert "[E1] source: web (pubmed.ncbi.nlm.nih.gov)" in m["user"] and "AS OF: 2026-10-06" in m["user"]
    assert "SUBJECT:\nABC-1\nalso known as: ABC1" in m["user"]
    assert m["user"].count("x ") <= 1500  # evidence.max_chars_per_item = 3000


def test_answer_metrics():
    from wsx.luna import answer_metrics
    ev = [{"id": "E1", "title": "ABC-1 in KPC mice", "url": "u1", "domain": "a.org",
           "text": "ABC-1 reduced tumour volume by 45% versus vehicle at 30 mg/kg in Study X-12."},
          {"id": "E2", "title": "other", "url": "u2", "domain": "b.org", "text": "unrelated"}]
    good = {"has_answer": "yes", "summarized_answer": "ABC-1 reduced tumour volume by 45% at 30 mg/kg. [E1]",
            "confident_score": 0.8, "missing": "safety", "citations": ["E1"], "next_queries": ["ABC-1 safety mice"]}
    m = answer_metrics(good, ev, ["ABC-1"], "o")
    assert m["json_valid"] and m["n_ungrounded"] == 0 and m["n_cited_items"] == 1 and m["subject_in_cited"]
    assert not m["search_talk"] and not m["url_in_answer"] and m["next_queries_subject_first"] == 1
    bad = {**good, "summarized_answer": "Then Rivalix cut volume 77% (see https://x.org) [E3]. "
                                        "The evidence does not state safety."}
    b = answer_metrics(bad, ev, ["ABC-1"], "o")
    assert b["invalid_tags"] == [3] and b["url_in_answer"] and b["search_talk"]
    assert "77%" in b["ungrounded_tokens"] and "Rivalix" in b["ungrounded_tokens"] and not b["names_subject"]
    no = answer_metrics({**good, "has_answer": "no", "summarized_answer": "Nothing found."}, ev, ["ABC-1"], "o")
    assert no["nonempty_when_no"] and not no["has_answer"]
    assert answer_metrics(None, ev, [], "o") == {"json_valid": False}


def _openai_handler(calls, answer_for=None):
    def handler(request):
        body = json.loads(request.content)
        calls.append(body)
        user = body["messages"][1]["content"]
        content = answer_for(user) if answer_for else {
            "has_answer": "yes", "summarized_answer": "ABC-1 data reported. [E1]", "confident_score": 0.7,
            "missing": "nothing", "citations": ["E1"], "next_queries": []}
        return httpx.Response(200, json={"choices": [{"message": {"content": json.dumps(content)}}],
                                         "usage": {"prompt_tokens": 1000, "completion_tokens": 100}})
    return handler


def _make_sources(tmp_path):
    """A Parallel batch run (2 rows) and a Jev folder on it that keeps 1 link of q001 and abstains on q002."""
    run = tmp_path / "20260101-000000__parallel-parallel_fast__batch"
    run.mkdir()
    recs = [_rec("q001-batch", "q001", [_res(1, "ABC-1 mice"), _res(2, "other")]),
            _rec("q002-batch", "q002", [_res(1, "nothing", "example.com")])]
    (run / "results.jsonl").write_text("".join(json.dumps(r) + "\n" for r in recs), encoding="utf-8")
    (run / "run.json").write_text(json.dumps({"config": {"provider": "parallel", "mode": "batch",
                                                         "params": {"mode": "fast"}}}))
    flt = tmp_path / "20260101-000001__jev-jev_v2_k10__on__src"
    flt.mkdir()
    frecs = []
    for r, keep in zip(recs, (True, False)):
        res = [{**x, "orig_rank": i, "jev_rank": i, "jev_score": 0.9 if keep else 0.1, "kept": keep and i == 1}
               for i, x in enumerate(r["results"], start=1)]
        frecs.append({**r, "results": res, "search_latency_ms": 900.0, "jev_latency_ms": 350.0, "cost_usd": 0.0001})
    (flt / "results.jsonl").write_text("".join(json.dumps(r) + "\n" for r in frecs), encoding="utf-8")
    (flt / "filter.json").write_text(json.dumps({"source_run_id": run.name}))  # run found next to it
    return run, flt


def test_synth_mocked(tmp_path, monkeypatch):
    from wsx import llm, luna
    monkeypatch.setenv("OPENAI_API_KEY", "test")
    monkeypatch.setattr(llm.asyncio, "sleep", _no_sleep)
    run, flt = _make_sources(tmp_path)
    calls = []
    out = luna.run_synth(run, _luna_cfg(), cli_args=[], out_root=tmp_path / "synth",
                         transport=httpx.MockTransport(_openai_handler(calls)))
    assert {p.name for p in out.iterdir()} == {"synth.json", "results.jsonl", "summary.json", "answers.md"}
    assert len(calls) == 2 and calls[0]["model"] == "test-model"
    assert calls[0]["response_format"] == {"type": "json_object"} and "temperature" not in calls[0]
    s = json.loads((out / "summary.json").read_text(encoding="utf-8"))
    assert s["arm"] == "parallel-fast/batch" and s["answering"]["answer_rate"] == 1.0
    assert s["cost_usd"]["luna"] == round(2 * (1000 * 1 + 100 * 4) / 1e6, 4)
    assert s["timing_ms"]["total"]["p50"] >= s["timing_ms"]["search"]["p50"]

    calls.clear()
    out2 = luna.run_synth(flt, _luna_cfg(), cli_args=[], out_root=tmp_path / "synth",
                          transport=httpx.MockTransport(_openai_handler(calls)))
    s2 = json.loads((out2 / "summary.json").read_text(encoding="utf-8"))
    assert len(calls) == 1  # q002: Jev kept nothing -> Luna is not called
    assert s2["arm"] == "parallel-fast/batch + jev" and s2["answering"]["jev_abstain_rate"] == 0.5
    assert s2["evidence_use"]["items_given_mean"] == 0.5 and s2["timing_ms"]["jev"]["p50"] == 350.0
    assert "ABSTAIN" in (out2 / "answers.md").read_text(encoding="utf-8")


def test_synth_auth_error_aborts(tmp_path, monkeypatch):
    from wsx import luna
    monkeypatch.setenv("OPENAI_API_KEY", "bad")
    run, _ = _make_sources(tmp_path)
    with pytest.raises(SystemExit, match="auth failed"):
        luna.run_synth(run, _luna_cfg("run.concurrency=1"), cli_args=[], out_root=tmp_path / "s",
                       transport=httpx.MockTransport(lambda r: httpx.Response(401, json={"error": "bad"})))


def test_synth_requires_model(tmp_path, monkeypatch):
    from wsx import luna
    monkeypatch.setenv("OPENAI_API_KEY", "x")
    run, _ = _make_sources(tmp_path)
    with pytest.raises(SystemExit, match="llm.model"):
        luna.run_synth(run, luna.build_luna_config("luna_openai", ["llm.model=null"]), cli_args=[],
                       out_root=tmp_path / "s", transport=httpx.MockTransport(lambda r: httpx.Response(500)))


# ---------- judge ----------

def test_judge_unshuffle_and_spearman():
    from wsx.judge import shuffled, spearman, unshuffle
    order = shuffled(3, 7, "q001")
    assert sorted(order) == [0, 1, 2] and order == shuffled(3, 7, "q001")
    arms = ["a0", "a1", "a2"]
    parsed = {"answers": {L: {"correct": 5, "complete": i + 1, "subject": 5, "useful": i + 1}
                          for i, L in enumerate("ABC")}, "ranking": ["C", "B", "A"]}
    u = unshuffle(parsed, order, arms)
    assert u["valid"] and u["ranking"][0] == arms[order[2]] and u["scores"][arms[order[0]]]["complete"] == 1
    assert spearman(["a", "b", "c"], ["a", "b", "c"]) == 1.0 and spearman(["a", "b", "c"], ["c", "b", "a"]) == -1.0
    assert not unshuffle({"answers": {}, "ranking": []}, order, arms)["valid"]


def test_judge_mocked_with_human_sheet(tmp_path, monkeypatch):
    from wsx import judge, llm, luna
    monkeypatch.setenv("OPENAI_API_KEY", "test")
    monkeypatch.setattr(llm.asyncio, "sleep", _no_sleep)
    run, flt = _make_sources(tmp_path)

    def luna_answer(user):  # Jev arm sees only the on-target link -> "GOOD" answer
        good = "ABC-1 mice" in user and "other" not in user
        return {"has_answer": "yes", "summarized_answer": ("GOOD " if good else "") + "ABC-1 result [E1]",
                "confident_score": 0.8, "missing": "nothing", "citations": ["E1"], "next_queries": []}

    s1 = luna.run_synth(run, _luna_cfg(), cli_args=[], out_root=tmp_path / "synth",
                        transport=httpx.MockTransport(_openai_handler([], luna_answer)))
    s2 = luna.run_synth(flt, _luna_cfg(), cli_args=[], out_root=tmp_path / "synth",
                        transport=httpx.MockTransport(_openai_handler([], luna_answer)))

    def judge_answer(user):
        answers_part = user.split("ANSWERS:")[1]
        assert "[S1]" in user and "[E1]" not in answers_part  # tags re-mapped to the pool
        scores = {b[0]: (5 if "GOOD" in b else 1 if "(EMPTY" in b else 2) for b in answers_part.split("ANSWER ")[1:]}
        return {"answers": {L: {"correct": v, "complete": v, "subject": 5, "useful": v, "errors": []}
                            for L, v in scores.items()},
                "ranking": sorted(scores, key=lambda L: -scores[L]), "pool_answers_objective": "yes"}

    cfg = judge.build_judge_config("judge_openai", ["llm.model=judge-model", "position_check_rows=1", "human_sample=2"])
    out = judge.run_judge([s1, s2], cfg, out_root=tmp_path / "judge",
                          transport=httpx.MockTransport(_openai_handler([], judge_answer)))
    s = json.loads((out / "summary.json").read_text(encoding="utf-8"))
    jev_arm = "parallel-fast/batch + jev"
    assert s["n_valid"] == 2 and s["position_check"]["n"] == 1 and s["position_check"]["same_winner"] == 1.0
    assert s["per_arm"][jev_arm]["win_rate"] == 0.5  # q001 GOOD; q002 abstained (empty) loses to an answer
    assert s["objective"][jev_arm]["answering"]["jev_abstain_rate"] == 0.5
    assert "| arm |" in (out / "compare.md").read_text(encoding="utf-8")

    # fill the human sheet with the judge's own scores -> full agreement
    with (out / "human_review.csv").open(encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    key = json.loads((out / "human_key.json").read_text(encoding="utf-8"))
    judged = {r["row_id"]: r for r in metrics.load_records(out)}
    for r in rows:
        arm = key[r["row_id"]][r["label"]]
        r.update({c: judged[r["row_id"]]["judge"]["scores"][arm][c] for c in judge.CRITERIA})
        r["rank"] = judged[r["row_id"]]["judge"]["ranking"].index(arm) + 1
    with (out / "human_review.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    h = judge.summarize_judge_dir(out)["human"]
    assert h["n_rows"] == 2 and h["exact"] == 1.0 and h["rank_spearman_mean"] == 1.0


# ---------- regressions from code review ----------

def test_pool_keeps_each_arms_text_and_luna_cap():
    from wsx.judge import pool_and_answers
    long = "ABC-1 cut tumour volume 45% " + "x " * 1000 + "and 62% at day 28"
    a = {"evidence": [{"id": "E1", "url": "u", "title": "t", "text": "short snippet"}],
         "output": {"summarized_answer": "a [E1]"}}
    b = {"evidence": [{"id": "E1", "url": "u", "title": "t", "text": long}],
         "output": {"summarized_answer": "b [E1]"}}
    pool, answers = pool_and_answers([a, b])
    assert len(pool) == 1 and "short snippet" in pool[0]["text"] and "62% at day 28" in pool[0]["text"]
    assert answers[0]["text"] == "a [S1]" and answers[1]["text"] == "b [S1]"


def test_evidence_view_matches_what_luna_saw():
    from wsx.luna import _evidence_view, format_evidence
    items = [{**_res(1, "t"), "snippet": "one\n\n\n\n" * 400 + "TAILFACT 99"}]
    shown = format_evidence(items, 3000)
    assert "TAILFACT" in shown and "TAILFACT" in _evidence_view(items, 3000)[0]["text"]


def test_errors_are_not_answers_or_abstains(tmp_path, monkeypatch):
    from wsx import judge, llm, luna
    monkeypatch.setenv("OPENAI_API_KEY", "test")
    monkeypatch.setattr(llm.asyncio, "sleep", _no_sleep)
    run = tmp_path / "20260101-000000__perplexity-pplx_fast__batch"
    run.mkdir()
    recs = [_rec("q001-batch", "q001", [_res(1, "ABC-1 mice")]),
            _rec("q002-batch", "q002", [], ok=False),            # search failed
            _rec("q003-batch", "q003", []),                      # search ok, zero links
            _rec("q004-batch", "q004", [_res(1, "ABC-1 rats")])]  # Luna returns invalid JSON
    (run / "results.jsonl").write_text("".join(json.dumps(r) + "\n" for r in recs), encoding="utf-8")
    (run / "run.json").write_text(json.dumps({"config": {"provider": "perplexity", "mode": "batch",
                                                         "params": {"search_type": "fast"}}}))
    calls = []

    def handler(request):
        calls.append(1)
        bad = "rats" in json.loads(request.content)["messages"][1]["content"]
        content = "not json" if bad else json.dumps({"has_answer": "yes", "summarized_answer": "ABC-1 [E1]",
                                                     "confident_score": 0.7, "missing": "nothing",
                                                     "citations": ["E1"], "next_queries": []})
        return httpx.Response(200, json={"choices": [{"message": {"content": content}}],
                                         "usage": {"prompt_tokens": 10, "completion_tokens": 5}})

    out = luna.run_synth(run, _luna_cfg(), cli_args=[], out_root=tmp_path / "synth",
                         transport=httpx.MockTransport(handler))
    s = json.loads((out / "summary.json").read_text(encoding="utf-8"))
    a = s["answering"]
    assert len(calls) == 2 and s["n_rows"] == 4  # failed search row kept in the denominator
    assert a["answer_rate"] == 0.25 and a["error_rate"] == 0.5 and a["no_links_rate"] == 0.25
    assert a["jev_abstain_rate"] == 0.0 and a["luna_no_rate"] == 0.0
    assert s["contract"]["json_valid_rate"] == 0.5  # of the 2 Luna replies, 1 was valid JSON
    assert "NO LINKS" in (out / "answers.md").read_text(encoding="utf-8")

    p = judge.plan_judge([out, out], judge.build_judge_config("judge_openai", ["llm.model=j"]))
    assert set(p["skipped"]) == {"q002", "q004"} and [x["row_id"] for x in p["items"]] == ["q001", "q003"]
    jcfg = judge.build_judge_config("judge_openai")  # no judge model -> Luna's model and pricing
    judge.plan_judge([out, out], jcfg)
    assert jcfg["llm"]["model"] == "test-model" and jcfg["llm"]["pricing"]["per_1m_output_tokens"] == 4


def test_llm_latency_is_final_attempt(monkeypatch):
    import asyncio
    from wsx import llm
    monkeypatch.setenv("OPENAI_API_KEY", "x")
    n = []

    def handler(request):
        n.append(1)
        if len(n) == 1:
            return httpx.Response(429, json={"error": "rate"})
        return httpx.Response(200, json={"choices": [{"message": {"content": "{}"}}], "usage": {}})

    real_sleep = asyncio.sleep

    async def slow_sleep(*_a, **_k):
        await real_sleep(0.05)

    async def go():
        async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as c:
            return await llm.complete(c, {"model": "m", "retries": 2}, "s", "u")

    monkeypatch.setattr(llm.asyncio, "sleep", slow_sleep)
    r = asyncio.run(go())
    assert r.ok and r.attempts == 2 and r.wall_ms >= 50 > r.latency_ms


def test_per_answer_cost_and_retry_from_any_source_dir(tmp_path, monkeypatch):
    from wsx import llm, luna
    monkeypatch.setenv("OPENAI_API_KEY", "test")
    monkeypatch.setattr(llm.asyncio, "sleep", _no_sleep)
    run = tmp_path / "elsewhere" / "20260101-000000__perplexity-pplx_fast__batch"  # not under RUNS_DIR
    run.mkdir(parents=True)
    recs = [_rec("q001-batch", "q001", [_res(1, "ABC-1 mice")]), _rec("q002-batch", "q002", [_res(1, "ABC-1 rats")])]
    (run / "results.jsonl").write_text("".join(json.dumps(r) + "\n" for r in recs), encoding="utf-8")
    (run / "run.json").write_text(json.dumps({"config": {"provider": "perplexity", "mode": "batch",
                                                         "params": {"search_type": "fast"}}}))
    fail = [True]

    def handler(request):
        if fail[0] and "rats" in json.loads(request.content)["messages"][1]["content"]:
            return httpx.Response(200, json={"choices": [{"message": {"content": "not json"}}], "usage": {}})
        return _openai_handler([])(request)

    out = luna.run_synth(run, _luna_cfg(), cli_args=[], out_root=tmp_path / "synth",
                         transport=httpx.MockTransport(handler))
    c = json.loads((out / "summary.json").read_text(encoding="utf-8"))["cost_usd"]
    assert abs(c["per_answer"] - c["total"]) < 1e-5 and abs(c["per_row"] - c["total"] / 2) < 1e-5  # 1 of 2 answered
    fail[0] = False
    assert luna.retry_failed(out, transport=httpx.MockTransport(handler)) == ["q002"]
    assert json.loads((out / "summary.json").read_text(encoding="utf-8"))["answering"]["answer_rate"] == 1.0


def test_llm_non_json_200_fails_the_row_not_the_run():
    import asyncio
    from wsx import llm

    async def go():
        t = httpx.MockTransport(lambda r: httpx.Response(200, text="<html>gateway</html>"))
        async with httpx.AsyncClient(transport=t) as c:
            return await llm.complete(c, {"model": "m", "retries": 0}, "s", "u")

    r = asyncio.run(go())
    assert not r.ok and r.status == 200 and "non-JSON" in r.error


def test_judge_out_dir_same_second(tmp_path, monkeypatch):
    from datetime import datetime as real_dt
    from wsx import judge, llm, luna
    monkeypatch.setenv("OPENAI_API_KEY", "test")
    monkeypatch.setattr(llm.asyncio, "sleep", _no_sleep)
    run, _ = _make_sources(tmp_path)
    s1 = luna.run_synth(run, _luna_cfg(), cli_args=[], out_root=tmp_path / "synth",
                        transport=httpx.MockTransport(_openai_handler([])))

    class Fixed(real_dt):
        @classmethod
        def now(cls, tz=None):
            return real_dt(2026, 1, 1, 0, 0, 0, tzinfo=tz)

    def judge_answer(user):
        labels = [b[0] for b in user.split("ANSWERS:")[1].split("ANSWER ")[1:]]
        return {"answers": {L: {"correct": 3, "complete": 3, "subject": 3, "useful": 3, "errors": []} for L in labels},
                "ranking": labels, "pool_answers_objective": "yes"}

    monkeypatch.setattr(judge, "datetime", Fixed)
    cfg = judge.build_judge_config("judge_openai", ["llm.model=j", "position_check_rows=0", "human_sample=0"])
    outs = [judge.run_judge([s1, s1], cfg, out_root=tmp_path / "judge",
                            transport=httpx.MockTransport(_openai_handler([], judge_answer))) for _ in range(2)]
    assert outs[0] != outs[1] and outs[1].name.endswith("-2")
