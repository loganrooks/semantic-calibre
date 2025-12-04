# ADR-006: Hybrid Metadata Filtering (Calibre DB + Vector Store)

**Date:** 2025-12-01
**Status:** Accepted
**Deciders:** Project maintainers

## Context

Users need to filter semantic search results by book metadata:
- Built-in fields: authors, tags, series, publisher, language, rating, pubdate
- Custom columns: user-defined fields like `#tradition`, `#course`, `#reading_status`

### Problem Statement

With potentially millions of embeddings (1-2k chunks per book × thousands of books), metadata filtering is essential for:
- Scoping searches to specific collections (e.g., "phenomenology books only")
- Course-specific searching (e.g., "PHIL-401 readings")
- Author/tradition filtering (e.g., "continental philosophy")
- Combining semantic similarity with categorical constraints

### Options Considered

| Option | Description | Pros | Cons |
|--------|-------------|------|------|
| **A: Sync to Vector Store** | Copy all metadata to ChromaDB | Fast queries, single data source | Sync complexity, drift risk |
| **B: Hybrid Query** | Filter in Calibre DB, then vector search | No sync needed, DB is source of truth | Two-step query |
| **C: Full Metadata Copy** | Store complete metadata with each chunk | Maximum flexibility | Storage bloat, sync on every edit |

## Decision

Implement **Hybrid Query Architecture** (Option B):

```
┌─────────────────────────┐      ┌─────────────────────────┐
│     Calibre DB          │      │     Vector Store        │
│     (SQLite)            │      │     (ChromaDB)          │
│                         │      │                         │
│  Source of Truth:       │      │  Stores only:           │
│  - books                │      │  - book_id (reference)  │
│  - metadata             │◄────►│  - chunk_id             │
│  - tags                 │ join │  - embeddings           │
│  - custom columns (#*)  │      │  - chunk_text           │
│  - identifiers          │      │  - location_info        │
└─────────────────────────┘      └─────────────────────────┘
```

### Query Flow

```python
def search_with_metadata_filter(
    query: str,
    filters: dict,  # {"authors": ["Heidegger"], "#tradition": "continental"}
    profile_id: str,
    top_k: int = 20
) -> list[SearchResult]:

    # Step 1: Filter books in Calibre DB (fast, indexed)
    matching_book_ids = calibre_db.search(
        'author:"Heidegger" and #tradition:"continental"'
    )

    # Step 2: Semantic search scoped to matching books
    results = vector_store.query(
        query_embedding=embed(query),
        where={"book_id": {"$in": matching_book_ids}},
        n_results=top_k
    )

    # Step 3: Enrich results with full metadata
    return enrich_with_metadata(results, calibre_db)
```

### Calibre Metadata Available for Filtering

**Built-in Fields:**
| Field | Type | Example Filter |
|-------|------|----------------|
| `authors` | text (multi) | `author:Heidegger` |
| `tags` | text (multi) | `tag:phenomenology` |
| `series` | text | `series:"Being and Time"` |
| `publisher` | text | `publisher:"MIT Press"` |
| `languages` | text (multi) | `language:eng` |
| `rating` | int (0-10) | `rating:>8` |
| `pubdate` | datetime | `pubdate:>2020` |
| `formats` | text (multi) | `format:EPUB` |
| `identifiers` | text (multi) | `identifier:isbn:...` |

**Custom Columns (User-Defined):**
| Type | Use Case | Example |
|------|----------|---------|
| `enumeration` | Tradition, Status | `#tradition:continental` |
| `text` | Course codes | `#course:PHIL-401` |
| `bool` | Flags | `#is_primary:true` |
| `rating` | Quality scores | `#importance:>6` |
| `datetime` | Read dates | `#date_read:>2024` |

Custom columns are prefixed with `#` in Calibre's search syntax.

## Consequences

### Positive
- **No sync complexity**: Calibre DB is single source of truth for metadata
- **Custom columns work automatically**: Any user-defined column is immediately filterable
- **Leverages Calibre's search**: Reuses battle-tested search parser and indexes
- **Fork maintenance**: Minimal changes to Calibre codebase
- **Consistency**: Metadata edits in Calibre are instantly reflected

### Negative
- **Two-step query**: Slightly more complex query execution
- **Large result sets**: If metadata filter matches many books, vector query is broader
- **No combined ranking**: Can't easily blend metadata relevance with semantic similarity

### Neutral
- Vector store only needs `book_id` in metadata (minimal storage overhead)
- Query performance depends on metadata filter selectivity
- UI must expose Calibre's search syntax or provide filter builder

## Implementation Notes

### Vector Store Schema (ChromaDB)

```python
# When indexing a chunk:
collection.add(
    ids=[chunk_id],
    embeddings=[vector],
    metadatas=[{
        "book_id": 123,           # Required: links to Calibre DB
        "chunk_index": 5,         # For ordering
        "location": "chapter:3",  # For navigation
        # NO metadata copied - query Calibre DB instead
    }],
    documents=[chunk_text]        # Optional: for retrieval
)
```

### Filter Translation Layer

```python
class MetadataFilterBuilder:
    """Translates UI filters to Calibre search syntax."""

    def build_query(self, filters: dict) -> str:
        parts = []
        for field, value in filters.items():
            if field.startswith('#'):
                # Custom column
                parts.append(f'{field}:"{value}"')
            elif field == 'authors':
                parts.append(f'author:"{value}"')
            elif field == 'tags':
                if isinstance(value, list):
                    parts.append(' or '.join(f'tag:"{v}"' for v in value))
                else:
                    parts.append(f'tag:"{value}"')
            # ... more field mappings
        return ' and '.join(parts)
```

### Integration with SemanticSearchEngine

```python
class SemanticSearchEngine:
    def search(
        self,
        query: str,
        profile_id: str | None = None,
        top_k: int = 10,
        min_score: float = 0.0,
        book_ids: list[int] | None = None,      # Existing
        metadata_filter: dict | None = None,     # NEW
        calibre_db: CalibreDB | None = None,     # NEW: for filter resolution
    ) -> SearchResults:
        # Resolve metadata filter to book_ids
        if metadata_filter and calibre_db:
            filter_query = self._build_filter_query(metadata_filter)
            filtered_ids = calibre_db.search(filter_query)
            book_ids = self._intersect(book_ids, filtered_ids)

        # Existing vector search with book_ids constraint
        return self._vector_search(query, profile_id, top_k, min_score, book_ids)
```

## Related Decisions

- [ADR-001](001-embedding-profiles.md): Profiles define which vector store to query
- [ADR-002](002-on-demand-indexing.md): Books must be indexed before searchable
- [ADR-005](005-vector-index-strategies.md): ChromaDB uses HNSW for efficient search at scale

## Future Considerations

- **Caching**: Cache frequent metadata filter → book_ids mappings
- **Combined ranking**: Future ADR for blending metadata and semantic scores
- **Saved filters**: Allow users to save common filter combinations
- **Smart defaults**: Auto-suggest filters based on user's library organization
