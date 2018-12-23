import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '0.0.0.0'
port = 8000

s.bind((host, port))

s.listen(5)

