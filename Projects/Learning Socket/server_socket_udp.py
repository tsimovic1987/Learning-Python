import socket

socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket_server.bind((socket.gethostbyname(socket.gethostname()), 12345))

message, address = socket_server.recvfrom(1024)