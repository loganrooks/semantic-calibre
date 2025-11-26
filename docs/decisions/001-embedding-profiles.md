# ADR-001: Embedding Profiles (Not Single Global Model)

**Date:** 2025-01-26
**Status:** Accepted
**Deciders:** Project maintainers

## Context

Originally, the system stored a single `model_id` globally in the vector store. This assumed all books would use the same embedding model.

### Problem Statement

Users have different needs:
- Some want fast local embeddings (sentence-transformers)
- Some want high-quality cloud embeddings (Gemini, OpenAI)
- Researchers may want specific models for specific collections

Additionally:
- Embeddings from different providers are **not interoperable** (Gemini vectors cannot be compared with OpenAI vectors, even at the same dimensionality)
- No way to track which books were indexed with which model
- Changing models required full re-index of entire library

## Decision

Implement **Embedding Profiles** - named configurations that group:

```python
@dataclass
class EmbeddingProfile:
    id: str                  # "philosophy-gemini-768"
    name: str                # "Philosophy Research"
    provider: str            # "gemini", "openai", "sentence-transformers"
    model: str               # "text-embedding-004"
    dimension: int           # 768
    index_strategy: str      # "flat", "hnsw", "ivf"
    index_options: dict      # Strategy-specific parameters
    created_at: datetime
```

Each profile maintains its own vector space. Books can belong to multiple profiles.

## Consequences

### Positive
- Users can have multiple embedding configurations
- Clear separation between incompatible vector spaces
- Flexibility for different use cases (research vs. general browsing)
- Can index same book with different models for comparison

### Negative
- More complex data model
- UI needs profile selector
- Database schema requires additional tables
- Storage increases if same book is in multiple profiles

### Neutral
- Search is scoped to a single profile (no cross-profile search)
- Migration path needed for existing single-model indexes

## Implementation Notes

Database schema additions:
```sql
CREATE TABLE embedding_profiles (...);
CREATE TABLE book_index_status (...);
```

See [CALIBRE_AI.md](../CALIBRE_AI.md) for provider integration details.
