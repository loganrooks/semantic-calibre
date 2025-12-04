#!/usr/bin/env python
# License: GPL v3 Copyright: 2025

"""
Profile Manager Dialog for Semantic Search.

This dialog allows users to manage embedding profiles and view/modify
the semantic search index for their library.
"""

import os
from functools import partial

from qt.core import (
    QAbstractTableModel, QComboBox, QDialogButtonBox, QFrame,
    QGroupBox, QHBoxLayout, QHeaderView, QIcon, QLabel, QLineEdit,
    QModelIndex, QProgressBar, QPushButton, QSize, QSpinBox,
    QTableView, Qt, QVBoxLayout, QWidget, pyqtSignal,
)

from calibre.gui2 import error_dialog, info_dialog, question_dialog
from calibre.gui2.ui import get_gui
from calibre.gui2.widgets2 import Dialog


def get_db():
    """Get the current library database."""
    gui = get_gui()
    if gui is not None:
        return gui.current_db.new_api
    return None


def get_library_engine():
    """Get or create the LibrarySearchEngine for the current library."""
    try:
        from calibre_semantic.library import get_library_engine as _get
        db = get_db()
        if db is None:
            return None
        return _get(db)
    except ImportError:
        return None


class ProfilesTableModel(QAbstractTableModel):
    """Table model for displaying embedding profiles."""

    HEADERS = [_('Profile ID'), _('Provider'), _('Model'), _('Dimension'), _('Books Indexed')]

    def __init__(self, parent=None):
        super().__init__(parent)
        self._profiles = []
        self._stats = {}

    def refresh(self):
        """Refresh profile data from engine."""
        self.beginResetModel()
        self._profiles = []
        self._stats = {}

        engine = get_library_engine()
        if engine is not None:
            try:
                profiles = engine.get_profiles()
                self._profiles = profiles if profiles else []
                # Get stats for each profile
                for profile in self._profiles:
                    pid = profile.profile_id if hasattr(profile, 'profile_id') else str(profile)
                    try:
                        stats = engine.get_stats(profile_id=pid)
                        self._stats[pid] = stats
                    except Exception:
                        self._stats[pid] = {}
            except Exception:
                pass

        self.endResetModel()

    def rowCount(self, parent=QModelIndex()):
        return len(self._profiles)

    def columnCount(self, parent=QModelIndex()):
        return len(self.HEADERS)

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return self.HEADERS[section]
        return None

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid() or index.row() >= len(self._profiles):
            return None

        profile = self._profiles[index.row()]
        col = index.column()

        if role == Qt.ItemDataRole.DisplayRole:
            pid = profile.profile_id if hasattr(profile, 'profile_id') else str(profile)

            if col == 0:  # Profile ID
                return pid
            elif col == 1:  # Provider
                return getattr(profile, 'provider_id', 'Unknown')
            elif col == 2:  # Model
                return getattr(profile, 'model_name', 'Unknown')
            elif col == 3:  # Dimension
                return str(getattr(profile, 'dimension', '?'))
            elif col == 4:  # Books Indexed
                stats = self._stats.get(pid, {})
                count = stats.get('book_count', 0)
                return str(count)

        return None

    def get_profile(self, row):
        """Get profile at given row."""
        if 0 <= row < len(self._profiles):
            return self._profiles[row]
        return None


class IndexedBooksPanel(QWidget):
    """Panel showing indexed books for a profile."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_profile = None
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # Stats
        stats_layout = QHBoxLayout()
        self.books_label = QLabel(_('Indexed books: 0'))
        stats_layout.addWidget(self.books_label)
        self.chunks_label = QLabel(_('Total chunks: 0'))
        stats_layout.addWidget(self.chunks_label)
        stats_layout.addStretch()
        layout.addLayout(stats_layout)

        # Action buttons
        btn_layout = QHBoxLayout()

        self.index_selected_btn = QPushButton(_('Index Selected Books'))
        self.index_selected_btn.setIcon(QIcon.ic('plus.png'))
        self.index_selected_btn.clicked.connect(self._index_selected)
        btn_layout.addWidget(self.index_selected_btn)

        self.index_all_btn = QPushButton(_('Index All Books'))
        self.index_all_btn.setIcon(QIcon.ic('lt.png'))
        self.index_all_btn.clicked.connect(self._index_all)
        btn_layout.addWidget(self.index_all_btn)

        self.clear_btn = QPushButton(_('Clear Index'))
        self.clear_btn.setIcon(QIcon.ic('trash.png'))
        self.clear_btn.clicked.connect(self._clear_index)
        btn_layout.addWidget(self.clear_btn)

        btn_layout.addStretch()
        layout.addLayout(btn_layout)

        # Progress bar (hidden by default)
        self.progress = QProgressBar()
        self.progress.setVisible(False)
        layout.addWidget(self.progress)

        layout.addStretch()

    def set_profile(self, profile_id):
        """Set the current profile and refresh stats."""
        self.current_profile = profile_id
        self._refresh_stats()

    def _refresh_stats(self):
        """Refresh statistics display."""
        if not self.current_profile:
            self.books_label.setText(_('Indexed books: 0'))
            self.chunks_label.setText(_('Total chunks: 0'))
            return

        engine = get_library_engine()
        if engine is None:
            return

        try:
            stats = engine.get_stats(profile_id=self.current_profile)
            book_count = stats.get('book_count', 0)
            chunk_count = stats.get('chunk_count', 0)
            self.books_label.setText(_('Indexed books: {}').format(book_count))
            self.chunks_label.setText(_('Total chunks: {}').format(chunk_count))
        except Exception as e:
            self.books_label.setText(_('Error loading stats'))

    def _index_selected(self):
        """Index currently selected books in library view."""
        gui = get_gui()
        if gui is None:
            return

        rows = gui.library_view.selectionModel().selectedRows()
        if not rows:
            info_dialog(
                self, _('No Selection'),
                _('Please select books in the library view to index.'),
                show=True
            )
            return

        book_ids = [gui.library_view.model().id(row) for row in rows]
        self._do_index(book_ids)

    def _index_all(self):
        """Index all books in library."""
        if not question_dialog(
            self, _('Index All Books'),
            _('This will index all books in the library. '
              'This may take a long time for large libraries. Continue?')
        ):
            return

        db = get_db()
        if db is None:
            return

        book_ids = list(db.all_book_ids())
        self._do_index(book_ids)

    def _do_index(self, book_ids):
        """Execute indexing for given book IDs."""
        if not book_ids:
            return

        engine = get_library_engine()
        if engine is None:
            error_dialog(
                self, _('Error'),
                _('Could not initialize search engine.'),
                show=True
            )
            return

        self.progress.setVisible(True)
        self.progress.setMaximum(len(book_ids))
        self.progress.setValue(0)

        try:
            def progress_callback(current, total, book_id, message):
                self.progress.setValue(current)

            results = engine.index_books(
                book_ids=book_ids,
                profile_id=self.current_profile,
                progress_callback=progress_callback,
                skip_indexed=True,
            )

            self.progress.setVisible(False)
            self._refresh_stats()

            info_dialog(
                self, _('Indexing Complete'),
                _('Successfully indexed {} books. {} failed, {} skipped.').format(
                    len(results.succeeded),
                    len(results.failed),
                    len(results.skipped),
                ),
                show=True
            )

        except Exception as e:
            self.progress.setVisible(False)
            error_dialog(
                self, _('Indexing Error'),
                _('An error occurred during indexing: {}').format(str(e)),
                show=True
            )

    def _clear_index(self):
        """Clear the index for current profile."""
        if not self.current_profile:
            return

        if not question_dialog(
            self, _('Clear Index'),
            _('This will remove all indexed data for profile "{}". '
              'This cannot be undone. Continue?').format(self.current_profile)
        ):
            return

        engine = get_library_engine()
        if engine is None:
            return

        try:
            engine.clear(profile_id=self.current_profile)
            self._refresh_stats()
            info_dialog(
                self, _('Index Cleared'),
                _('Index has been cleared for profile "{}".').format(self.current_profile),
                show=True
            )
        except Exception as e:
            error_dialog(
                self, _('Error'),
                _('Failed to clear index: {}').format(str(e)),
                show=True
            )


class ProfileManagerDialog(Dialog):
    """Dialog for managing semantic search profiles and indexes."""

    def __init__(self, parent=None):
        super().__init__(
            _('Semantic Search - Profile Manager'),
            'semantic-profile-manager-dialog',
            default_buttons=QDialogButtonBox.StandardButton.Close
        )
        self.setWindowIcon(QIcon.ic('lt.png'))

    def setup_ui(self):
        layout = QVBoxLayout(self)

        # Profiles section
        profiles_group = QGroupBox(_('Embedding Profiles'))
        profiles_layout = QVBoxLayout(profiles_group)

        # Profiles table
        self.profiles_model = ProfilesTableModel(self)
        self.profiles_table = QTableView()
        self.profiles_table.setModel(self.profiles_model)
        self.profiles_table.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.profiles_table.setSelectionMode(QTableView.SelectionMode.SingleSelection)
        self.profiles_table.selectionModel().selectionChanged.connect(self._on_profile_selected)
        self.profiles_table.horizontalHeader().setStretchLastSection(True)
        profiles_layout.addWidget(self.profiles_table)

        # Profile buttons
        profile_btn_layout = QHBoxLayout()
        self.refresh_btn = QPushButton(_('Refresh'))
        self.refresh_btn.setIcon(QIcon.ic('view-refresh.png'))
        self.refresh_btn.clicked.connect(self._refresh_profiles)
        profile_btn_layout.addWidget(self.refresh_btn)
        profile_btn_layout.addStretch()
        profiles_layout.addLayout(profile_btn_layout)

        layout.addWidget(profiles_group)

        # Index management section
        index_group = QGroupBox(_('Index Management'))
        index_layout = QVBoxLayout(index_group)

        self.indexed_panel = IndexedBooksPanel(self)
        index_layout.addWidget(self.indexed_panel)

        layout.addWidget(index_group)

        # Buttons
        layout.addWidget(self.bb)

        # Initialize
        self._refresh_profiles()

    def _refresh_profiles(self):
        """Refresh the profiles list."""
        self.profiles_model.refresh()
        # Resize columns
        for i in range(self.profiles_model.columnCount()):
            self.profiles_table.resizeColumnToContents(i)

    def _on_profile_selected(self):
        """Handle profile selection change."""
        indexes = self.profiles_table.selectionModel().selectedRows()
        if indexes:
            row = indexes[0].row()
            profile = self.profiles_model.get_profile(row)
            if profile:
                pid = profile.profile_id if hasattr(profile, 'profile_id') else str(profile)
                self.indexed_panel.set_profile(pid)
        else:
            self.indexed_panel.set_profile(None)

    def sizeHint(self):
        return QSize(800, 600)


if __name__ == '__main__':
    from calibre.gui2 import Application
    from calibre.library import db

    get_db.db = db(os.path.expanduser('~/calibre'))
    app = Application([])
    d = ProfileManagerDialog()
    d.exec()
