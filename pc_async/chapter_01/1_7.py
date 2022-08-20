"""
    Simple Event Loop
"""

from collections import deque


# Tasks
tasks = deque()
tasks.append("hello")
tasks.append("world")

while True:     # infinite loop
    if tasks:
        task = tasks.pop()
        print('Task:', task)
