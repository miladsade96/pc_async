"""
    I/O-bound and CPU-bound operations
"""

import requests

response = requests.get('https://www.elns.info')    # I/O-bound web request
items = response.headers.items()
headers = [f"{key}: {header}" for key, header in items]   # CPU-bound response processing
formatted_headers = '\n'.join(headers)  # CPU-bound string concatenation

with open('1_1.txt', 'w') as f:
    f.write(formatted_headers)
