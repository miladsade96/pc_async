"""
    Creating a non-blocking socket
"""

import socket


# Creating a tcp server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8000)    # Setting the address of the socket
server_socket.bind(server_address)
server_socket.listen()      # Listening for connection
server_socket.setblocking(False)
