# ADR-005: Vector Index Strategies

**Date:** 2025-01-26
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

1. **Default to "flat"** for simplicity - most personal libraries are small enough
2. **Expose strategy in profile configuration** for advanced users
3. **sqlite-vec uses flat** by default
4. **FAISS backend** provides HNSW/IVF when needed

```python
@dataclass
class EmbeddingProfile:
    # ...
    index_strategy: str = "flat"  # "flat", "hnsw", "ivf"
    index_options: dict = field(default_factory=dict)
    # HNSW options: hnsw_m, hnsw_ef_construction, hnsw_ef_search
    # IVF options: ivf_nlist, ivf_nprobe
```

## Consequences

### Positive
- Simple default experience for most users
- Power users can optimize for their scale
- No premature optimization

### Negative
- Users with large libraries need to know to switch strategies
- FAISS adds another optional dependency
- Strategy change requires re-indexing

### Neutral
- Most Calibre users have <10k books (flat is fine)
- Documentation should include scaling guidance

## Implementation Notes

Current implementations:
- `InMemoryVectorStore`: Flat (numpy dot product)
- `SQLiteVecStore`: Flat (sqlite-vec cosine distance)

Future:
- `FAISSStore`: HNSW, IVF, with optional quantization

Threshold guidance (to document for users):
- <10k chunks: Flat is fine (<100ms search)
- 10k-100k chunks: Consider HNSW
- >100k chunks: Strongly recommend HNSW or IVF

## Related Decisions
- [ADR-001](001-embedding-profiles.md): Strategy is per-profile
