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
    chat_message = client_socket.recv(BYTESIZE).decode(ENCODE_UTF8)
    if chat_message == "/logout":
        client_socket.send("/logout".encode(ENCODE_UTF8))
        print("\nLogged out..")
        break
    else:
        print(f"\n{chat_message}")
        chat_message = input("Chat: ")
        client_socket.send(chat_message.encode(ENCODE_UTF8))

client_socket.close()