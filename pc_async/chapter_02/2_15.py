"""
    A decorator for timing coroutines
"""

from time import time
from functools import wraps
from typing import Any, Callable


def async_timed():
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f"Starting {func} with args {args} {kwargs}")
            start = time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time()
                total = end - start
                print(f"Finished {func} in {total:.4f} second(s)")
        return wrapped
    return wrapper
