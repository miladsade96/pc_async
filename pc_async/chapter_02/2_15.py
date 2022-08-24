"""
    A decorator for timing coroutines
"""

from time import time
from functools import wraps
from typing import Any, Callable
