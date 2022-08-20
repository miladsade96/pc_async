"""
    Synchronously reading status codes
"""

import time
import requests


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
