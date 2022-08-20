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
