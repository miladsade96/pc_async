"""
    Incorrectly using a blocking API in a coroutine
"""

import asyncio
import requests
from pc_async.utils.decorators import async_timed


@async_timed()
async def get_google_status() -> int:
    return requests.get("https://www.google.com").status_code


@async_timed()
async def main() -> None:
    task_1 = asyncio.create_task(get_google_status())
    task_2 = asyncio.create_task(get_google_status())
    task_3 = asyncio.create_task(get_google_status())

    await task_1
    await task_2
    await task_3


asyncio.run(main())
