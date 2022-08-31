"""
    Allowing multiple connections and the dangers of blocking
"""

import socket


# Creating a tcp server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8000)    # Setting the address of the socket
server_socket.bind(server_address)
server_socket.listen()      # Listening for connection

connections = list()

try:
    while True:
        connection, client_address = server_socket.accept()
        print(f"I got a connection from {client_address}")
        connections.append(connection)

        for connection in connections:
            buffer = b''
            while buffer[-2:] != b'\r\n':
                data = connection.recv(2)
                if not data:
                    break
                else:
                    print(f"I got a data {data}")
                    buffer += data
            print(f"All the data is {buffer}")
            connection.send(buffer)
finally:
    server_socket.close()
