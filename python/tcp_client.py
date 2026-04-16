import socket

# AF_INET uses IPv4 addresses (like 127.0.0.1).
# SOCK_STREAM uses TCP.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Dial the server. 127.0.0.1 means localhost or this same computer.
client_socket.connect(('127.0.0.1', 5000))

# Send bytes. encode() turns a string into bytes.
client_socket.sendall("Hello, server!".encode())

# Wait for up to 1024 bytes back.
response = client_socket.recv(1024)
print(f"Server said: {response.decode()}")

client_socket.close()
