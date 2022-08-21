"""
    Running a coroutine
"""

import asyncio


# Defining a coroutine
async def coroutine_add_one(number: int) -> int:
    """
    Add one to the number
    :param number: int
    :return: int
    """
    return number + 1


# Running a coroutine
result = asyncio.run(coroutine_add_one(1))
print(result)
