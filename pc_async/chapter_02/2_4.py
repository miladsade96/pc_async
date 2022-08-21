"""
    Using await to wait for the result of coroutine
"""

import asyncio


async def add_one(number: int) -> int:
    """
    Add 1 to the number
    :param number: int
    :return: int
    """
    return number + 1


async def main() -> None:
    """
    Main function
    :return: None
    """
    one_plus_one = await add_one(1)     # pause and wait for the result of add_one(1)
    two_plus_one = await add_one(2)     # pause and wait for the result of add_one(2)
    print(f"one_plus_one: {one_plus_one}")
    print(f"two_plus_one: {two_plus_one}")


asyncio.run(main())
