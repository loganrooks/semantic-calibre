# calibre-semantic

Semantic search library for Calibre e-book manager.

## Installation

```bash
# Core library (numpy only)
pip install -e .

# With local embeddings (recommended)
pip install -e ".[sentence-transformers]"

# With persistent storage
pip install -e ".[sqlite-vec]"

# All optional dependencies
pip install -e ".[all]"
```

## Quick Start

```python
from calibre_semantic import (
    SemanticSearchEngine,
    SemanticSearchConfig,
    BookIdentifier,
)

# Create engine with default config
config = SemanticSearchConfig()
engine = SemanticSearchEngine(config)

# Index some text
book_id = BookIdentifier("my-library", 1, "EPUB")
engine.index_text(
    text="Machine learning is transforming how we process data...",
    book_id=book_id,
    spine_index=0,
    spine_name="chapter1.xhtml",
    chapter_title="Introduction",
)

# Search
results = engine.search("artificial intelligence applications")
for result in results.results:
    print(f"Score: {result.score:.2f}")
    print(f"Text: {result.chunk.text[:100]}...")
    print(f"Location: {result.chunk.location.spine_name}")
    print()
```

## Configuration

```python
from calibre_semantic import SemanticSearchConfig
from calibre_semantic.core import (
    EmbeddingConfig,
    VectorStoreConfig,
    ChunkingConfig,
)

config = SemanticSearchConfig(
    # Embedding settings
    embedding=EmbeddingConfig(
        provider="sentence-transformers",  # or "openai", "ollama"
        model="all-MiniLM-L6-v2",
        device="auto",  # "cpu", "cuda", "mps"
        batch_size=32,
    ),

    # Vector store settings
    vector_store=VectorStoreConfig(
        backend="sqlite-vec",  # or "memory"
        path=Path("./semantic_index.db"),
    ),

    # Chunking settings
    chunking=ChunkingConfig(
        strategy="semantic",  # or "fixed"
        target_size=512,
        overlap=64,
        respect_boundaries=True,
    ),

    # Search settings
    default_result_limit=20,
    min_similarity_score=0.3,
)
```

## Components

### Embedding Providers

| Provider | Description | Install |
|----------|-------------|---------|
| `sentence-transformers` | Local models (default) | `pip install sentence-transformers` |
| `openai` | OpenAI API | `pip install openai` |
| `ollama` | Local Ollama server | Ollama running locally |
| `calibre-ai` | Calibre's built-in AI | Calibre with AI support |

### Vector Stores

| Backend | Description | Install |
|---------|-------------|---------|
| `memory` | In-memory (development) | Built-in |
| `sqlite-vec` | SQLite with vector extension | `pip install sqlite-vec` |

### Chunking Strategies

| Strategy | Description |
|----------|-------------|
| `semantic` | Respects paragraph/sentence boundaries |
| `fixed` | Fixed-size chunks with overlap |

## API Reference

### SemanticSearchEngine

```python
# Indexing
engine.index_text(text, book_id, spine_index, spine_name, chapter_title=None)
engine.index_book_content(book_id, spine_items, chapter_titles=None)

# Searching
results = engine.search(
    query,
    limit=20,
    filter_book_ids=None,
    filter_libraries=None,
    min_score=0.3,
)

# Management
engine.is_indexed(book_id) -> bool
engine.remove_book(book_id) -> int
engine.get_indexed_books() -> set[BookIdentifier]
engine.get_stats() -> dict
engine.clear()
```

### SearchResults

```python
results.query          # Original query string
results.results        # List of SearchResult
results.total_searched # Total chunks searched
results.search_time_ms # Search duration
results.model_id       # Embedding model used

# Each SearchResult
result.chunk           # TextChunk with text and location
result.score           # Similarity score (0-1)
result.highlights      # Optional highlight offsets
```

## Development

```bash
# Run tests
python -m pytest tests/ -v

# Run specific tests
python -m pytest tests/test_chunking.py -v

# Run with coverage
python -m pytest tests/ --cov=calibre_semantic
```

## License

Same as Calibre (GPL v3).
