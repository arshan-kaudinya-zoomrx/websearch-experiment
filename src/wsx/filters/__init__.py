from .base import Filter, FilterResponse
from .jev import JevFilter

# Register new filters / rerankers here (name -> class).
FILTERS: dict[str, type[Filter]] = {
    JevFilter.name: JevFilter,
}


def get_filter(cfg: dict) -> Filter:
    try:
        cls = FILTERS[cfg["filter"]]
    except KeyError:
        raise SystemExit(f"Unknown filter '{cfg.get('filter')}'. Available: {', '.join(FILTERS)}")
    return cls(cfg)


__all__ = ["FILTERS", "Filter", "FilterResponse", "get_filter"]
