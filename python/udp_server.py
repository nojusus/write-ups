import socket

# SOCK_DGRAM uses UDP.
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Claim port 5000 on this machine. '' means any network interface.
server.bind(('', 5000))
print("UDP server ready...")

while True:
    # recvfrom returns both the data and sender.
    data, client_address = server.recvfrom(1024)
    print(f"Got '{data.decode()}' from {client_address}")

    # Echo it back to the same address.
    server.sendto(data, client_address)
