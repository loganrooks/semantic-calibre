# ADR-004: Minimal Viewer Modification

**Date:** 2025-01-26
**Status:** Accepted
**Deciders:** Project maintainers

## Context

Calibre's e-book viewer has existing search functionality with:
- Multiple search modes (normal, word, regex)
- Complex JavaScript + Python interaction
- Sidebar with grouped results
- Navigation to matches

We want to add semantic search to the viewer.

### Problem Statement

- Modifying Calibre source creates merge conflicts on upstream sync
- Viewer search has intricate state management
- We need to maintain this fork long-term
- Extensive modifications increase maintenance burden

## Decision

**Only modify `src/calibre/gui2/viewer/search.py`**:
- Add "Semantic" to search mode dropdown
- Delegate all semantic logic to `calibre_semantic` library
- Keep result format compatible with existing viewer infrastructure

All semantic search complexity lives in our library, not Calibre source.

## Consequences

### Positive
- Single file to review during upstream syncs
- Easy to test semantic search logic independently
- Clear boundary between Calibre and our code
- Reduced merge conflict surface

### Negative
- May not leverage all viewer features
- Need to carefully bridge data formats
- Some UI limitations (can't deeply customize viewer)

### Neutral
- Plugin system could be alternative approach
- Viewer's search infrastructure is fairly stable

## Implementation Notes

Modification to `search.py`:

```python
# Add to SearchInput.__init__
self.query_type.addItem(_('Semantic'), 'semantic')

# Add handler in search dispatch
elif search_query.mode == 'semantic':
    from calibre_semantic import search_viewer_book
    results = search_viewer_book(
        book_path=self.current_book_path,
        query=search_query.text,
        profile_id=self.semantic_profile,
    )
    # Convert to viewer's SearchResult format
```

## Related Decisions
- [ADR-003](003-calibre-ai-integration.md): AI integration approach
- See [FORK_MAINTENANCE.md](../../FORK_MAINTENANCE.md) for sync procedures
