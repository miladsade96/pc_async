"""
    Comparing coroutine to normal functions
"""


async def coroutine_add_one(number: int) -> int:
    """
    Coroutine add one
    :param number: int
    :return: int
    """
    return number + 1


def normal_add_one(number: int) -> int:
    """
    Normal add one
    :param number: int
    :return: int
    """
    return number + 1
