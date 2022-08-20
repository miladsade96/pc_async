"""
    Creating a multithreaded Python application
"""

import threading


def hello_from_thread() -> None:
    """
    Print hello from thread function
    :return: None
    """
    print(f"Hello from thread {threading.current_thread()}!")
