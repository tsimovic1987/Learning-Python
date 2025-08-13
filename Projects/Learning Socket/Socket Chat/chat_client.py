import socket

CLIENT_IP: str = socket.gethostbyname(socket.gethostname())
CLIENT_PORT: int = 12345
ENCODE_UTF8: str = "utf-8"
ENCODE_ASCII: str = "ascii"#
BYTESIZE: int = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((CLIENT_IP, CLIENT_PORT))

# send & receive messages loop:
while True:
    pass