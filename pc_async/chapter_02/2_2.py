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


# Comparison section
function_result = normal_add_one(1)
coroutine_result = coroutine_add_one(1)

print(f"Function result is {function_result} and the type is {type(function_result)}")
print(f"Coroutine result is {coroutine_result} and the type is {type(coroutine_result)}")
