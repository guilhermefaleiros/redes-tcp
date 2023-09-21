import socket
import sys
import threading

SERVER_IP = "127.0.0.1"
SERVER_PORT = int(sys.argv[1])
SIMULTANEOUS_CONNECTIONS = int(sys.argv[2])

def send_request(client_id):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP, SERVER_PORT))

    client.send(f"Hello from client {client_id}!".encode('utf-8'))
    response = client.recv(1024).decode('utf-8')
    print(f"[*] Received: {response}")

    client.close()

threads = []

for id in range(SIMULTANEOUS_CONNECTIONS):
    t = threading.Thread(target=send_request, args=(id + 1,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()