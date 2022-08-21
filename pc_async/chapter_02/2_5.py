"""
    First application with sleep
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


async def hello_world_message() -> str:
    """
    Return hello world message
    :return: hello world message
    """
    await asyncio.sleep(1)      # pause for 1 second
    return "Hello World"


async def main() -> None:
    """
    Main function
    :return: None
    """
    message = await hello_world_message()   # pause main until hello_world_message is done
    print(message)


asyncio.run(main())
