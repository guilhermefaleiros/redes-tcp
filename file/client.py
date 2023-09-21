import socket
import sys

SERVER_IP = "127.0.0.1"
SERVER_PORT = int(sys.argv[1])
FILENAME = sys.argv[2]

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, SERVER_PORT))
client.send(FILENAME.encode('utf-8'))

with open("new-" + FILENAME, 'wb') as f:
    while True:
        data = client.recv(1024)
        if not data:
            break
        f.write(data)

print(f"[*] File {FILENAME} received successfully")

