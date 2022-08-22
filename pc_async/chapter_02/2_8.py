"""
    Running multiple tasks concurrently
"""

import asyncio
from pc_async.utils.delay_functions import delay


async def main():
    sleep_for_three = asyncio.create_task(delay(10))
    sleep_again = asyncio.create_task(delay(5))
    sleep_one_more = asyncio.create_task(delay(3))

    await sleep_for_three
    await sleep_again
    await sleep_one_more


asyncio.run(main())
