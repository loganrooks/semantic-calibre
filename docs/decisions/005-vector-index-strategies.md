# ADR-005: Vector Index Strategies

**Date:** 2025-01-26
**Updated:** 2025-12-03 (Phase 3: Added ChromaDB)
**Status:** Accepted
**Deciders:** Project maintainers

## Context

Different vector search algorithms have different performance characteristics. Users may have libraries ranging from dozens to millions of books.

### Options Considered

| Strategy | Best For | Search | Memory | Trade-offs |
|----------|----------|--------|--------|------------|
| **Flat** | <50k vectors | O(n) exact | Low | Simple, exact, but slow at scale |
| **HNSW** | 50k-10M vectors | O(log n) approx | High | Fast, but memory-heavy |
| **IVF** | >1M vectors | O(√n) approx | Medium | Needs training, good for huge collections |
| **Quantization** | Memory-limited | Varies | Very low | Can combine with above, lossy |

## Decision

### Phase 2 (Viewer Search): Flat/SQLite-vec
1. **Default to "flat"** for simplicity - single-book search is small
2. **sqlite-vec uses flat** - lightweight, embedded
3. Suitable for in-book search (hundreds to thousands of chunks per book)

### Phase 3 (Library Search): HNSW/ChromaDB
1. **ChromaDB as primary store** for library-wide search
2. **HNSW by default** - ChromaDB uses HNSW internally
3. **Metadata filtering support** - essential for hybrid queries ([ADR-006](006-hybrid-metadata-filtering.md))
4. **Profile-based collections** - each profile gets separate ChromaDB collection

```python
@dataclass
class EmbeddingProfile:
    # ...
    index_strategy: str = "hnsw"  # "flat", "hnsw"
    index_options: dict = field(default_factory=dict)
    # HNSW options: hnsw_space ("cosine", "l2", "ip")
    # ChromaDB handles M, ef_construction internally
```

### Store Selection by Use Case

| Use Case | Store | Strategy | Reason |
|----------|-------|----------|--------|
| Viewer (in-book) | SQLite-vec | Flat | Small scale, single file |
| Library (cross-book) | ChromaDB | HNSW | Scale, metadata filtering |
| Development/Testing | InMemory | Flat | No persistence needed |

## Consequences

### Positive
- Simple default experience for most users
- ChromaDB handles HNSW complexity automatically
- Metadata filtering built into library search
- Power users can tune HNSW parameters if needed

### Negative
- ChromaDB adds ~50MB dependency
- Two vector stores to maintain (sqlite-vec + ChromaDB)
- Strategy change still requires re-indexing

### Neutral
- Most Calibre users have <10k books (HNSW handles easily)
- ChromaDB is well-maintained, active project
- SQLite-vec remains for lightweight viewer use case

## Implementation Notes

Current implementations:
- `InMemoryVectorStore`: Flat (numpy dot product) - testing only
- `SQLiteVecStore`: Flat (sqlite-vec cosine distance) - viewer search
- `ChromaDBStore`: HNSW (ChromaDB built-in) - library search

Threshold guidance:
- <1k chunks (single book): SQLite-vec is fine
- 1k-1M chunks (library): ChromaDB HNSW handles well
- >1M chunks: Consider ChromaDB with quantization

### ChromaDB HNSW Configuration

ChromaDB's default HNSW settings work well for most cases:
```python
# Defaults (usually don't need to change)
# M = 16 (number of neighbors per layer)
# ef_construction = 100 (build-time accuracy)
# ef_search = 10 (query-time accuracy)
```

For very large collections or higher recall needs:
```python
collection = client.create_collection(
    name="semantic_library",
    metadata={
        "hnsw:space": "cosine",
        "hnsw:M": 32,  # More connections = higher recall, more memory
        "hnsw:construction_ef": 200,  # Higher = better index, slower build
    }
)
```

## Related Decisions
- [ADR-001](001-embedding-profiles.md): Strategy is per-profile
- [ADR-006](006-hybrid-metadata-filtering.md): ChromaDB for hybrid queries
