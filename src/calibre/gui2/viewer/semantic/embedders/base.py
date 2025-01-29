from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List
from calibre.utils.config import JSONConfig
from calibre.utils.sqlite import Connection

class AbstractEmbedder(ABC):
    """Base class for text embedding providers with caching capabilities."""
    
    #: Configuration namespace for this embedder
    config_namespace = 'semantic_embedder'
    
    def __init__(self, config: JSONConfig, db: Connection):
        self.config = config
        self.db = db
        self._setup_schema()
        
    def _setup_schema(self) -> None:
        """Initialize required database tables"""
        with self.db:
            self.db.execute('''
                CREATE TABLE IF NOT EXISTS embeddings (
                    id INTEGER PRIMARY KEY,
                    model_id TEXT NOT NULL,
                    text_hash TEXT NOT NULL,
                    section TEXT NOT NULL,
                    embedding BLOB NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    UNIQUE(model_id, text_hash, section)
                )
            ''')
            
            self.db.execute('''
                CREATE TABLE IF NOT EXISTS model_configs (
                    model_id TEXT PRIMARY KEY,
                    config_json TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
        
    @property
    @abstractmethod
    def model_id(self) -> str:
        """Unique identifier for model/configuration combination"""
        pass
        
    @abstractmethod
    def embed_text(self, text: str, section: str) -> List[float]:
        """
        Generate embedding for text within a document section.
        
        :param text: Normalized text content
        :param section: Structural context (e.g. 'body', 'footnote')
        :return: List of floats representing the embedding vector
        """
        pass
        
    @abstractmethod
    def batch_embed(self, texts: List[str], sections: List[str]) -> List[List[float]]:
        """
        Batch process embeddings with section context.
        Optimized for GPU-based implementations.
        """
        pass
        
    def get_cache_key(self, text: str, section: str) -> str:
        """Generate stable cache key combining model, text hash, and section"""
        return f"{self.model_id}|{hash(text)}|{section}"
        
    def get_cached(self, key: str) -> Optional[List[float]]:
        """Retrieve cached embedding if available"""
        model_id, text_hash, section = key.split('|')
        row = self.db.execute('''
            SELECT embedding FROM embeddings
            WHERE model_id = ? AND text_hash = ? AND section = ?
        ''', (model_id, text_hash, section)).fetchone()
        
        return list(map(float, row[0].split(b','))) if row else None
        
    def set_cache(self, key: str, embedding: List[float]) -> None:
        """Store embedding in database cache"""
        model_id, text_hash, section = key.split('|')
        embedding_bytes = b','.join(map(str.encode, map(str, embedding)))
        self.db.execute('''
            INSERT OR REPLACE INTO embeddings
            (model_id, text_hash, section, embedding)
            VALUES (?, ?, ?, ?)
        ''', (model_id, text_hash, section, embedding_bytes))
        
    @classmethod
    def get_config_template(cls) -> Dict[str, Any]:
        """Configuration schema for embedder-specific settings"""
        return {
            "api_key": "",  # For cloud-based providers
            "model_version": "default",
            "batch_size": 32,
            "gpu_acceleration": False
        }