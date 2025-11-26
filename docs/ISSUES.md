# Issues & Decisions Index

This document indexes architectural decisions and known issues for the Semantic Calibre project.

---

## Architecture Decision Records (ADRs)

Detailed design decisions are stored in [`docs/decisions/`](decisions/).

| ID | Title | Status | Summary |
|----|-------|--------|---------|
| [ADR-001](decisions/001-embedding-profiles.md) | Embedding Profiles | Accepted | Support multiple embedding configurations instead of single global model. |
| [ADR-002](decisions/002-on-demand-indexing.md) | On-Demand Indexing | Accepted | Default to user-initiated indexing, not auto-index. Respects resources and costs. |
| [ADR-003](decisions/003-calibre-ai-integration.md) | Calibre AI Integration | Accepted | Extend Calibre's AI backends with `embed()` rather than parallel infrastructure. |
| [ADR-004](decisions/004-minimal-viewer-modification.md) | Minimal Viewer Mod | Accepted | Only modify `viewer/search.py`. All logic in our library. |
| [ADR-005](decisions/005-vector-index-strategies.md) | Vector Index Strategies | Accepted | Default to flat search, expose HNSW/IVF for large collections. |

### Creating New ADRs

1. Create file: `docs/decisions/NNN-your-decision.md`
2. Use format: Context → Decision → Consequences
3. Add to this index table
4. Link from relevant code/docs

---

## Known Issues

| ID | Title | Impact | Status |
|----|-------|--------|--------|
| KI-001 | sqlite-vec tests skipped in CI | Low | Open |
| KI-002 | SentenceTransformer tests require heavy deps | Low | Open |
| KI-003 | CalibreAIAdapter falls back silently | Medium | In Progress |

### KI-001: sqlite-vec Tests Skipped in CI

**Impact:** Low (tests pass locally)

sqlite-vec extension not installed in CI environment, causing 18 tests to skip.

**Workaround:** Run tests locally with `pip install sqlite-vec`.

### KI-002: SentenceTransformer Tests Require Heavy Dependencies

**Impact:** Low (tests skip gracefully)

Tests for local embedding require ~500MB sentence-transformers download.

**Workaround:** Tests skip when dependency missing. Run locally for full coverage.

### KI-003: CalibreAIAdapter Falls Back Silently

**Impact:** Medium
**Status:** In Progress (see [ADR-003](decisions/003-calibre-ai-integration.md))

When Calibre AI module not found, adapter falls back to sentence-transformers without clear indication to user.

**Fix:** Implementing proper Calibre AI integration per ADR-003.

---

## Future Considerations

Ideas under discussion (not yet ADRs):

| ID | Topic | Question |
|----|-------|----------|
| FC-001 | Cross-Library Search UI | Menu item vs toolbar button vs keyboard shortcut? |
| FC-002 | Embedding Cost Tracking | Should we track/display API costs? |
| FC-003 | Incremental Re-indexing | How to handle modified books? |

---

## Changelog

| Date | Change |
|------|--------|
| 2025-01-26 | Restructured to ADR format with separate decision files |
| 2025-01-26 | Initial document |
