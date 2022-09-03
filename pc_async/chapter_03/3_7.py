"""
    Using selectors to build a non-blocking server
"""

import socket
import selectors
from selectors import SelectorKey
from typing import List, Tuple

selector = selectors.DefaultSelector()

server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ("127.0.0.1", 8000)
server_socket.setblocking(False)
server_socket.bind(server_address)
server_socket.listen()

selector.register(server_socket, selectors.EVENT_READ)

while True:
    # Creating a selector that will timeout after 1 second
    events: List[Tuple[SelectorKey, int]] = selector.select(timeout=1)
    if len(events) == 0:  # If there are no events, print it out. This happens when a timeout occurs
        print("No events, waiting a bit more!")
    for event, _ in events:
        event_socket = event.fileobj  # Get the socket for the event, which is sorted in the fileobj field
        if event_socket == server_socket:  # If the event_socket equals to server_socket, this is a connection attempt
            connection, address = server_socket.accept()
            connection.setblocking(False)
            print(f"I got a connection from {address}")
            # Registering the client that connected with our selector
            selector.register(connection, selectors.EVENT_READ)
        else:
            # If the event_socket is not the server_socket, receive data from client and echo it back
            data = event_socket.recv(1024)
            print(f"I got some data: {data}")
            event_socket.send(data)
