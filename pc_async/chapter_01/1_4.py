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
