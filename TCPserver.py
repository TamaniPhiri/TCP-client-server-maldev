import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(("127.0.0.1",8080))

s.listen()

conn,addr=s.accept()

print("Connection received from"+addr[0])

while True:
    command=input("CMD> ")
    
    if command=="exit":
        conn.send("exit".encode("UTF-8"))
        conn.close()
        break
    
    conn.send(command.encode("UTF-8"))
    print(conn.recv(4096).decode("UTF-8"))