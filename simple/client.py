import socket

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = ("127.0.0.1", 8080)
    client.connect(server_ip)

    message = "Hello, World!"
    client.sendall(message.encode('utf-8'))
            
    response = client.recv(1024)
    print(f"Resposta do servidor: {response.decode('utf-8')}")
        
except ConnectionError:
    print("Não foi possível conectar ao servidor.")
finally:
    client.close()