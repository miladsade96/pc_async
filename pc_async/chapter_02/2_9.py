"""
    Running code while other operations complete
"""

import asyncio
from pc_async.utils.delay_functions import delay


async def hello_every_second() -> None:
    """
    Print a message every second
    :return: None
    """
    for i in range(4):
        await asyncio.sleep(1)
        print("I am running other code while i am waiting.")


async def main() -> None:
    """
    The main function
    :return: None
    """
    first_delay = asyncio.create_task(delay(5))
    second_delay = asyncio.create_task(delay(5))
    await hello_every_second()
    await first_delay
    await second_delay


asyncio.run(main())
