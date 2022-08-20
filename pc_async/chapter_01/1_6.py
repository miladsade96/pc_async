"""
    Synchronously reading status codes
"""

import time
import requests
import threading


def read_status() -> None:
    """
    Read the website status code.
    :return: None
    """
    response = requests.get("https://elns.info")
    print(response.status_code)


# Synchronous section
sync_start = time.time()

read_status()
read_status()
read_status()
read_status()
read_status()

sync_end = time.time()
print(f"running synchronously took {sync_end - sync_start:.4f} seconds.")

# ----------------------------------------------------------------------------------

# Multi-threading section
thread_1 = threading.Thread(target=read_status)
thread_2 = threading.Thread(target=read_status)
thread_3 = threading.Thread(target=read_status)
thread_4 = threading.Thread(target=read_status)
thread_5 = threading.Thread(target=read_status)


thread_start = time.time()

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
thread_5.start()

print("All threads are running!")

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()
thread_5.join()

thread_end = time.time()

print(f"Running with threads took {thread_end - thread_start:.4f} seconds.")
