# ADR-002: On-Demand Indexing (Not Auto-Index)

**Date:** 2025-01-26
**Status:** Accepted
**Deciders:** Project maintainers

## Context

Original design had `index_on_add: bool` configuration to automatically index new books when added to the library.

### Problem Statement

- Large libraries would consume significant compute resources
- Cloud embedding APIs cost money per token (e.g., Gemini, OpenAI)
- Users may only need semantic search for specific books/collections
- Auto-indexing doesn't know which profile to use
- No user control over resource expenditure

## Decision

Default to **on-demand indexing** with multiple user-initiated trigger points:

1. **Single book:** Right-click book → "Add to Semantic Index" → Select profile
2. **Viewer:** First semantic search triggers "Index this book first?"
3. **Bulk:** Select multiple books → "Index Selected..." → Choose profile
4. **Optional:** Dialog when adding books (user preference in settings)

The `index_on_add` setting can still exist but defaults to `False`.

## Consequences

### Positive
- Respects user resources (compute, API costs)
- User maintains explicit control
- Clear about what is and isn't indexed
- Works well with embedding profiles (user picks profile at index time)

### Negative
- Extra step required before first semantic search
- Users may forget to index books
- Need clear UI indication of "not indexed" state

### Neutral
- Background queue may still be useful for bulk operations
- Progress indication needed for indexing operations

## Implementation Notes

```python
class SemanticSearchEngine:
    def index_book(
        self,
        book_id: BookIdentifier,
        profile_id: str,
        on_progress: Callable[[IndexingProgress], None] | None = None,
    ) -> None:
        """Index a book into the specified profile."""
        ...

    def is_book_indexed(self, book_id: BookIdentifier, profile_id: str) -> bool:
        """Check if a book is indexed in a profile."""
        ...
```

UI should show indexing status:
- Not indexed: Gray icon, "Index for semantic search" action
- Indexing: Progress indicator
- Indexed: Checkmark, profile badge
