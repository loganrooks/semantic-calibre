"""Vector store provider implementations.

Available backends:
- memory: In-memory store for testing and small datasets
- sqlite_vec: SQLite with vec extension for persistent storage
- chromadb: ChromaDB for production use
- faiss: Facebook AI Similarity Search

Each backend implements the VectorStore protocol defined in
calibre_semantic.core.types.
"""

from calibre_semantic.core.vectordb import (
    create_vector_store,
    get_available_backends,
    register_backend,
)

__all__ = [
    "create_vector_store",
    "get_available_backends",
    "register_backend",
]
