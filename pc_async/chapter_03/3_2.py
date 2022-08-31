"""
    Reading data from a socket and write back to the client
"""

import socket

# Creating a tcp server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8000)    # Setting the address of the socket
server_socket.bind(server_address)
server_socket.listen()      # Listening for connection

try:
    connection, client_address = server_socket.accept()
    print(f"I got a connection from {client_address}")

    buffer = b''

    while buffer[-2:] != b'\r\n':
        data = connection.recv(2)   # Trying to receive two bytes
        if not data:
            break
        else:
            print(f"I got data {data}")
            buffer += data  # Storing in buffer

    print(f"All the data is {buffer}")
    connection.sendall(buffer)      # Write data back to the client
finally:
    server_socket.close()
