import socket
import sys

def send_file(client_socket, filename):
    try:
        with open(filename, 'rb') as f:
            for data in f:
                client_socket.send(data)
        print(f"[*] File {filename} sent successfully")
    except FileNotFoundError:
        print(f"[*] File {filename} not found")
    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

SERVER_PORT = int(sys.argv[1])
SERVER_HOST = "127.0.0.1"

server_ip = (SERVER_HOST, SERVER_PORT)
server.bind(server_ip)

server.listen()
print(f"[*] Server listening on {SERVER_PORT}")

while True:
    client, address = server.accept()
    print(f"[*] Accepted connection from: {address[0]}:{address[1]}")

    filename = client.recv(1024).decode('utf-8')
    send_file(client, filename)