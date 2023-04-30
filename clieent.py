import socket


host = 'localhost'
port = 12345


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

message = "Zdravo server!"
client_socket.send(message.encode())

response = client_socket.recv(1024)
print(response.decode())

client_socket.close()