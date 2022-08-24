"""
    Incorrectly using a blocking API in a coroutine
"""

import asyncio
import requests
from pc_async.utils.decorators import async_timed
