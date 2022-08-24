"""
    Creating a timeout for a task with wait_for
"""

import asyncio
from pc_async.utils.delay_functions import delay


async def main() -> None:
    delay_task = asyncio.create_task(delay(3))
    try:
        result = await asyncio.wait_for(delay_task, timeout=1)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print("Got a timeout")
        print(f"Was the task cancelled? {delay_task.cancelled()}")


asyncio.run(main())
