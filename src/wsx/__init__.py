"""wsx: web-search experiment harness."""

from pathlib import Path

__version__ = "0.1.0"

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data"
CONFIG_DIR = ROOT / "configs"
OUTPUT_DIR = ROOT / "outputs"
RUNS_DIR = OUTPUT_DIR / "runs"
COMPARISONS_DIR = OUTPUT_DIR / "comparisons"
QUERIES_DIR = OUTPUT_DIR / "queries"
FILTERS_DIR = OUTPUT_DIR / "filters"
