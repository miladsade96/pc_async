"""
    Awaiting a future
"""

from asyncio import run, sleep, Future, create_task


def make_request() -> Future:
    future = Future()
    # Create a task to asynchronously to set the value of the future
    create_task(set_future_value(future))
    return future


async def set_future_value(future) -> None:
    await sleep(1)  # wait 1 second before setting the value of the future
    future.set_result(42)


async def main() -> None:
    future = make_request()
    print(f"Is the future done? {future.done()}")
    value = await future    # pause main until future's value is set
    print(f"Is the future done? {future.done()}")
    print(value)


run(main())
