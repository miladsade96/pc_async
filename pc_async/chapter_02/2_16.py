"""
    Timing two concurrent tasks with a decorator
"""

import asyncio
from pc_async.utils.decorators import async_timed


@async_timed()
async def delay(delay_seconds: int) -> int:
    print(f"Sleeping for {delay_seconds} seconds.")
    await asyncio.sleep(delay_seconds)
    print(f"Finished sleeping for {delay_seconds} seconds.")
    return delay_seconds


@async_timed()
async def main() -> None:
    task_1 = asyncio.create_task(delay(2))
    task_2 = asyncio.create_task(delay(3))

    await task_1
    await task_2


asyncio.run(main())
