"""
    Starting a server and listening for a connection
"""

import socket

# Creating a tcp server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8000)    # Setting the address of the socket
server_socket.bind(server_address)
server_socket.listen()      # Listening for connection

connection, client_address = server_socket.accept()     # Waiting for a connection
print(f"I got a connection from {client_address}")
