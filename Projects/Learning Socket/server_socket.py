# Started to learn the socket modul from python lib
# Source of learning -> url.de
# Read README.md for more information
# I'll just don't copy the code. I'll try do understand it
# I'll highlight important parts of the code that were crucial for me to understand, 
# as well as sections where I added my own features or implemented something myself


import socket

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_server.bind((socket.gethostbyname(socket.gethostname()), 12345))

socket_server.listen()
while True:
    client_socket, client_address = socket_server.accept()
    print(type(client_socket))
    print(client_socket)
    print(type(client_address))
    print(client_address)
    print(f"Connected to {client_address}\n")
    client_socket.send(f"You are connected with {socket.gethostname}".encode("utf-8"))
    socket_server.close()
    break