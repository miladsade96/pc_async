"""
    Creating a task
"""

import asyncio
from pc_async.utils.delay_functions import delay


async def main():
    sleep_for_three = asyncio.create_task(delay(3))
    print(f"type(sleep_for_three) = {type(sleep_for_three)}")
    result = await sleep_for_three
    print(f"result = {result}")

asyncio.run(main())
