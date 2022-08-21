"""
    Delay functions for asyncio.
"""

import asyncio


async def delay(delay_seconds: int) -> int:
    """
    Delay for delay_seconds seconds
    :param delay_seconds: number of seconds to delay
    :return: number of seconds delayed
    """
    print(f"Sleeping for {delay_seconds} seconds.")
    await asyncio.sleep(delay_seconds)
    print(f"Done sleeping for {delay_seconds} seconds.")
    return delay_seconds
