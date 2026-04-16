import socket

# SOCK_DGRAM uses UDP.
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# No connection, just shoot a packet at the server.
client.sendto("Hello UDP!".encode(), ('127.0.0.1', 5000))

# Wait for up to 1024 bytes back.
data, _ = client.recvfrom(1024)
print(f"Server said: {data.decode()}")
client.close()
