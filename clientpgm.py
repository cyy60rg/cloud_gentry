import socket
import os
import select
import sys


HOST = '127.0.0.1'
PORT = 6060
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
    
    res1 = int(Cadd) % p
    res2 = int(Cmul) % p
    print "Cadd % p : ", res1
    print "Cmul % p : ", res2
    print ""
    if Nos1 % 2 == 0:
        print "even. Noise = ", res1
    else:
        print "odd. Noise = ", res1
  
    if Nos2 % 2 == 0:
        print "even. noise = ", res2
    else:
        print "odd. noise = ", res2

s.close()
