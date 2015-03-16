import socket
import os
import select
import sys


HOST = '127.0.0.1'
PORT = 8081
p = input('p = ')
q1 = input('q1 = ')
r1 = input('r1 = ')
b1 = input('b1 = ')
q2 = input('q2 = ')
r2 = input('r2 = ')
b2 = input('b2 = ')
b = b1^b2
bmul = b1&b2

print "bmul = ", bmul

c1 = (int(p) * int(q1)) + (2 * int (r1)) + int(b1)
print "cipher1 = ", c1

c2 = (int(p) * int(q2)) + (2 * int(r2)) + int(b2)
print "cipher2 =", c2

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

s.connect((HOST, PORT))

s.send(str(c1)+":"+str(c2))

while True:

    mrec = s.recv(4098)
    Cadd=mrec.split(":")[0]
    Cmul=mrec.split(":")[1]
    print " Cadd = ", Cadd
    print " "
    print "Cmul = ", Cmul
    
    Nos1 = int(Cadd) % p
    Nos2 = int(Cmul) % p
    print "Cadd % p : ", Nos1
    print "Cmul % p : ", Nos2
    print ""
    if Nos1 % 2 == 0:
        print "Number is even. Noise = ", Nos1
    else:
        print "Number is odd. Noise = ", Nos1
  
    if Nos2 % 2 == 0:
        print "Number is even. Noise = ", Nos2
    else:
        print "Number is odd. Noise = ", Nos2

s.close()
