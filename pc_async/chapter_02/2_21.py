"""
    Accessing the event loop
"""

import asyncio
from pc_async.utils.delay_functions import delay


def call_later():
    print("I am being cancelled in the future.")


async def main():
    loop = asyncio.get_running_loop()
    loop.call_soon(call_later)
    await delay(1)


asyncio.run(main())
