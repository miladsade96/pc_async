"""
    Attempting to run CPU-bound code concurrently
"""

import asyncio
from pc_async.utils.delay_functions import delay
from pc_async.utils.decorators import async_timed
