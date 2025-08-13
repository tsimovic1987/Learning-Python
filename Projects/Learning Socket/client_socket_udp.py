import socket

socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket_client.sendto("Hello from the Server".encode("utf-8")),
(socket.gethostbyname(socket.gethostname))