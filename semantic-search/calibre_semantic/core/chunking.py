"""Text chunking strategies for semantic search.

This module provides strategies for splitting book text into chunks
suitable for embedding. Strategies include:

1. SemanticChunkingStrategy - Respects paragraph and sentence boundaries
2. FixedSizeChunkingStrategy - Simple fixed-size chunks with overlap

Usage:
    >>> from calibre_semantic.core.chunking import create_chunking_strategy
    >>> from calibre_semantic.core.types import ChunkingConfig
    >>> config = ChunkingConfig(strategy="semantic", target_size=512)
    >>> strategy = create_chunking_strategy(config)
    >>> chunks = list(strategy.chunk(text, book_id, 0, "chapter1.xhtml"))
"""

from __future__ import annotations

import hashlib
import re
from abc import ABC, abstractmethod
from typing import Iterator

from calibre_semantic.core.types import (
    BookIdentifier,
    ChunkingConfig,
    ChunkLocation,
    ChunkType,
    TextChunk,
)


def _generate_chunk_id(
    book_id: BookIdentifier,
    spine_index: int,
    start_offset: int,
    text_hash: str,
) -> str:
    """Generate a deterministic chunk ID.

    Args:
        book_id: The source book identifier
        spine_index: Index in spine
        start_offset: Character offset in spine item
        text_hash: Hash of the chunk text

    Returns:
        Deterministic chunk ID string
    """
    content = f"{book_id}:{spine_index}:{start_offset}:{text_hash}"
    return hashlib.sha256(content.encode()).hexdigest()[:16]


def _hash_text(text: str) -> str:
    """Generate a short hash of text content."""
    return hashlib.md5(text.encode()).hexdigest()[:8]


class BaseChunkingStrategy(ABC):
    """Base class for chunking strategies."""

    def __init__(self, config: ChunkingConfig):
        """Initialize with configuration.

        Args:
            config: Chunking configuration
        """
        self._config = config

    @property
    def target_chunk_size(self) -> int:
        """Target size for chunks in characters."""
        return self._config.target_size

    @property
    def chunk_overlap(self) -> int:
        """Overlap between consecutive chunks in characters."""
        return self._config.overlap

    @abstractmethod
    def chunk(
        self,
        text: str,
        book_id: BookIdentifier,
        spine_index: int,
        spine_name: str,
        chapter_title: str | None = None,
    ) -> Iterator[TextChunk]:
        """Split text into chunks.

        Args:
            text: The text to chunk
            book_id: Source book identifier
            spine_index: Index in EPUB spine or page number
            spine_name: Spine item filename
            chapter_title: Optional chapter title

        Yields:
            TextChunk objects
        """
        ...


class SemanticChunkingStrategy(BaseChunkingStrategy):
    """Chunking strategy that respects paragraph and sentence boundaries.

    This strategy attempts to create chunks that align with natural
    text boundaries (paragraphs first, then sentences). When a paragraph
    is too long, it falls back to sentence splitting.
    """

    # Regex patterns for boundary detection
    _PARAGRAPH_PATTERN = re.compile(r"\n\s*\n")
    _SENTENCE_PATTERN = re.compile(r"(?<=[.!?])\s+(?=[A-Z])")

    def chunk(
        self,
        text: str,
        book_id: BookIdentifier,
        spine_index: int,
        spine_name: str,
        chapter_title: str | None = None,
    ) -> Iterator[TextChunk]:
        """Split text into chunks respecting paragraph/sentence boundaries.

        Args:
            text: The text to chunk
            book_id: Source book identifier
            spine_index: Index in EPUB spine
            spine_name: Spine item filename
            chapter_title: Optional chapter title

        Yields:
            TextChunk objects aligned to natural boundaries
        """
        # Handle empty or whitespace-only text
        if not text or not text.strip():
            return

        # Split into paragraphs
        paragraphs = self._split_paragraphs(text)

        current_chunk_text = ""
        current_start_offset = 0
        chunk_start_in_text = 0

        for para_text, para_start in paragraphs:
            para_text = para_text.strip()
            if not para_text:
                continue

            # If adding this paragraph would exceed target size
            if current_chunk_text and len(current_chunk_text) + len(para_text) + 2 > self.target_chunk_size:
                # Yield current chunk
                yield self._create_chunk(
                    text=current_chunk_text,
                    book_id=book_id,
                    spine_index=spine_index,
                    spine_name=spine_name,
                    start_offset=current_start_offset,
                    chapter_title=chapter_title,
                    chunk_type=ChunkType.PARAGRAPH,
                )

                # Handle overlap
                if self.chunk_overlap > 0:
                    overlap_text = self._get_overlap_text(current_chunk_text)
                    current_chunk_text = overlap_text + "\n\n" + para_text if overlap_text else para_text
                    # Approximate new start offset (overlap means we go back a bit)
                    current_start_offset = max(0, para_start - len(overlap_text))
                else:
                    current_chunk_text = para_text
                    current_start_offset = para_start
            elif len(para_text) > self.target_chunk_size:
                # Paragraph too long, need to split at sentences
                if current_chunk_text:
                    # First yield what we have
                    yield self._create_chunk(
                        text=current_chunk_text,
                        book_id=book_id,
                        spine_index=spine_index,
                        spine_name=spine_name,
                        start_offset=current_start_offset,
                        chapter_title=chapter_title,
                        chunk_type=ChunkType.PARAGRAPH,
                    )
                    current_chunk_text = ""

                # Split long paragraph into sentence-based chunks
                yield from self._split_long_paragraph(
                    para_text=para_text,
                    para_start=para_start,
                    book_id=book_id,
                    spine_index=spine_index,
                    spine_name=spine_name,
                    chapter_title=chapter_title,
                )
                current_start_offset = para_start + len(para_text)
            else:
                # Add paragraph to current chunk
                if current_chunk_text:
                    current_chunk_text += "\n\n" + para_text
                else:
                    current_chunk_text = para_text
                    current_start_offset = para_start

        # Yield remaining text
        if current_chunk_text.strip():
            yield self._create_chunk(
                text=current_chunk_text,
                book_id=book_id,
                spine_index=spine_index,
                spine_name=spine_name,
                start_offset=current_start_offset,
                chapter_title=chapter_title,
                chunk_type=ChunkType.PARAGRAPH,
            )

    def _split_paragraphs(self, text: str) -> list[tuple[str, int]]:
        """Split text into paragraphs with their start offsets.

        Args:
            text: Text to split

        Returns:
            List of (paragraph_text, start_offset) tuples
        """
        paragraphs = []
        current_pos = 0

        parts = self._PARAGRAPH_PATTERN.split(text)
        for part in parts:
            if part.strip():
                # Find actual position in original text
                start = text.find(part, current_pos)
                if start == -1:
                    start = current_pos
                paragraphs.append((part, start))
                current_pos = start + len(part)

        return paragraphs

    def _split_long_paragraph(
        self,
        para_text: str,
        para_start: int,
        book_id: BookIdentifier,
        spine_index: int,
        spine_name: str,
        chapter_title: str | None,
    ) -> Iterator[TextChunk]:
        """Split a long paragraph at sentence boundaries.

        Args:
            para_text: The paragraph text
            para_start: Start offset of paragraph in source
            book_id: Source book identifier
            spine_index: Spine index
            spine_name: Spine item name
            chapter_title: Optional chapter title

        Yields:
            TextChunk objects split at sentence boundaries
        """
        sentences = self._split_sentences(para_text)

        current_chunk_text = ""
        current_start_offset = para_start

        for sent_text, sent_rel_offset in sentences:
            if not sent_text.strip():
                continue

            # If adding this sentence would exceed target
            if current_chunk_text and len(current_chunk_text) + len(sent_text) + 1 > self.target_chunk_size:
                yield self._create_chunk(
                    text=current_chunk_text,
                    book_id=book_id,
                    spine_index=spine_index,
                    spine_name=spine_name,
                    start_offset=current_start_offset,
                    chapter_title=chapter_title,
                    chunk_type=ChunkType.SENTENCE,
                )

                # Handle overlap
                if self.chunk_overlap > 0:
                    overlap_text = self._get_overlap_text(current_chunk_text)
                    current_chunk_text = overlap_text + " " + sent_text if overlap_text else sent_text
                    current_start_offset = para_start + sent_rel_offset - len(overlap_text)
                else:
                    current_chunk_text = sent_text
                    current_start_offset = para_start + sent_rel_offset
            else:
                # Add sentence to current chunk
                if current_chunk_text:
                    current_chunk_text += " " + sent_text
                else:
                    current_chunk_text = sent_text
                    current_start_offset = para_start + sent_rel_offset

        # Yield remaining
        if current_chunk_text.strip():
            yield self._create_chunk(
                text=current_chunk_text,
                book_id=book_id,
                spine_index=spine_index,
                spine_name=spine_name,
                start_offset=current_start_offset,
                chapter_title=chapter_title,
                chunk_type=ChunkType.SENTENCE,
            )

    def _split_sentences(self, text: str) -> list[tuple[str, int]]:
        """Split text into sentences with relative offsets.

        Args:
            text: Text to split

        Returns:
            List of (sentence_text, relative_offset) tuples
        """
        sentences = []
        current_pos = 0

        parts = self._SENTENCE_PATTERN.split(text)
        for part in parts:
            if part.strip():
                start = text.find(part, current_pos)
                if start == -1:
                    start = current_pos
                sentences.append((part.strip(), start))
                current_pos = start + len(part)

        return sentences

    def _get_overlap_text(self, text: str) -> str:
        """Get overlap text from the end of a chunk.

        Args:
            text: The chunk text

        Returns:
            Text to include as overlap in next chunk
        """
        if len(text) <= self.chunk_overlap:
            return text

        # Try to break at a sentence boundary within overlap region
        overlap_region = text[-self.chunk_overlap * 2:]
        sentences = self._SENTENCE_PATTERN.split(overlap_region)

        if len(sentences) > 1:
            # Return last complete sentence(s) up to overlap size
            result = ""
            for sent in reversed(sentences):
                if len(result) + len(sent) <= self.chunk_overlap:
                    result = sent + " " + result if result else sent
                else:
                    break
            return result.strip()

        # No sentence boundary, just take last N characters
        return text[-self.chunk_overlap:]

    def _create_chunk(
        self,
        text: str,
        book_id: BookIdentifier,
        spine_index: int,
        spine_name: str,
        start_offset: int,
        chapter_title: str | None,
        chunk_type: ChunkType,
    ) -> TextChunk:
        """Create a TextChunk with proper metadata.

        Args:
            text: Chunk text content
            book_id: Source book identifier
            spine_index: Spine index
            spine_name: Spine item name
            start_offset: Start offset in source
            chapter_title: Optional chapter title
            chunk_type: Type of chunk

        Returns:
            TextChunk instance
        """
        text_hash = _hash_text(text)
        chunk_id = _generate_chunk_id(book_id, spine_index, start_offset, text_hash)

        return TextChunk(
            id=chunk_id,
            book_id=book_id,
            text=text,
            location=ChunkLocation(
                spine_index=spine_index,
                spine_name=spine_name,
                start_offset=start_offset,
                end_offset=start_offset + len(text),
            ),
            chunk_type=chunk_type,
            chapter_title=chapter_title,
        )


class FixedSizeChunkingStrategy(BaseChunkingStrategy):
    """Simple fixed-size chunking with overlap.

    Splits text into fixed-size chunks, attempting to break at word
    boundaries when possible.
    """

    def chunk(
        self,
        text: str,
        book_id: BookIdentifier,
        spine_index: int,
        spine_name: str,
        chapter_title: str | None = None,
    ) -> Iterator[TextChunk]:
        """Split text into fixed-size chunks.

        Args:
            text: The text to chunk
            book_id: Source book identifier
            spine_index: Index in EPUB spine
            spine_name: Spine item filename
            chapter_title: Optional chapter title

        Yields:
            TextChunk objects of approximately target_size
        """
        if not text or not text.strip():
            return

        text = text.strip()
        text_len = len(text)

        if text_len <= self.target_chunk_size:
            # Text fits in single chunk
            yield self._create_chunk(
                text=text,
                book_id=book_id,
                spine_index=spine_index,
                spine_name=spine_name,
                start_offset=0,
                chapter_title=chapter_title,
            )
            return

        current_pos = 0

        while current_pos < text_len:
            # Calculate end position
            end_pos = min(current_pos + self.target_chunk_size, text_len)

            # Try to break at word boundary if not at end
            if end_pos < text_len:
                # Look for space within last 20% of chunk
                search_start = max(current_pos, end_pos - self.target_chunk_size // 5)
                last_space = text.rfind(" ", search_start, end_pos)
                if last_space > current_pos:
                    end_pos = last_space

            chunk_text = text[current_pos:end_pos].strip()

            if chunk_text:
                yield self._create_chunk(
                    text=chunk_text,
                    book_id=book_id,
                    spine_index=spine_index,
                    spine_name=spine_name,
                    start_offset=current_pos,
                    chapter_title=chapter_title,
                )

            # Move position, accounting for overlap
            if end_pos >= text_len:
                break

            current_pos = end_pos - self.chunk_overlap
            if current_pos >= end_pos:
                # Prevent infinite loop
                current_pos = end_pos

    def _create_chunk(
        self,
        text: str,
        book_id: BookIdentifier,
        spine_index: int,
        spine_name: str,
        start_offset: int,
        chapter_title: str | None,
    ) -> TextChunk:
        """Create a TextChunk with proper metadata."""
        text_hash = _hash_text(text)
        chunk_id = _generate_chunk_id(book_id, spine_index, start_offset, text_hash)

        return TextChunk(
            id=chunk_id,
            book_id=book_id,
            text=text,
            location=ChunkLocation(
                spine_index=spine_index,
                spine_name=spine_name,
                start_offset=start_offset,
                end_offset=start_offset + len(text),
            ),
            chunk_type=ChunkType.PARAGRAPH,
            chapter_title=chapter_title,
        )


def create_chunking_strategy(config: ChunkingConfig) -> BaseChunkingStrategy:
    """Factory function to create chunking strategies.

    Args:
        config: Chunking configuration

    Returns:
        Appropriate chunking strategy instance

    Raises:
        ValueError: If strategy name is unknown
    """
    strategy_map = {
        "semantic": SemanticChunkingStrategy,
        "fixed": FixedSizeChunkingStrategy,
    }

    strategy_class = strategy_map.get(config.strategy)
    if strategy_class is None:
        raise ValueError(
            f"Unknown chunking strategy: {config.strategy}. "
            f"Available: {list(strategy_map.keys())}"
        )

    return strategy_class(config)
