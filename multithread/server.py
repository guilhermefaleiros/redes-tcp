import socket
import sys
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

SERVER_PORT = int(sys.argv[1])
SERVER_HOST = "127.0.0.1"

server_ip = (SERVER_HOST, SERVER_PORT)
server.bind(server_ip)

server.listen()

def handle_request(client_socket):
    data_as_string = client_socket.recv(1024).decode('utf-8')
    data_as_string = data_as_string.upper() + " by server listening on port " + str(SERVER_PORT)

    client_socket.send(data_as_string.encode('utf-8'))
    client_socket.close()

while True:
    print(f"[*] Server listening on {SERVER_PORT}")
    client, address = server.accept()
    print(f"[*] Accepted connection from: {address[0]}:{address[1]}")

    request_handler = threading.Thread(target=handle_request, args=(client,))
    request_handler.start()