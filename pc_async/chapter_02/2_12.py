"""
    Shielding a task from cancellation
"""

import asyncio
from pc_async.utils.delay_functions import delay


async def main() -> None:
    task = asyncio.create_task(delay(10))

    try:
        result = await asyncio.wait_for(asyncio.shield(task), timeout=5)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print("Task took longer than 5 seconds, It will finish soon.")
        result = await task
        print(result)


asyncio.run(main())
