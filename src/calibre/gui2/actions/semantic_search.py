#!/usr/bin/env python
# License: GPL v3 Copyright: 2025

"""
Semantic Search Action for Calibre Library.

This action provides semantic (meaning-based) search across the Calibre library,
powered by the calibre_semantic library. Unlike full-text search which matches
exact keywords, semantic search finds books by concept and meaning.
"""

from calibre.gui2.actions import InterfaceAction


class SemanticSearchAction(InterfaceAction):
    """Action to show the semantic search dialog."""

    name = 'Semantic Search'
    action_spec = (_('Semantic search'), 'search.png',
                   _('Search books by meaning using AI embeddings'), ('Ctrl+Shift+S',))
    dont_add_to = frozenset(('context-menu-device',))
    action_type = 'current'

    def genesis(self):
        self.qaction.triggered.connect(self.show_semantic_search)
        self._dialog = None

    @property
    def dialog(self):
        if self._dialog is None:
            from calibre.gui2.semantic_search.dialog import SemanticSearchDialog
            self._dialog = SemanticSearchDialog(self.gui)
        return self._dialog

    def show_semantic_search(self):
        """Show the semantic search dialog."""
        # If there's text in the search bar, use it as initial query
        text = self.gui.search.text()
        if text and ':' not in text:
            self.dialog.set_search_text(text)
        self.dialog.show()
        self.dialog.raise_and_focus()

    def library_changed(self, db):
        """Called when the library is changed."""
        if self._dialog is not None:
            self._dialog.library_changed()

    def clear_search_history(self):
        """Clear the search history."""
        if self._dialog is not None:
            self._dialog.clear_search_history()
