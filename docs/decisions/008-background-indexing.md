# ADR-008: Background Indexing Architecture

**Date:** 2025-12-03
**Status:** Accepted
**Deciders:** Project maintainers

## Context

Library semantic search requires indexing books before they're searchable. For large libraries or bulk operations, this must happen in the background without freezing the UI.

### Problem Statement

- Indexing a single book takes 5-30 seconds (depending on size and embedding provider)
- Bulk indexing 100+ books would take hours
- UI must remain responsive during indexing
- Users need progress feedback and cancellation ability
- Errors on individual books shouldn't abort entire batch
- Cloud embedding APIs have rate limits and costs

### Calibre's Threading Model

Calibre uses:
- **Qt's threading**: `QThread`, signals/slots for UI updates
- **Calibre's job system**: `calibre.gui2.threaded_jobs` for long operations
- **Progress dialogs**: Standard pattern for showing job progress

## Decision

Use **Calibre's existing job system** with a custom `ThreadedJob` for semantic indexing:

### 1. Job Architecture

```python
# semantic-search/calibre_semantic/library.py
class IndexingJob:
    """Background indexing job for Calibre's job system."""

    def __init__(
        self,
        db: CalibreDB,
        book_ids: list[int],
        profile_id: str,
        engine: SemanticSearchEngine,
    ):
        self.db = db
        self.book_ids = book_ids
        self.profile_id = profile_id
        self.engine = engine
        self.cancelled = False
        self.results = IndexingResults()

    def run(self, progress_callback: Callable[[int, str], None]):
        """Called in background thread."""
        total = len(self.book_ids)
        for i, book_id in enumerate(self.book_ids):
            if self.cancelled:
                break
            try:
                title = self.db.get_title(book_id)
                progress_callback(i, f"Indexing: {title}")
                self.engine.index_book(book_id, self.profile_id)
                self.results.succeeded.append(book_id)
            except Exception as e:
                self.results.failed.append((book_id, str(e)))
        return self.results

    def cancel(self):
        self.cancelled = True
```

### 2. Integration with Calibre's Job Dialog

```python
# src/calibre/gui2/dialogs/semantic_search.py
from calibre.gui2.threaded_jobs import ThreadedJob

class IndexSelectedBooksJob(ThreadedJob):
    def __init__(self, gui, book_ids, profile_id):
        self.gui = gui
        self.book_ids = book_ids
        self.profile_id = profile_id
        ThreadedJob.__init__(
            self,
            'index_semantic',
            _('Indexing for semantic search'),
            lambda job: self._finished(job),
            lambda job: self._progress(job),
        )

    def work(self):
        from calibre_semantic.library import IndexingJob
        job = IndexingJob(
            db=self.gui.current_db.new_api,
            book_ids=self.book_ids,
            profile_id=self.profile_id,
            engine=get_semantic_engine(),
        )
        return job.run(self.set_progress)

    def _finished(self, job):
        if job.failed:
            error_dialog(self.gui, _('Indexing Failed'), job.details)
        else:
            results = job.result
            info_dialog(
                self.gui,
                _('Indexing Complete'),
                _('{} books indexed, {} failed').format(
                    len(results.succeeded), len(results.failed)
                )
            )
```

### 3. Progress Reporting

```
┌──────────────────────────────────────────────┐
│ Semantic Indexing                     [X]    │
├──────────────────────────────────────────────┤
│                                              │
│ Indexing: Being and Time                     │
│ [████████████░░░░░░░░░░░░░░░] 42%           │
│                                              │
│ 42 of 100 books processed                    │
│ 2 failed (will be listed at end)             │
│                                              │
│ Estimated time remaining: 12 minutes         │
│                                              │
│                    [Cancel]                  │
└──────────────────────────────────────────────┘
```

### 4. Error Handling Strategy

| Error Type | Action | User Feedback |
|------------|--------|---------------|
| **API Rate Limit** | Pause, retry with backoff | "Waiting for API rate limit..." |
| **API Key Invalid** | Abort entire job | Error dialog with setup instructions |
| **Book Extraction Failed** | Skip book, continue | Add to failed list |
| **Network Error** | Retry 3 times, then skip | "Network error, retrying..." |
| **Cancelled** | Stop gracefully | "Cancelled. X books indexed." |

### 5. Rate Limiting for Cloud APIs

```python
class RateLimitedEngine:
    """Wrapper that respects API rate limits."""

    def __init__(self, engine: SemanticSearchEngine, rpm: int = 60):
        self.engine = engine
        self.min_interval = 60.0 / rpm  # seconds between requests
        self.last_request = 0

    async def index_book(self, book_id: int, profile_id: str):
        elapsed = time.time() - self.last_request
        if elapsed < self.min_interval:
            await asyncio.sleep(self.min_interval - elapsed)
        self.last_request = time.time()
        return self.engine.index_book(book_id, profile_id)
```

## Consequences

### Positive
- **Responsive UI**: Background processing doesn't freeze Calibre
- **Familiar UX**: Uses Calibre's standard job dialog pattern
- **Resilient**: Individual failures don't abort batch
- **Cancellable**: Users can stop long operations
- **Cost-aware**: Rate limiting protects against API overuse

### Negative
- **Complexity**: More code than synchronous indexing
- **State management**: Need to track job state across UI updates
- **Testing**: Background jobs harder to test than synchronous

### Neutral
- Progress granularity is per-book (not per-chunk)
- Calibre's job system handles thread lifecycle

## Implementation Notes

### Index Status Tracking

Per [ADR-002](002-on-demand-indexing.md), track indexing status:

```python
class IndexStatus(Enum):
    NOT_INDEXED = "not_indexed"
    INDEXING = "indexing"
    COMPLETE = "complete"
    FAILED = "failed"

# Store in ChromaDB metadata or separate SQLite table
profiles_db.update_book_status(book_id, profile_id, IndexStatus.COMPLETE)
```

### Re-indexing Strategy

When a book needs re-indexing (content changed, profile updated):

1. Mark as `INDEXING`
2. Remove old chunks from vector store
3. Re-extract and embed
4. Update to `COMPLETE` or `FAILED`

### Batch Size Optimization

```python
# For very large operations, process in batches
BATCH_SIZE = 10  # Commit to DB after each batch

for batch in chunked(book_ids, BATCH_SIZE):
    for book_id in batch:
        index_single_book(book_id)
    commit_batch()  # Periodic commits for crash recovery
```

## Related Decisions

- [ADR-002](002-on-demand-indexing.md): On-demand indexing philosophy
- [ADR-007](007-library-ui-integration.md): UI integration for indexing actions
- [ADR-006](006-hybrid-metadata-filtering.md): ChromaDB storage for indexed chunks

## Future Considerations

- **Queue persistence**: Save queue to disk for crash recovery
- **Priority scheduling**: Index frequently accessed books first
- **Incremental indexing**: Only re-index changed chapters
- **Cost estimation**: Show estimated API cost before bulk indexing
