# Calibre AI Integration Guide

This document describes how Semantic Calibre integrates with Calibre's built-in AI module.

## Overview

Calibre has a built-in AI system at `src/calibre/ai/` that provides:
- Provider plugins (Google, OpenAI, Ollama, OpenRouter, GitHub)
- API key management with secure storage
- Capability detection (`AICapabilities` flags)
- User configuration UI

We leverage this system for embeddings rather than duplicating configuration.

## Calibre AI Architecture

```
src/calibre/ai/
├── __init__.py          # AICapabilities enum, base types
├── config.py            # ConfigureAI widget
├── prefs.py             # Provider selection, preferences
├── utils.py             # Shared utilities
├── google/
│   ├── __init__.py      # GoogleAI plugin registration
│   ├── backend.py       # API calls (text_chat, embed)
│   └── config.py        # Google-specific config widget
├── openai/
│   ├── __init__.py      # OpenAI plugin registration
│   ├── backend.py       # API calls
│   └── config.py        # OpenAI config widget
└── ... (ollama, github, open_router)
```

## AICapabilities Enum

```python
# src/calibre/ai/__init__.py
class AICapabilities(Flag):
    none = 0
    text_to_text = auto()      # Chat/completion
    text_to_image = auto()     # Image generation
    text_and_image_to_image = auto()
    embedding = auto()          # <-- We use this
    tts = auto()
```

Providers declare their capabilities:
```python
# src/calibre/ai/google/__init__.py
@property
def capabilities(self) -> AICapabilities:
    return (
        AICapabilities.text_to_text |
        AICapabilities.embedding |   # Google supports embeddings
        AICapabilities.tts
    )
```

## Adding Embedding Support

### Google Backend

Gemini models with `'embedContent'` in `supportedGenerationMethods` support embeddings.

```python
# src/calibre/ai/google/backend.py

# Embedding endpoint
EMBED_URL = f'{API_BASE_URL}/{{model}}:embedContent'

def embed(
    texts: list[str],
    model: str = 'models/text-embedding-004',
    dimensions: int = 768,
    task_type: str = 'SEMANTIC_SIMILARITY',
) -> list[list[float]]:
    """Generate embeddings using Gemini API.

    Args:
        texts: List of texts to embed
        model: Embedding model ID
        dimensions: Output dimensions (256, 768, or 3072)
        task_type: One of RETRIEVAL_QUERY, RETRIEVAL_DOCUMENT,
                   SEMANTIC_SIMILARITY, CLASSIFICATION, CLUSTERING

    Returns:
        List of embedding vectors

    See: https://ai.google.dev/gemini-api/docs/embeddings
    """
    api_key = decoded_api_key()

    results = []
    for text in texts:
        data = {
            'model': model,
            'content': {'parts': [{'text': text}]},
            'outputDimensionality': dimensions,
            'taskType': task_type,
        }

        url = EMBED_URL.format(model=model)
        headers = {
            'X-goog-api-key': api_key,
            'Content-Type': 'application/json',
        }

        req = Request(url, data=json.dumps(data).encode(), headers=headers)
        with urlopen(req) as response:
            result = json.loads(response.read())
            results.append(result['embedding']['values'])

    return results


def embed_batch(
    texts: list[str],
    model: str = 'models/text-embedding-004',
    dimensions: int = 768,
) -> list[list[float]]:
    """Batch embed multiple texts in one API call.

    See: https://ai.google.dev/gemini-api/docs/embeddings#batch
    """
    api_key = decoded_api_key()

    url = f'{API_BASE_URL}/{model}:batchEmbedContents'
    data = {
        'requests': [
            {
                'model': model,
                'content': {'parts': [{'text': text}]},
                'outputDimensionality': dimensions,
            }
            for text in texts
        ]
    }

    headers = {
        'X-goog-api-key': api_key,
        'Content-Type': 'application/json',
    }

    req = Request(url, data=json.dumps(data).encode(), headers=headers)
    with urlopen(req) as response:
        result = json.loads(response.read())
        return [e['values'] for e in result['embeddings']]
```

### OpenAI Backend

```python
# src/calibre/ai/openai/backend.py

def embed(
    texts: list[str],
    model: str = 'text-embedding-3-small',
    dimensions: int | None = None,
) -> list[list[float]]:
    """Generate embeddings using OpenAI API.

    Args:
        texts: List of texts to embed
        model: Embedding model (text-embedding-3-small, text-embedding-3-large)
        dimensions: Optional dimension reduction (for -3- models)

    Returns:
        List of embedding vectors
    """
    api_key = decoded_api_key()

    data = {
        'input': texts,
        'model': model,
    }
    if dimensions:
        data['dimensions'] = dimensions

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }

    req = Request(
        'https://api.openai.com/v1/embeddings',
        data=json.dumps(data).encode(),
        headers=headers,
    )

    with urlopen(req) as response:
        result = json.loads(response.read())
        # Sort by index to maintain order
        embeddings = sorted(result['data'], key=lambda x: x['index'])
        return [e['embedding'] for e in embeddings]
```

## CalibreAIAdapter Bridge

Our library uses a thin adapter to access Calibre's AI:

```python
# semantic-search/calibre_semantic/providers/embeddings/calibre_ai.py

class CalibreAIAdapter:
    """Bridges calibre_semantic to Calibre's AI module."""

    def __init__(self, provider: str = 'google', model: str = '', dimensions: int = 768):
        self._provider = provider
        self._model = model
        self._dimensions = dimensions
        self._embed_func = None
        self._init_provider()

    def _init_provider(self) -> None:
        """Initialize the appropriate Calibre AI backend."""
        try:
            if self._provider == 'google':
                from calibre.ai.google.backend import embed, is_ready_for_use
                if is_ready_for_use():
                    self._embed_func = embed
                    self._model = self._model or 'models/text-embedding-004'
            elif self._provider == 'openai':
                from calibre.ai.openai.backend import embed, is_ready_for_use
                if is_ready_for_use():
                    self._embed_func = embed
                    self._model = self._model or 'text-embedding-3-small'
        except ImportError:
            pass  # Calibre AI not available

        if not self._embed_func:
            self._init_fallback()

    def embed(self, texts: list[str]) -> list[Vector]:
        """Generate embeddings using Calibre AI or fallback."""
        if self._embed_func:
            raw = self._embed_func(texts, self._model, self._dimensions)
            return [np.array(v, dtype=np.float32) for v in raw]
        elif self._fallback:
            return self._fallback.embed(texts)
        else:
            raise RuntimeError("No embedding provider available")
```

## Provider Selection

Users configure their preferred AI provider in Calibre's preferences:

```
Preferences → Sharing → Ask AI → Provider: [Google ▼]
                              → API Key: [••••••••••]
```

We can query the active provider:

```python
from calibre.ai.prefs import plugin_for_purpose
from calibre.ai import AICapabilities

# Get provider configured for embeddings
provider = plugin_for_purpose(AICapabilities.embedding)
if provider:
    print(f"Using {provider.name} for embeddings")
```

## Embedding Models

### Google Gemini

| Model | Dimensions | Max Tokens | Notes |
|-------|-----------|------------|-------|
| text-embedding-004 | 256/768/3072 | 2048 | Latest, best quality |
| embedding-001 | 768 | 2048 | Legacy |

Task types:
- `RETRIEVAL_QUERY` - For search queries
- `RETRIEVAL_DOCUMENT` - For documents being searched
- `SEMANTIC_SIMILARITY` - General similarity (default)

### OpenAI

| Model | Dimensions | Max Tokens | Notes |
|-------|-----------|------------|-------|
| text-embedding-3-large | 256-3072 | 8191 | Best quality |
| text-embedding-3-small | 512-1536 | 8191 | Good balance |
| text-embedding-ada-002 | 1536 | 8191 | Legacy |

## Fallback Chain

When Calibre AI is unavailable:

```
1. Try Calibre AI (user's configured provider)
   ↓ (ImportError or not configured)
2. Try sentence-transformers (local)
   ↓ (not installed)
3. Raise RuntimeError with installation instructions
```

## Testing Without Calibre

For standalone testing of `calibre_semantic`:

```python
from calibre_semantic.core.types import EmbeddingConfig
from calibre_semantic.core.embeddings import create_embedding_provider

# Use local embeddings directly (no Calibre needed)
config = EmbeddingConfig(
    provider='sentence-transformers',
    model='all-MiniLM-L6-v2',
)
provider = create_embedding_provider(config)
embeddings = provider.embed(['test text'])
```

## API Rate Limits

| Provider | Requests/min | Tokens/min |
|----------|-------------|------------|
| Google Gemini (free) | 60 | 1M |
| Google Gemini (paid) | 1000 | 4M |
| OpenAI | 3000 | 1M |

Our embedding code should:
1. Batch requests when possible (reduce API calls)
2. Respect rate limits with exponential backoff
3. Report progress for large indexing operations

## See Also

- [ISSUES.md](ISSUES.md) - DD-003 for design decision rationale
- [Gemini Embeddings Docs](https://ai.google.dev/gemini-api/docs/embeddings)
- [OpenAI Embeddings Docs](https://platform.openai.com/docs/guides/embeddings)
