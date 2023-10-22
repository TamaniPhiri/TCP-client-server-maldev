import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(("192.168.56.1",8080))

s.listen()