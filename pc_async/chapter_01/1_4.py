"""
    Creating multiple processes
"""

import os
import multiprocessing


def hello_from_process() -> None:
    """
    Print hello from process
    :return: None
    """
    print(f"Hello from child process {os.getpid()}!")


# Multi-Processing section
if __name__ == '__main__':
    hello_process = multiprocessing.Process(target=hello_from_process)
    hello_process.start()
    print(f"Hello from parent process {os.getpid()}!")
    hello_process.join()
