import openai
from typing import List, Optional, Dict, Any
from .base import AbstractEmbedder
from calibre.utils.config import JSONConfig
from calibre.db.backend import Connection
from calibre.utils.retry import retry
from calibre.utils.rate_limit import RateLimiter

class OpenAIEmbedder(AbstractEmbedder):
    """OpenAI API-based text embedding provider."""
    
    def __init__(self, config: JSONConfig, db: Connection):
        super().__init__(config, db)
        self._setup_openai()
        self.rate_limiter = RateLimiter(requests_per_minute=3500)
        
    def _setup_openai(self) -> None:
        """Initialize OpenAI client with configured API key"""
        api_key = self.config.get('api_key')
        if not api_key:
            raise ValueError("OpenAI API key not configured")
            
        openai.api_key = api_key
        self.model = self.config.get('model_version', 'text-embedding-3-small')
        
    @property
    def model_id(self) -> str:
        return f"openai:{self.model}"
        
    @retry(max_retries=3, delay=1.0)
    def embed_text(self, text: str, section: str) -> List[float]:
        """Generate embedding for a single text segment"""
        with self.rate_limiter:
            response = openai.Embedding.create(
                input=text,
                model=self.model
            )
            return response['data'][0]['embedding']
            
    @retry(max_retries=3, delay=1.0)
    def batch_embed(self, texts: List[str], sections: List[str]) -> List[List[float]]:
        """Batch process embeddings with rate limiting"""
        if len(texts) > 2048:
            raise ValueError("OpenAI batch size limit exceeded")
            
        with self.rate_limiter:
            response = openai.Embedding.create(
                input=texts,
                model=self.model
            )
            return [item['embedding'] for item in response['data']]
            
    @classmethod
    def get_config_template(cls) -> Dict[str, Any]:
        """Extended configuration options for OpenAI"""
        base = super().get_config_template()
        base.update({
            "api_key": "",
            "model_version": "text-embedding-3-small",
            "organization": "",
            "timeout": 30.0
        })
        return base