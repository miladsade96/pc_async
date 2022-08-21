"""
    First application with sleep
"""
import asyncio


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
