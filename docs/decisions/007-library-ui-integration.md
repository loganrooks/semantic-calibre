# ADR-007: Library UI Integration Strategy

**Date:** 2025-12-03
**Status:** Accepted
**Deciders:** Project maintainers

## Context

Phase 3 adds semantic search to Calibre's main library interface. Unlike Phase 2 (viewer), this requires multiple UI touchpoints:
- Menu items for search dialog
- Right-click context menu actions
- Profile management interface
- Search results display
- Indexing progress dialogs

### Problem Statement

- Library UI is more complex than viewer (many files, interdependencies)
- Need to minimize fork divergence for upstream sync compatibility
- Must integrate naturally with Calibre's existing GUI patterns
- Should support both single-book and bulk operations

### Calibre GUI Architecture

Calibre's main GUI (`src/calibre/gui2/`) follows these patterns:
- **Actions**: Menu/toolbar items in `actions/` directory (subclass `InterfaceAction`)
- **Dialogs**: Modal dialogs in `dialogs/` directory (subclass `QDialog`)
- **Preferences**: Settings in `preferences/` directory
- **Library model**: Book data access via `library/`

## Decision

Follow a **minimal modification strategy** similar to [ADR-004](004-minimal-viewer-modification.md):

### 1. New Files (No Modification Required)

Create new files in appropriate Calibre directories:

```
src/calibre/gui2/
├── actions/
│   └── semantic_search.py     # NEW: InterfaceAction for menu items
├── dialogs/
│   ├── semantic_search.py     # NEW: Main search dialog
│   └── profile_manager.py     # NEW: Profile CRUD dialog
└── preferences/
    └── semantic_search.py     # NEW: Settings page (optional)
```

### 2. Minimal Modifications

**Modified Files (ideally ≤3):**

| File | Modification | Purpose |
|------|--------------|---------|
| `gui2/actions/__init__.py` | Add import | Register SemanticSearchAction |
| `gui2/init.py` or similar | Add initialization | Initialize semantic search on startup |
| `gui2/library/views.py` | Add context menu | Right-click "Add to Semantic Index" |

### 3. Integration Pattern

```python
# actions/semantic_search.py
class SemanticSearchAction(InterfaceAction):
    name = 'Semantic Search'
    action_spec = (_('Semantic Search'), 'search.png', _('Search by meaning'), 'Ctrl+Shift+S')

    def genesis(self):
        """Called when plugin initialized."""
        self.menu = QMenu(self.gui)
        self.create_menu_action(...)

    def library_search(self):
        """Show library search dialog."""
        from calibre.gui2.dialogs.semantic_search import SemanticSearchDialog
        dialog = SemanticSearchDialog(self.gui, self.gui.current_db)
        dialog.exec_()
```

### 4. Delegation to calibre_semantic

All complex logic lives in our library:

```python
# In dialog code
from calibre_semantic.library import (
    LibrarySearchEngine,  # Orchestrates Calibre DB + ChromaDB
    ProfileManager,       # Profile CRUD
    IndexManager,         # Indexing operations
)
```

## Consequences

### Positive
- **Easy upstream sync**: Only 2-3 modified files to review
- **Clear boundaries**: All semantic logic in calibre_semantic library
- **Natural integration**: Uses Calibre's existing action/dialog patterns
- **Testable**: Library components can be tested independently

### Negative
- **Some duplication**: May need to bridge data formats
- **Discovery challenge**: Users need to find the new menu items
- **Limited customization**: Can't deeply modify existing dialogs

### Neutral
- New files in Calibre's directories (no modification, but adds to fork)
- Action system handles keyboard shortcuts naturally

## Implementation Notes

### Phase 3 File List

**New Files to Create:**
1. `src/calibre/gui2/actions/semantic_search.py` - Menu action
2. `src/calibre/gui2/dialogs/semantic_search.py` - Search dialog
3. `src/calibre/gui2/dialogs/semantic_profile_manager.py` - Profile manager
4. `semantic-search/calibre_semantic/library.py` - Library integration API

**Files to Modify (Keep Minimal):**
1. `src/calibre/gui2/actions/__init__.py` - Register action
2. `src/calibre/gui2/library/views.py` - Context menu item

### Context Menu Integration

```python
# In views.py, add to context menu:
if semantic_search_available():
    menu.addAction(
        _('Add to Semantic Index...'),
        self.semantic_index_selected
    )
```

### Dialog Layout (Search)

```
┌─────────────────────────────────────────────────────┐
│ Semantic Search                              [X]    │
├─────────────────────────────────────────────────────┤
│ Query: [________________________] [🔍 Search]       │
│                                                     │
│ Profile: [Philosophy Research    ▼]                 │
│                                                     │
│ ▼ Metadata Filters                                  │
│   Authors: [________________________]               │
│   Tags:    [________________________]               │
│   Custom:  [#tradition ▼] [continental ▼]           │
│                                                     │
│ ─────────────────────────────────────────────────── │
│ Results (15 matches)                                │
│ ┌───────────────────────────────────────────────┐   │
│ │ 📖 Being and Time (0.92)                      │   │
│ │   "...the question of the meaning of Being..." │   │
│ │   Chapter 1, p. 42                             │   │
│ ├───────────────────────────────────────────────┤   │
│ │ 📖 Phenomenology of Spirit (0.87)             │   │
│ │   "...consciousness of something as..."       │   │
│ │   Preface, p. 15                              │   │
│ └───────────────────────────────────────────────┘   │
│                                                     │
│          [Go to Book] [View in Context]             │
└─────────────────────────────────────────────────────┘
```

## Related Decisions

- [ADR-004](004-minimal-viewer-modification.md): Same minimal modification philosophy
- [ADR-006](006-hybrid-metadata-filtering.md): Metadata filter implementation
- [ADR-008](008-background-indexing.md): Background indexing for bulk operations
