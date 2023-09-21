import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_ip = ("127.0.0.1", 8080)
server.bind(server_ip)

server.listen()

while True:
    print("Waiting")
    connection, client_address = server.accept()
    print(f"Conexão estabelecida com {client_address}")

    while True:
        data = connection.recv(1024)
        if data:
            data_as_string = data.decode('utf-8')
            data_as_string = data_as_string.upper()
            connection.sendall(data_as_string.encode('utf-8'))
        else:
            break

    connection.close()