import socket

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_client.connect((socket.gethostbyname(socket.gethostname()), 12345))

message = socket_client.recv(1024)
print(message.decode("utf-8"))
raise