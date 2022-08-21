"""
    Running two coroutines
"""

import asyncio
from pc_async.utils.delay_functions import delay


async def add_one(number: int) -> int:
    """
    Add one to the number
    :param number: number to add one to
    :return: number + 1
    """
    return number + 1


async def hello_world_message() -> str:
    """
    Return the message "Hello World"
    :return: "Hello World"
    """
    await delay(5)
    return "Hello World"


async def main() -> None:
    """
    Run the coroutines
    :return: None
    """
    message = await hello_world_message()   # Pause main until hello_world_message returns.
    one_plus_one = await add_one(1)         # Pause main until add_one returns.
    print(one_plus_one)
    print(message)


asyncio.run(main())
