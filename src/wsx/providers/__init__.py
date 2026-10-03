from .base import Provider, SearchResponse
from .perplexity import PerplexityProvider

# Register new providers here (name -> class). See docs/ADDING_PROVIDERS.md.
PROVIDERS: dict[str, type[Provider]] = {
    PerplexityProvider.name: PerplexityProvider,
}


def get_provider(name: str, params: dict, timeout_s: float) -> Provider:
    try:
        cls = PROVIDERS[name]
    except KeyError:
        raise SystemExit(f"Unknown provider '{name}'. Available: {', '.join(PROVIDERS)}")
    return cls(params, timeout_s)


__all__ = ["PROVIDERS", "Provider", "SearchResponse", "get_provider"]
