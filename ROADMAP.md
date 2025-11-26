# Semantic Calibre Roadmap

## Vision

Enable semantic (meaning-based) search across Calibre e-book libraries, allowing users to find books and passages by concept rather than exact keywords.

---

## Phase 1: Core Library

**Goal:** Build the foundational `calibre_semantic` library with all core components.

### Completed

- [x] **Types & Protocols** (`core/types.py`)
  - BookIdentifier, TextChunk, EmbeddedChunk
  - EmbeddingProvider protocol
  - VectorStore protocol
  - Configuration dataclasses

- [x] **Embedding Providers** (`core/embeddings.py`, `providers/embeddings/`)
  - BaseEmbeddingProvider abstract class
  - SentenceTransformerProvider (local)
  - Provider registry and factory
  - CalibreAIAdapter (bridges Calibre's AI module)

- [x] **Vector Stores** (`core/vectordb.py`, `providers/vectordb/`)
  - InMemoryVectorStore (development/testing)
  - SQLiteVecStore (production persistence)
  - Store registry and factory

- [x] **Chunking Strategies** (`core/chunking.py`)
  - SemanticChunkingStrategy (respects boundaries)
  - FixedSizeChunkingStrategy (simple overlap)
  - Factory function

- [x] **SemanticSearchEngine** (`search.py`)
  - Orchestrates embedding + chunking + storage
  - Index management (add, remove, check)
  - Search with filters (book, library, score)

### In Progress

- [ ] **Book Content Extraction**
  - EPUB text extraction (parse spine, strip HTML)
  - PDF text extraction (optional)
  - Metadata extraction from Calibre DB

### Planned

- [ ] **MCP Server** (`mcp/`)
  - Expose search as MCP tools
  - Index management tools
  - Configuration tools

- [ ] **CLI Tool**
  - `calibre-semantic index <library>`
  - `calibre-semantic search <query>`
  - `calibre-semantic status`

---

## Phase 2: Calibre Plugin

**Goal:** Create an installable Calibre plugin for cross-library semantic search.

### Planned

- [ ] **Plugin Skeleton**
  - InterfaceActionBase implementation
  - Plugin metadata and packaging

- [ ] **Search Dialog UI**
  - Qt-based search interface
  - Result display with book covers
  - Navigation to results in library view

- [ ] **Background Indexer**
  - Index books on library open
  - Incremental indexing (new books only)
  - Progress reporting

- [ ] **Configuration Panel**
  - Embedding model selection
  - Vector store location
  - Indexing preferences

---

## Phase 3: Viewer Integration

**Goal:** Add semantic search mode to Calibre's e-book viewer.

### Planned

- [ ] **Viewer Search Patch**
  - Add "Semantic" to search mode dropdown
  - Integrate with viewer's search infrastructure

- [ ] **In-Book Indexing**
  - Index current book on open
  - Cache embeddings for reopened books

- [ ] **Result Navigation**
  - Jump to semantic matches in book
  - Highlight relevant passages

---

## Phase 4: Advanced Features (Future)

- [ ] **Multi-model Support**
  - Compare results from different models
  - Model performance benchmarking

- [ ] **Semantic Recommendations**
  - "Books similar to this"
  - "More like this passage"

- [ ] **Cross-language Search**
  - Search in English, find results in other languages
  - Multi-lingual embedding models

- [ ] **Cloud Sync**
  - Sync embeddings across devices
  - Shared library search

---

## Technical Debt & Maintenance

### Known Issues
- SQLite-vec tests skipped (dependency not installed in CI)
- SentenceTransformer tests skipped (heavy dependency)

### Maintenance Tasks
- [ ] Set up CI/CD with GitHub Actions
- [ ] Add type checking with mypy
- [ ] Add code coverage reporting
- [ ] Automate upstream sync checks

---

## Contributing

See CLAUDE.md for development conventions and FORK_MAINTENANCE.md for working with the Calibre fork.

### Priority for Contributors
1. Book content extraction (Phase 1 blocker)
2. MCP server (enables AI integration)
3. Plugin skeleton (enables user testing)
