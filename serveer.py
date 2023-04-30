import socket

host = ''
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))

server_socket.listen(5)

print(f"Server je pokrenut i čeka na klijenta na portu {port}...")

client_socket, address = server_socket.accept()
print(f"Nova veza uspostavljena sa {address[0]}:{address[1]}")

while True:
    data = client_socket.recv(1024)
    if not data:
        break
    message = data.decode()
    print(f"Primljena poruka od klijenta: {message}")
    response = f"Primio sam poruku '{message}'"
    client_socket.send(response.encode())

client_socket.close()