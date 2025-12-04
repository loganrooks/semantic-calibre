#!/usr/bin/env python
# License: GPL v3 Copyright: 2025

"""
Semantic Search Action for Calibre Library.

This action provides semantic (meaning-based) search across the Calibre library,
powered by the calibre_semantic library. Unlike full-text search which matches
exact keywords, semantic search finds books by concept and meaning.
"""

from functools import partial

from qt.core import QIcon, QProgressDialog

from calibre.gui2 import error_dialog, info_dialog
from calibre.gui2.actions import InterfaceAction


class SemanticSearchAction(InterfaceAction):
    """Action to show the semantic search dialog and manage semantic index."""

    name = 'Semantic Search'
    action_spec = (_('Semantic search'), 'search.png',
                   _('Search books by meaning using AI embeddings'), ('Ctrl+Shift+S',))
    dont_add_to = frozenset(('context-menu-device',))
    action_type = 'current'
    action_add_menu = True
    action_menu_clone_qaction = _('Search library...')

    def genesis(self):
        self.menu = self.qaction.menu()
        self.qaction.triggered.connect(self.show_semantic_search)
        self._dialog = None

        # Add menu actions
        ma = partial(self.create_menu_action, self.menu)

        self.menu.addSeparator()
        ma('semantic-add-to-index', _('Add selected books to index'),
           icon='plus.png', shortcut='Ctrl+Shift+I',
           description=_('Add selected books to the semantic search index')
           ).triggered.connect(self.add_selected_to_index)

        ma('semantic-manage-index', _('Manage index...'),
           icon='lt.png',
           description=_('Open the semantic index manager')
           ).triggered.connect(self.show_index_manager)

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

    def add_selected_to_index(self):
        """Add currently selected books to the semantic index."""
        rows = self.gui.library_view.selectionModel().selectedRows()
        if not rows:
            info_dialog(
                self.gui, _('No Selection'),
                _('Please select books to add to the semantic index.'),
                show=True
            )
            return

        book_ids = [self.gui.library_view.model().id(row) for row in rows]
        self._do_index_books(book_ids)

    def _do_index_books(self, book_ids):
        """Execute indexing for given book IDs."""
        if not book_ids:
            return

        try:
            from calibre_semantic.library import get_library_engine
        except ImportError:
            error_dialog(
                self.gui, _('Not Available'),
                _('The calibre_semantic library is not installed. '
                  'Semantic search features are not available.'),
                show=True
            )
            return

        db = self.gui.current_db.new_api
        engine = get_library_engine(db)
        if engine is None:
            error_dialog(
                self.gui, _('Error'),
                _('Could not initialize the semantic search engine.'),
                show=True
            )
            return

        # Show progress dialog
        progress = QProgressDialog(
            _('Indexing books for semantic search...'),
            _('Cancel'), 0, len(book_ids), self.gui
        )
        progress.setWindowTitle(_('Semantic Indexing'))
        progress.setMinimumDuration(0)
        progress.setValue(0)
        progress.show()

        cancelled = False
        succeeded = 0
        failed = 0
        skipped = 0

        try:
            for i, book_id in enumerate(book_ids):
                if progress.wasCanceled():
                    cancelled = True
                    break

                progress.setValue(i)
                progress.setLabelText(
                    _('Indexing book {} of {}...').format(i + 1, len(book_ids))
                )

                try:
                    # Check if already indexed
                    if engine.is_book_indexed(book_id):
                        skipped += 1
                        continue

                    # Index the book
                    result = engine.index_book(book_id)
                    if result:
                        succeeded += 1
                    else:
                        failed += 1
                except Exception as e:
                    failed += 1

            progress.setValue(len(book_ids))

        finally:
            progress.close()

        # Show result
        if cancelled:
            msg = _('Indexing cancelled. {} books indexed, {} failed, {} skipped.').format(
                succeeded, failed, skipped
            )
        else:
            msg = _('Indexing complete. {} books indexed, {} failed, {} skipped.').format(
                succeeded, failed, skipped
            )

        info_dialog(
            self.gui, _('Indexing Complete'),
            msg,
            show=True
        )

    def show_index_manager(self):
        """Show the index management dialog."""
        try:
            from calibre.gui2.semantic_search.profile_manager import ProfileManagerDialog
            dlg = ProfileManagerDialog(self.gui)
            dlg.exec()
        except ImportError:
            error_dialog(
                self.gui, _('Not Available'),
                _('The semantic search profile manager is not available.'),
                show=True
            )

    def library_changed(self, db):
        """Called when the library is changed."""
        if self._dialog is not None:
            self._dialog.library_changed()

    def clear_search_history(self):
        """Clear the search history."""
        if self._dialog is not None:
            self._dialog.clear_search_history()
