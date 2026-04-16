import socket

# AF_INET uses IPv4 addresses (like 127.0.0.1).
# SOCK_STREAM uses TCP.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Claim port 5000 on this machine. '' means any network interface.
server_socket.bind(('', 5000))

# Start listening. The 1 means queue up to 1 pending connection.
server_socket.listen(1)
print("Server listening on port 5000...")

while True:
    # accept() waits until a client connects and returns a new socket just for talking to that client.
    client_socket, client_address = server_socket.accept()
    print(f"Connected to {client_address}")

    # Read up to 1024 bytes from the client.
    data = client_socket.recv(1024)
    print(f"Received: {data.decode()}")

    # Send the same data back.
    client_socket.sendall(data)

    # Hang up on this client. The server loop continues for the next one.
    client_socket.close()
