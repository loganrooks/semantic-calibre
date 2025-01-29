from threading import Lock
import time
from typing import Optional, Callable
from contextlib import contextmanager

class RateLimiter:
    """Thread-safe rate limiter with configurable requests per minute."""
    
    def __init__(self, requests_per_minute: int):
        """
        Initialize rate limiter.
        
        Args:
            requests_per_minute: Maximum number of requests allowed per minute
        """
        self.rate = requests_per_minute
        self.min_interval = 60.0 / requests_per_minute
        self.last_check = 0.0
        self._lock = Lock()
        self._last_reset = time.monotonic()
        self._num_calls = 0
    
    @contextmanager 
    def __call__(self):
        """Context manager for rate limiting."""
        with self._lock:
            now = time.monotonic()
            
            # Reset counter if minute has elapsed
            if now - self._last_reset >= 60.0:
                self._last_reset = now
                self._num_calls = 0
            
            # Check if we've exceeded rate
            if self._num_calls >= self.rate:
                sleep_time = 60.0 - (now - self._last_reset)
                if sleep_time > 0:
                    time.sleep(sleep_time)
                self._last_reset = time.monotonic()
                self._num_calls = 0
            
            # Calculate delay needed since last call
            elapsed = now - self.last_check
            if elapsed < self.min_interval:
                time.sleep(self.min_interval - elapsed)
            
            self.last_check = time.monotonic()
            self._num_calls += 1
            
            try:
                yield
            finally:
                pass
