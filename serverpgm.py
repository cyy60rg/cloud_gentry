import socket
import os
import select
import sys


try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except:
    print 'Failed to create socket'
    sys.exit()

PORT = 8081
HOST = '127.0.0.1'
RECV_BUFFER = 4098

server_socket.bind((HOST, PORT))
server_socket.listen(10)


while True:
    c, addr = server_socket.accept()

    rec= c.recv(4098)
    c1=rec.split(":")[0]
    c2=rec.split(":")[1]
    print "cipher1= ", c1
    print "cipher2= ", c2
    Cadd = int(c1) + int(c2)
    Cmul = int(c1) * int(c2)
    print "Addition operation Result: ", Cadd
    print "Multiplication operation Result: ", Cmul
    c.send(str(Cadd)+":"+str(Cmul))
    
server_socket.close()


