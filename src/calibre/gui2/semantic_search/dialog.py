#!/usr/bin/env python
# License: GPL v3 Copyright: 2025

"""
Semantic Search Dialog for Calibre Library.

This dialog provides a UI for searching books by meaning using AI embeddings.
It includes a search panel with query input, metadata filters, and results display.
"""

import os
import time
from functools import partial

from qt.core import (
    QAction, QComboBox, QDialogButtonBox, QFrame, QGroupBox,
    QHBoxLayout, QIcon, QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPixmap, QPushButton, QSize, QSplitter, QStackedWidget, Qt, QVBoxLayout,
    QWidget, pyqtSignal,
)

from calibre.gui2 import error_dialog, gprefs, info_dialog, warning_dialog
from calibre.gui2.ui import get_gui
from calibre.gui2.widgets2 import Dialog, HistoryLineEdit2


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


class ProfileSelector(QWidget):
    """Widget for selecting embedding profile."""

    profile_changed = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.label = QLabel(_('Profile:'))
        layout.addWidget(self.label)

        self.combo = QComboBox()
        self.combo.setMinimumWidth(150)
        self.combo.currentTextChanged.connect(self._on_profile_changed)
        layout.addWidget(self.combo)

        self.refresh_btn = QPushButton()
        self.refresh_btn.setIcon(QIcon.ic('view-refresh.png'))
        self.refresh_btn.setToolTip(_('Refresh profile list'))
        self.refresh_btn.clicked.connect(self.refresh_profiles)
        layout.addWidget(self.refresh_btn)

        layout.addStretch()

    def refresh_profiles(self):
        """Refresh the list of available profiles."""
        engine = get_library_engine()
        if engine is None:
            self.combo.clear()
            self.combo.addItem(_('(No profiles available)'))
            return

        current = self.combo.currentText()
        self.combo.clear()

        try:
            profiles = engine.get_profiles()
            if not profiles:
                self.combo.addItem('library-default')
            else:
                for profile in profiles:
                    self.combo.addItem(profile.profile_id if hasattr(profile, 'profile_id') else str(profile))

            # Restore selection
            idx = self.combo.findText(current)
            if idx >= 0:
                self.combo.setCurrentIndex(idx)
        except Exception as e:
            self.combo.addItem('library-default')

    def current_profile(self):
        """Get the currently selected profile ID."""
        return self.combo.currentText() or 'library-default'

    def _on_profile_changed(self, text):
        self.profile_changed.emit(text)


class MetadataFilterPanel(QWidget):
    """Panel for building metadata filters with preset support."""

    filter_changed = pyqtSignal()

    PRESETS_PREF_KEY = 'semantic_search_filter_presets'

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # Presets section
        presets_group = QGroupBox(_('Filter Presets'))
        presets_layout = QVBoxLayout(presets_group)

        # Preset selector row
        preset_row = QHBoxLayout()
        self.preset_combo = QComboBox()
        self.preset_combo.setMinimumWidth(120)
        self.preset_combo.currentTextChanged.connect(self._on_preset_selected)
        preset_row.addWidget(self.preset_combo, 1)

        self.save_preset_btn = QPushButton()
        self.save_preset_btn.setIcon(QIcon.ic('save.png'))
        self.save_preset_btn.setToolTip(_('Save current filters as preset'))
        self.save_preset_btn.clicked.connect(self._save_preset)
        preset_row.addWidget(self.save_preset_btn)

        self.delete_preset_btn = QPushButton()
        self.delete_preset_btn.setIcon(QIcon.ic('trash.png'))
        self.delete_preset_btn.setToolTip(_('Delete selected preset'))
        self.delete_preset_btn.clicked.connect(self._delete_preset)
        preset_row.addWidget(self.delete_preset_btn)

        presets_layout.addLayout(preset_row)
        layout.addWidget(presets_group)

        # Authors filter
        authors_group = QGroupBox(_('Authors'))
        authors_layout = QVBoxLayout(authors_group)
        self.authors_input = QLineEdit()
        self.authors_input.setPlaceholderText(_('Enter author names, comma-separated'))
        self.authors_input.textChanged.connect(self._on_filter_changed)
        authors_layout.addWidget(self.authors_input)
        layout.addWidget(authors_group)

        # Tags filter
        tags_group = QGroupBox(_('Tags'))
        tags_layout = QVBoxLayout(tags_group)
        self.tags_input = QLineEdit()
        self.tags_input.setPlaceholderText(_('Enter tags, comma-separated'))
        self.tags_input.textChanged.connect(self._on_filter_changed)
        tags_layout.addWidget(self.tags_input)
        layout.addWidget(tags_group)

        # Series filter
        series_group = QGroupBox(_('Series'))
        series_layout = QVBoxLayout(series_group)
        self.series_input = QLineEdit()
        self.series_input.setPlaceholderText(_('Enter series name'))
        self.series_input.textChanged.connect(self._on_filter_changed)
        series_layout.addWidget(self.series_input)
        layout.addWidget(series_group)

        # Clear button
        self.clear_btn = QPushButton(_('Clear Filters'))
        self.clear_btn.clicked.connect(self.clear_filters)
        layout.addWidget(self.clear_btn)

        layout.addStretch()

        # Load presets
        self._refresh_presets()

    def _get_presets(self):
        """Get saved presets from preferences."""
        return gprefs.get(self.PRESETS_PREF_KEY, {})

    def _save_presets(self, presets):
        """Save presets to preferences."""
        gprefs[self.PRESETS_PREF_KEY] = presets

    def _refresh_presets(self):
        """Refresh the preset combo box."""
        current = self.preset_combo.currentText()
        self.preset_combo.blockSignals(True)
        self.preset_combo.clear()
        self.preset_combo.addItem('')  # Empty item for "no preset"

        presets = self._get_presets()
        for name in sorted(presets.keys()):
            self.preset_combo.addItem(name)

        # Restore selection if possible
        idx = self.preset_combo.findText(current)
        if idx >= 0:
            self.preset_combo.setCurrentIndex(idx)
        self.preset_combo.blockSignals(False)

    def _on_preset_selected(self, name):
        """Load the selected preset."""
        if not name:
            return

        presets = self._get_presets()
        if name in presets:
            preset = presets[name]
            self.authors_input.setText(preset.get('authors', ''))
            self.tags_input.setText(preset.get('tags', ''))
            self.series_input.setText(preset.get('series', ''))

    def _save_preset(self):
        """Save current filters as a new preset."""
        from qt.core import QInputDialog

        name, ok = QInputDialog.getText(
            self, _('Save Preset'),
            _('Enter a name for this filter preset:')
        )
        if not ok or not name.strip():
            return

        name = name.strip()
        presets = self._get_presets()
        presets[name] = {
            'authors': self.authors_input.text(),
            'tags': self.tags_input.text(),
            'series': self.series_input.text(),
        }
        self._save_presets(presets)
        self._refresh_presets()
        self.preset_combo.setCurrentText(name)

    def _delete_preset(self):
        """Delete the currently selected preset."""
        name = self.preset_combo.currentText()
        if not name:
            return

        from calibre.gui2 import question_dialog
        if not question_dialog(
            self, _('Delete Preset'),
            _('Are you sure you want to delete the preset "{}"?').format(name)
        ):
            return

        presets = self._get_presets()
        if name in presets:
            del presets[name]
            self._save_presets(presets)
            self._refresh_presets()

    def clear_filters(self):
        """Clear all filter inputs."""
        self.preset_combo.setCurrentIndex(0)  # Clear preset selection
        self.authors_input.clear()
        self.tags_input.clear()
        self.series_input.clear()

    def _on_filter_changed(self):
        self.filter_changed.emit()

    def build_filter(self):
        """Build a MetadataFilterBuilder from current inputs."""
        try:
            from calibre_semantic.library import MetadataFilterBuilder
        except ImportError:
            return None

        builder = MetadataFilterBuilder()

        # Authors
        authors_text = self.authors_input.text().strip()
        if authors_text:
            authors = [a.strip() for a in authors_text.split(',') if a.strip()]
            if authors:
                builder.add_authors(authors)

        # Tags
        tags_text = self.tags_input.text().strip()
        if tags_text:
            tags = [t.strip() for t in tags_text.split(',') if t.strip()]
            if tags:
                builder.add_tags(tags)

        # Series
        series_text = self.series_input.text().strip()
        if series_text:
            builder.add_series([series_text])

        return builder if not builder.is_empty() else None


class SearchResultItem(QListWidgetItem):
    """List item for a search result."""

    def __init__(self, result):
        self.result = result
        title = result.title or f'Book {result.book_id}'
        authors = ', '.join(result.authors) if result.authors else _('Unknown')
        score = f'{result.score:.0%}' if result.score else ''

        text = f'{title}\n{authors}'
        if score:
            text += f' ({score} match)'

        super().__init__(text)
        self.setToolTip(result.chunk_text[:500] if result.chunk_text else '')

        # Set book cover as icon
        self._set_cover_icon(result.book_id)

    def _set_cover_icon(self, book_id):
        """Set book cover as the item icon."""
        gui = get_gui()
        if gui is None:
            return

        try:
            db = gui.current_db.new_api
            cover = db.cover(book_id, as_pixmap=True)
            if cover:
                self.setIcon(QIcon(cover))
            else:
                # Use default cover if no cover available
                self.setIcon(QIcon.ic('default_cover.png'))
        except Exception:
            # Silently fail - item will just have no icon
            pass


class ResultsPanel(QWidget):
    """Panel displaying search results."""

    result_selected = pyqtSignal(object)  # Emits LibrarySearchResult

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # Status label
        self.status_label = QLabel(_('Enter a query to search'))
        layout.addWidget(self.status_label)

        # Results list with book cover icons
        self.results_list = QListWidget()
        self.results_list.setIconSize(QSize(60, 80))  # Standard cover aspect ratio
        self.results_list.setSpacing(4)
        self.results_list.itemClicked.connect(self._on_item_clicked)
        self.results_list.itemDoubleClicked.connect(self._on_item_double_clicked)
        layout.addWidget(self.results_list)

        # Preview area
        self.preview_label = QLabel()
        self.preview_label.setWordWrap(True)
        self.preview_label.setFrameStyle(QFrame.Shape.StyledPanel)
        self.preview_label.setMinimumHeight(100)
        layout.addWidget(self.preview_label)

    def clear(self):
        """Clear results."""
        self.results_list.clear()
        self.preview_label.clear()
        self.status_label.setText(_('Enter a query to search'))

    def set_results(self, results, search_time_ms=None):
        """Display search results."""
        self.results_list.clear()
        self.preview_label.clear()

        if not results:
            self.status_label.setText(_('No results found'))
            return

        time_str = f' ({search_time_ms:.0f}ms)' if search_time_ms else ''
        self.status_label.setText(ngettext(
            '{} result found{}',
            '{} results found{}',
            len(results)
        ).format(len(results), time_str))

        for result in results:
            item = SearchResultItem(result)
            self.results_list.addItem(item)

        # Select first result
        if self.results_list.count() > 0:
            self.results_list.setCurrentRow(0)
            self._show_preview(results[0])

    def set_status(self, text):
        """Set status message."""
        self.status_label.setText(text)

    def _on_item_clicked(self, item):
        if isinstance(item, SearchResultItem):
            self._show_preview(item.result)
            self.result_selected.emit(item.result)

    def _on_item_double_clicked(self, item):
        """Open book in viewer on double-click."""
        if isinstance(item, SearchResultItem):
            gui = get_gui()
            if gui is not None:
                gui.iactions['View'].view_book(False)

    def _show_preview(self, result):
        """Show preview of result text."""
        if result.chunk_text:
            preview = result.chunk_text[:1000]
            if len(result.chunk_text) > 1000:
                preview += '...'
            self.preview_label.setText(preview)
        else:
            self.preview_label.clear()


class SearchPanel(QWidget):
    """Main search panel with query input and search button."""

    search_requested = pyqtSignal(str)  # Emits query string

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # Search input row
        search_row = QHBoxLayout()

        self.search_input = HistoryLineEdit2(self)
        self.search_input.setPlaceholderText(_('Enter your semantic search query...'))
        self.search_input.returnPressed.connect(self._on_search)
        search_row.addWidget(self.search_input, 1)

        self.search_btn = QPushButton(_('Search'))
        self.search_btn.setIcon(QIcon.ic('search.png'))
        self.search_btn.clicked.connect(self._on_search)
        search_row.addWidget(self.search_btn)

        layout.addLayout(search_row)

    def set_search_text(self, text):
        """Set the search query text."""
        self.search_input.setText(text)

    def get_search_text(self):
        """Get the current search query text."""
        return self.search_input.text().strip()

    def _on_search(self):
        text = self.get_search_text()
        if text:
            self.search_requested.emit(text)

    def clear_history(self):
        """Clear search history."""
        self.search_input.clear_history()


class SemanticSearchDialog(Dialog):
    """Main semantic search dialog."""

    def __init__(self, parent=None):
        super().__init__(
            _('Semantic Search'),
            'library-semantic-search-dialog',
            default_buttons=QDialogButtonBox.StandardButton.Close
        )
        self.setWindowIcon(QIcon.ic('search.png'))
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowMinMaxButtonsHint)

    def setup_ui(self):
        layout = QVBoxLayout(self)

        # Check if calibre_semantic is available
        self.library_available = self._check_library_available()

        if not self.library_available:
            # Show error message
            error_label = QLabel(_(
                '<p><b>Semantic search is not available.</b></p>'
                '<p>The calibre_semantic library is not installed. '
                'Please install it to enable semantic search functionality.</p>'
            ))
            error_label.setWordWrap(True)
            layout.addWidget(error_label)
            layout.addWidget(self.bb)
            return

        # Profile selector
        self.profile_selector = ProfileSelector(self)
        layout.addWidget(self.profile_selector)

        # Main splitter
        self.splitter = QSplitter(Qt.Orientation.Horizontal)
        layout.addWidget(self.splitter, 1)

        # Left side: filters
        filters_widget = QWidget()
        filters_layout = QVBoxLayout(filters_widget)
        filters_layout.setContentsMargins(0, 0, 0, 0)

        filters_label = QLabel(_('<b>Metadata Filters</b>'))
        filters_layout.addWidget(filters_label)

        self.filter_panel = MetadataFilterPanel(self)
        filters_layout.addWidget(self.filter_panel)

        self.splitter.addWidget(filters_widget)

        # Right side: search and results
        search_widget = QWidget()
        search_layout = QVBoxLayout(search_widget)
        search_layout.setContentsMargins(0, 0, 0, 0)

        self.search_panel = SearchPanel(self)
        self.search_panel.search_requested.connect(self._do_search)
        search_layout.addWidget(self.search_panel)

        self.results_panel = ResultsPanel(self)
        self.results_panel.result_selected.connect(self._on_result_selected)
        search_layout.addWidget(self.results_panel, 1)

        self.splitter.addWidget(search_widget)

        # Set splitter proportions
        self.splitter.setSizes([250, 750])

        # Buttons
        button_layout = QHBoxLayout()

        self.index_btn = QPushButton(_('Manage Index...'))
        self.index_btn.setIcon(QIcon.ic('lt.png'))
        self.index_btn.clicked.connect(self._show_index_manager)
        button_layout.addWidget(self.index_btn)

        button_layout.addStretch()
        button_layout.addWidget(self.bb)

        layout.addLayout(button_layout)

        # Initialize
        self.profile_selector.refresh_profiles()

    def _check_library_available(self):
        """Check if calibre_semantic library is available."""
        try:
            from calibre_semantic.library import LibrarySearchEngine
            return True
        except ImportError:
            return False

    def _do_search(self, query):
        """Execute semantic search."""
        if not query:
            return

        self.results_panel.set_status(_('Searching...'))

        try:
            engine = get_library_engine()
            if engine is None:
                error_dialog(
                    self, _('Search Error'),
                    _('Could not initialize search engine. Please check that '
                      'calibre_semantic is properly installed.'),
                    show=True
                )
                return

            # Build filter
            metadata_filter = self.filter_panel.build_filter()
            profile_id = self.profile_selector.current_profile()

            # Execute search
            start_time = time.time()
            results = engine.search(
                query=query,
                metadata_filter=metadata_filter,
                profile_id=profile_id,
                limit=50,
            )
            elapsed_ms = (time.time() - start_time) * 1000

            self.results_panel.set_results(
                results.results if hasattr(results, 'results') else results,
                search_time_ms=elapsed_ms
            )

        except Exception as e:
            error_dialog(
                self, _('Search Error'),
                _('An error occurred during search: {}').format(str(e)),
                show=True
            )
            self.results_panel.set_status(_('Search failed'))

    def _on_result_selected(self, result):
        """Handle result selection."""
        gui = get_gui()
        if gui is not None and hasattr(result, 'book_id'):
            # Highlight the book in the library view
            gui.library_view.select_rows([result.book_id])

    def _show_index_manager(self):
        """Show the index management dialog."""
        try:
            from calibre.gui2.semantic_search.profile_manager import ProfileManagerDialog
            dlg = ProfileManagerDialog(self)
            dlg.exec()
            # Refresh profiles after manager closes
            self.profile_selector.refresh_profiles()
        except ImportError:
            info_dialog(
                self, _('Not Available'),
                _('Profile manager is not yet implemented.'),
                show=True
            )

    def set_search_text(self, text):
        """Set initial search text."""
        if hasattr(self, 'search_panel'):
            self.search_panel.set_search_text(text)

    def library_changed(self):
        """Called when library changes."""
        self.results_panel.clear()
        if hasattr(self, 'profile_selector'):
            self.profile_selector.refresh_profiles()

    def clear_search_history(self):
        """Clear search history."""
        if hasattr(self, 'search_panel'):
            self.search_panel.clear_history()

    def sizeHint(self):
        return QSize(1000, 700)

    def show(self):
        super().show()
        if hasattr(self, 'search_panel'):
            self.search_panel.search_input.setFocus()

    def raise_and_focus(self):
        """Raise window and set focus."""
        self.raise_()
        self.activateWindow()
        if hasattr(self, 'search_panel'):
            self.search_panel.search_input.setFocus()


if __name__ == '__main__':
    from calibre.gui2 import Application
    from calibre.library import db

    # For testing
    get_db.db = db(os.path.expanduser('~/calibre'))
    app = Application([])
    d = SemanticSearchDialog()
    d.exec()
