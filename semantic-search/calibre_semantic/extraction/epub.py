"""EPUB content extraction.

This module provides the EPUBExtractor class for extracting text content
from EPUB e-book files. EPUBs are ZIP archives containing XHTML content
files organized according to the OPF manifest and spine.

Usage:
    >>> from calibre_semantic.extraction.epub import EPUBExtractor
    >>> extractor = EPUBExtractor("book.epub")
    >>> for item in extractor.iter_content():
    ...     print(f"Chapter: {item['chapter_title']}")
    ...     print(item['text'][:200])
"""

from __future__ import annotations

import html
import io
import logging
import re
import zipfile
from pathlib import Path
from typing import Any, Iterator
from xml.etree import ElementTree as ET

logger = logging.getLogger(__name__)


class EPUBError(Exception):
    """Exception raised for EPUB parsing errors."""
    pass


class EPUBExtractor:
    """Extract text content from EPUB files.

    This class parses EPUB files and provides methods to extract:
    - Book metadata (title, author, language)
    - Spine items (ordered list of content files)
    - Plain text content from each spine item
    - Chapter titles from headings

    Attributes:
        _zipfile: The opened EPUB ZIP archive
        _opf_path: Path to the OPF file within the archive
        _opf_root: Parsed OPF XML root element
        _spine: Cached list of spine items
    """

    # XML namespaces used in EPUB
    NAMESPACES = {
        'container': 'urn:oasis:names:tc:opendocument:xmlns:container',
        'opf': 'http://www.idpf.org/2007/opf',
        'dc': 'http://purl.org/dc/elements/1.1/',
        'xhtml': 'http://www.w3.org/1999/xhtml',
    }

    # Block-level HTML elements that should have spacing
    BLOCK_ELEMENTS = {
        'p', 'div', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
        'blockquote', 'pre', 'li', 'dt', 'dd', 'tr', 'th', 'td',
        'section', 'article', 'aside', 'header', 'footer', 'nav',
    }

    def __init__(self, source: bytes | str | Path):
        """Initialize the EPUB extractor.

        Args:
            source: EPUB file as bytes, file path string, or Path object

        Raises:
            EPUBError: If the file is not a valid EPUB
        """
        self._source = source
        self._zipfile: zipfile.ZipFile | None = None
        self._opf_path: str = ""
        self._opf_root: ET.Element | None = None
        self._opf_dir: str = ""
        self._spine: list[dict[str, Any]] | None = None
        self._manifest: dict[str, dict[str, str]] | None = None

        self._open()

    def _open(self) -> None:
        """Open and validate the EPUB file."""
        try:
            if isinstance(self._source, bytes):
                self._zipfile = zipfile.ZipFile(io.BytesIO(self._source), 'r')
            else:
                self._zipfile = zipfile.ZipFile(self._source, 'r')
        except zipfile.BadZipFile as e:
            raise EPUBError(f"Invalid EPUB: not a valid ZIP file: {e}") from e

        # Find and parse container.xml
        try:
            container_data = self._zipfile.read('META-INF/container.xml')
        except KeyError as e:
            raise EPUBError("Invalid EPUB: META-INF/container.xml not found") from e

        try:
            container = ET.fromstring(container_data)
        except ET.ParseError as e:
            raise EPUBError(f"Invalid EPUB: malformed container.xml: {e}") from e

        # Find OPF path
        rootfile = container.find(
            './/container:rootfile[@media-type="application/oebps-package+xml"]',
            self.NAMESPACES
        )
        if rootfile is None:
            # Try without namespace (some EPUBs don't use namespaces properly)
            rootfile = container.find('.//{*}rootfile[@media-type="application/oebps-package+xml"]')

        if rootfile is None:
            raise EPUBError("Invalid EPUB: no OPF rootfile found in container.xml")

        self._opf_path = rootfile.get('full-path', '')
        if not self._opf_path:
            raise EPUBError("Invalid EPUB: OPF path is empty")

        # Determine OPF directory for relative paths
        self._opf_dir = str(Path(self._opf_path).parent)
        if self._opf_dir == '.':
            self._opf_dir = ''

        # Parse OPF
        try:
            opf_data = self._zipfile.read(self._opf_path)
        except KeyError as e:
            raise EPUBError(f"Invalid EPUB: OPF file not found at {self._opf_path}") from e

        try:
            self._opf_root = ET.fromstring(opf_data)
        except ET.ParseError as e:
            raise EPUBError(f"Invalid EPUB: malformed OPF file: {e}") from e

        # Parse manifest
        self._parse_manifest()

        logger.debug(f"Opened EPUB with {len(self._manifest or {})} manifest items")

    def _parse_manifest(self) -> None:
        """Parse the OPF manifest into a dictionary."""
        self._manifest = {}

        if self._opf_root is None:
            return

        manifest = self._opf_root.find('opf:manifest', self.NAMESPACES)
        if manifest is None:
            manifest = self._opf_root.find('{*}manifest')

        if manifest is None:
            return

        for item in manifest:
            item_id = item.get('id', '')
            if item_id:
                self._manifest[item_id] = {
                    'id': item_id,
                    'href': item.get('href', ''),
                    'media-type': item.get('media-type', ''),
                }

    def _resolve_path(self, href: str) -> str:
        """Resolve a path relative to the OPF file.

        Args:
            href: Relative path from OPF

        Returns:
            Full path within the ZIP archive
        """
        if self._opf_dir:
            return f"{self._opf_dir}/{href}"
        return href

    def get_metadata(self) -> dict[str, str]:
        """Extract book metadata from OPF.

        Returns:
            Dictionary with title, creator, language, etc.
        """
        metadata: dict[str, str] = {}

        if self._opf_root is None:
            return metadata

        meta_elem = self._opf_root.find('opf:metadata', self.NAMESPACES)
        if meta_elem is None:
            meta_elem = self._opf_root.find('{*}metadata')

        if meta_elem is None:
            return metadata

        # Extract DC metadata
        for field in ['title', 'creator', 'language', 'identifier', 'publisher', 'date']:
            elem = meta_elem.find(f'dc:{field}', self.NAMESPACES)
            if elem is None:
                elem = meta_elem.find(f'{{http://purl.org/dc/elements/1.1/}}{field}')
            if elem is not None and elem.text:
                metadata[field] = elem.text.strip()

        return metadata

    def get_spine(self) -> list[dict[str, Any]]:
        """Get ordered list of spine items.

        Returns:
            List of dicts with 'href', 'id', 'media-type' for each spine item
        """
        if self._spine is not None:
            return self._spine

        self._spine = []

        if self._opf_root is None or self._manifest is None:
            return self._spine

        spine_elem = self._opf_root.find('opf:spine', self.NAMESPACES)
        if spine_elem is None:
            spine_elem = self._opf_root.find('{*}spine')

        if spine_elem is None:
            return self._spine

        for itemref in spine_elem:
            idref = itemref.get('idref', '')
            if idref and idref in self._manifest:
                item = self._manifest[idref].copy()
                self._spine.append(item)

        return self._spine

    def extract_text(self, spine_index: int) -> str:
        """Extract plain text from a spine item.

        Args:
            spine_index: Index of the spine item (0-based)

        Returns:
            Plain text content with HTML stripped

        Raises:
            IndexError: If spine_index is out of range
        """
        spine = self.get_spine()
        if spine_index < 0 or spine_index >= len(spine):
            raise IndexError(f"Spine index {spine_index} out of range (0-{len(spine)-1})")

        item = spine[spine_index]
        href = item['href']
        full_path = self._resolve_path(href)

        if self._zipfile is None:
            return ""

        try:
            content = self._zipfile.read(full_path)
        except KeyError:
            logger.warning(f"Spine item not found: {full_path}")
            return ""

        # Decode content
        try:
            text_content = content.decode('utf-8')
        except UnicodeDecodeError:
            try:
                text_content = content.decode('latin-1')
            except UnicodeDecodeError:
                logger.warning(f"Could not decode content from {full_path}")
                return ""

        return self._html_to_text(text_content)

    def _html_to_text(self, html_content: str) -> str:
        """Convert HTML content to plain text.

        Strips HTML tags while preserving text content and adding
        appropriate spacing between block elements.

        Args:
            html_content: HTML string

        Returns:
            Plain text with HTML stripped
        """
        # Try parsing as XML first (proper XHTML)
        try:
            root = ET.fromstring(html_content)
            return self._extract_text_from_element(root).strip()
        except ET.ParseError:
            pass

        # Fallback: regex-based stripping for malformed HTML
        return self._regex_strip_html(html_content)

    def _extract_text_from_element(self, elem: ET.Element) -> str:
        """Recursively extract text from an XML element.

        Args:
            elem: XML element

        Returns:
            Text content with proper spacing
        """
        # Get local tag name without namespace
        tag = elem.tag.split('}')[-1].lower() if '}' in elem.tag else elem.tag.lower()

        parts: list[str] = []

        # Add element's direct text
        if elem.text:
            parts.append(elem.text)

        # Process children
        for child in elem:
            child_text = self._extract_text_from_element(child)
            if child_text:
                parts.append(child_text)

            # Add tail text (text after child element)
            if child.tail:
                parts.append(child.tail)

        result = ''.join(parts)

        # Add spacing for block elements
        if tag in self.BLOCK_ELEMENTS:
            result = '\n\n' + result.strip() + '\n\n'

        return result

    def _regex_strip_html(self, html_content: str) -> str:
        """Strip HTML using regex (fallback for malformed HTML).

        Args:
            html_content: HTML string

        Returns:
            Plain text
        """
        # Remove script and style content
        text = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

        # Add newlines before block elements
        for tag in self.BLOCK_ELEMENTS:
            text = re.sub(f'<{tag}[^>]*>', '\n\n', text, flags=re.IGNORECASE)
            text = re.sub(f'</{tag}>', '\n\n', text, flags=re.IGNORECASE)

        # Remove remaining tags
        text = re.sub(r'<[^>]+>', '', text)

        # Decode HTML entities
        text = html.unescape(text)

        # Normalize whitespace
        text = re.sub(r'\n\s*\n', '\n\n', text)
        text = re.sub(r'[ \t]+', ' ', text)

        return text.strip()

    def get_chapter_title(self, spine_index: int) -> str | None:
        """Extract chapter title from a spine item.

        Looks for the first heading (h1-h6) in the content.

        Args:
            spine_index: Index of the spine item

        Returns:
            Chapter title string or None if not found
        """
        spine = self.get_spine()
        if spine_index < 0 or spine_index >= len(spine):
            return None

        item = spine[spine_index]
        href = item['href']
        full_path = self._resolve_path(href)

        if self._zipfile is None:
            return None

        try:
            content = self._zipfile.read(full_path)
        except KeyError:
            return None

        try:
            text_content = content.decode('utf-8')
        except UnicodeDecodeError:
            return None

        # Try XML parsing first
        try:
            root = ET.fromstring(text_content)
            return self._find_heading(root)
        except ET.ParseError:
            pass

        # Regex fallback
        match = re.search(r'<h[1-6][^>]*>([^<]+)</h[1-6]>', text_content, re.IGNORECASE)
        if match:
            return html.unescape(match.group(1)).strip()

        return None

    def _find_heading(self, elem: ET.Element) -> str | None:
        """Find the first heading in an element tree.

        Args:
            elem: Root element to search

        Returns:
            Heading text or None
        """
        # Check for h1-h6 elements
        for level in range(1, 7):
            for ns_prefix in ['', '{http://www.w3.org/1999/xhtml}']:
                heading = elem.find(f'.//{ns_prefix}h{level}')
                if heading is not None:
                    # Get all text content
                    text = ''.join(heading.itertext())
                    if text.strip():
                        return text.strip()

        return None

    def iter_content(self) -> Iterator[dict[str, Any]]:
        """Iterate over all spine items with extracted content.

        Yields:
            Dict with keys:
                - spine_index: int
                - spine_name: str (href)
                - text: str (extracted text)
                - chapter_title: str | None
        """
        spine = self.get_spine()

        for i, item in enumerate(spine):
            text = self.extract_text(i)
            chapter_title = self.get_chapter_title(i)

            yield {
                'spine_index': i,
                'spine_name': item['href'],
                'text': text,
                'chapter_title': chapter_title,
            }

    def close(self) -> None:
        """Close the EPUB file."""
        if self._zipfile is not None:
            self._zipfile.close()
            self._zipfile = None

    def __enter__(self) -> "EPUBExtractor":
        """Context manager entry."""
        return self

    def __exit__(self, *args: Any) -> None:
        """Context manager exit."""
        self.close()
