import time
from functools import wraps
from typing import TypeVar, Callable, Optional
import logging

T = TypeVar('T')

def retry(
    max_retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: tuple = (Exception,),
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """
    Retry decorator with exponential backoff.
    
    Args:
        max_retries: Maximum number of retry attempts
        delay: Initial delay between retries in seconds
        backoff: Multiplier for delay after each retry
        exceptions: Tuple of exceptions to catch
        
    Returns:
        Decorated function that will retry on specified exceptions
    """
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> T:
            retry_count = 0
            cur_delay = delay
            
            while True:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    retry_count += 1
                    if retry_count >= max_retries:
                        raise
                    
                    logging.warning(
                        f"Retry {retry_count}/{max_retries} for {func.__name__} "
                        f"after error: {str(e)}. Waiting {cur_delay}s..."
                    )
                    
                    time.sleep(cur_delay)
                    cur_delay *= backoff
                    
        return wrapper
    return decorator
