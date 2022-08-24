"""
    The basics of futures
"""

from asyncio import Future


my_future = Future()    # Defining a future
print(f"Is my_future done? {my_future.done()}")

my_future.set_result(42)    # Setting the result
print(f"Is my_future done? {my_future.done()}")
print(f"What is the result of my_future? {my_future.result()}")
