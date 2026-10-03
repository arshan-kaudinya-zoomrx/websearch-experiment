"""Load Web_Questions.csv, normalize to questions.jsonl, derive anchor terms.

An *anchor* is the asset/drug name a question is about (e.g. "SOR102"). It is
used as a cheap relevance proxy: a result "hits" if any anchor appears in its
title, URL or snippet. Anchors are derived heuristically from the queries and
can be corrected in data/anchor_overrides.yaml.
"""

from __future__ import annotations

import ast
import csv
import hashlib
import json
import re
import unicodedata
from pathlib import Path

import yaml

from . import DATA_DIR

CSV_PATH = DATA_DIR / "Web_Questions.csv"
JSONL_PATH = DATA_DIR / "questions.jsonl"
OVERRIDES_PATH = DATA_DIR / "anchor_overrides.yaml"

# Words that are never distinctive enough to count as an anchor on their own.
GENERIC_WORDS = {
    "inhibitor", "inhibitors", "vaccine", "vector", "compound", "dual", "novel",
    "treatment", "asset", "antibody", "therapy", "small", "molecule", "the",
}


def normalize(text: str) -> str:
    """Lowercase, NFKC, drop everything that is not a letter or digit.

    Makes "SOR-102", "SOR 102" and "sor102" all equal.
    """
    text = unicodedata.normalize("NFKC", text or "").lower()
    return "".join(ch for ch in text if ch.isalnum())


def parse_queries(cell: str) -> list[str]:
    cell = (cell or "").strip()
    if not cell:
        return []
    try:
        value = json.loads(cell)
    except json.JSONDecodeError:
        value = ast.literal_eval(cell)
    return [str(q).strip() for q in value if str(q).strip()]


def _common_word_prefix(queries: list[str]) -> list[str]:
    split = [q.split() for q in queries]
    prefix: list[str] = []
    for words in zip(*split):
        if all(w.lower() == words[0].lower() for w in words):
            prefix.append(words[0])
        else:
            break
    return prefix


def derive_anchors(queries: list[str]) -> list[str]:
    """Heuristic anchor terms for a row (any one matching counts as a hit)."""
    if not queries:
        return []
    if len(queries) == 1:
        words = queries[0].split()
        prefix = words[:1]
        # Extend past generic leading words ("Compound 18l", "Dual CDK12/13 ...").
        while prefix and normalize(prefix[-1]) in GENERIC_WORDS and len(prefix) < len(words):
            prefix.append(words[len(prefix)])
        phrases = [" ".join(prefix)]
    else:
        prefix = _common_word_prefix(queries)
        if prefix:
            phrases = [" ".join(prefix)]
        else:  # rows whose queries use different names (e.g. Sirpiglenastat / DRP-104)
            phrases = [q.split()[0] for q in queries]

    candidates: list[str] = []
    for phrase in phrases:
        candidates.append(phrase)
        # "A/B" and "A + B" name alternatives: every part counts. Otherwise only
        # code-like tokens (with a digit) are split out, so "Crohn's" never becomes an anchor.
        has_alternatives = bool(re.search(r"[/+]", phrase))
        for token in re.split(r"[\s/()+,]+", phrase):
            norm = normalize(token)
            if len(norm) < 4 or norm in GENERIC_WORDS:
                continue
            if has_alternatives or any(ch.isdigit() for ch in norm):
                candidates.append(token)

    anchors: list[str] = []
    seen: set[str] = set()
    for cand in candidates:
        norm = normalize(cand)
        if norm and norm not in seen and norm not in GENERIC_WORDS:
            seen.add(norm)
            anchors.append(cand)
    return anchors


def load_overrides(path: Path = OVERRIDES_PATH) -> dict[str, list[str]]:
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return {str(k): [str(a) for a in v] for k, v in data.items()}


def build_questions(csv_path: Path = CSV_PATH, overrides_path: Path = OVERRIDES_PATH) -> list[dict]:
    overrides = load_overrides(overrides_path)
    questions = []
    with csv_path.open(encoding="utf-8-sig", newline="") as f:
        for i, row in enumerate(csv.DictReader(f), start=1):
            qid = f"q{i:03d}"
            queries = parse_queries(row.get("Queries", ""))
            auto = derive_anchors(queries)
            questions.append({
                "id": qid,
                "objective": (row.get("Objectives") or "").strip(),
                "queries": queries,
                "anchors": overrides.get(qid, auto),
                "anchors_source": "override" if qid in overrides else "auto",
            })
    return questions


def write_questions(questions: list[dict], path: Path = JSONL_PATH) -> None:
    with path.open("w", encoding="utf-8") as f:
        for q in questions:
            f.write(json.dumps(q, ensure_ascii=False) + "\n")


def load_questions(path: Path = JSONL_PATH) -> list[dict]:
    if not path.exists():
        questions = build_questions()
        write_questions(questions, path)
        return questions
    with path.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def select_rows(questions: list[dict], rows: str | None = "all", sample: int | None = None,
                seed: int = 42) -> list[dict]:
    """rows: "all" | "1-10" | "1-5,9,12" | "q003,q017" (1-based row numbers or ids)."""
    selected = questions
    if rows and str(rows).lower() != "all":
        wanted: set[str] = set()
        for part in str(rows).split(","):
            part = part.strip()
            if not part:
                continue
            if part.lower().startswith("q"):
                wanted.add(part.lower())
            elif "-" in part:
                lo, hi = (int(x) for x in part.split("-", 1))
                wanted.update(f"q{n:03d}" for n in range(lo, hi + 1))
            else:
                wanted.add(f"q{int(part):03d}")
        selected = [q for q in questions if q["id"] in wanted]
    if sample:
        import random
        rng = random.Random(seed)
        selected = sorted(rng.sample(selected, min(sample, len(selected))), key=lambda q: q["id"])
    return selected
