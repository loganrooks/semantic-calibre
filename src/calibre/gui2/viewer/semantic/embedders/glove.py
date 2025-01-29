import numpy as np
from typing import List, Dict, Any, Optional
from pathlib import Path
import mmap
from collections import defaultdict

from calibre.utils.config import JSONConfig
from calibre.db.backend import Connection
from .base import AbstractEmbedder

class GloVeEmbedder(AbstractEmbedder):
    """GloVe-based text embedding provider with memory mapping."""
    
    def __init__(self, config: JSONConfig, db: Connection):
        super().__init__(config, db)
        self.vectors = {}
        self.vector_dim = 300  # Default GloVe dimension
        self.model_path = Path(config.get('model_path', ''))
        self._load_vectors()
        
    def _load_vectors(self) -> None:
        """Load GloVe vectors with memory mapping"""
        if not self.model_path.exists():
            raise ValueError(f"GloVe model not found at {self.model_path}")
            
        # Memory map the vectors file
        with open(self.model_path, 'rb') as f:
            self.mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            
        # Load word index
        index_path = self.model_path.with_suffix('.index')
        if index_path.exists():
            self.word_index = np.load(index_path, allow_pickle=True).item()
        else:
            self._build_index()
            
    def _build_index(self) -> None:
        """Build word index for fast vector lookup"""
        self.word_index = {}
        offset = 0
        while offset < self.mm.size():
            self.mm.seek(offset)
            line = self.mm.readline()
            word = line.split(b' ')[0].decode('utf-8')
            self.word_index[word] = offset
            offset = self.mm.tell()
            
        # Save index for future use - Convert to numpy array first
        word_index_array = np.array([(k,v) for k,v in self.word_index.items()], 
                                dtype=[('word', 'U100'), ('offset', 'int64')])
        np.save(self.model_path.with_suffix('.index'), word_index_array)

    def _get_vector(self, word: str) -> np.ndarray:
        """Get vector for single word"""
        if word not in self.word_index:
            return np.zeros(self.vector_dim)
            
        self.mm.seek(self.word_index[word])
        line = self.mm.readline().decode('utf-8')
        values = line.split(' ')[1:]
        return np.array([float(x) for x in values])
    
    @property
    def model_id(self) -> str:
        return f"glove:{self.model_path.stem}"
        
    def preprocess_text(self, text: str) -> List[str]:
        """Basic text preprocessing"""
        return text.lower().split()
        
    def embed_text(self, text: str, section: str) -> List[float]:
        """Generate embedding for text segment"""
        with self.rate_limiter:
            # Include section context in embedding
            section_prefix = section.lower().split() if section else []
            words = section_prefix + self.preprocess_text(text)
            if not words:
                return [0.0] * self.vector_dim
                
            vectors = [self._get_vector(word) for word in words]
            # Average word vectors with section context
            embedding = np.mean(vectors, axis=0)
            return embedding.tolist()
            
    def batch_embed(self, texts: List[str], sections: List[str]) -> List[List[float]]:
        """Batch process embeddings"""
        with self.rate_limiter:
            results = []
            for text, section in zip(texts, sections):
                results.append(self.embed_text(text, section))
            return results
            
    @classmethod
    def get_config_template(cls) -> Dict[str, Any]:
        """Configuration options"""
        base = super().get_config_template()
        base.update({
            "model_path": "",
            "vector_dim": 300,
            "case_sensitive": False
        })
        return base