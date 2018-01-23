#!/usr/bin/env python

import socket
import math

TCP_IP = '127.0.0.1'
TCP_PORT = 5007
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print "received value:", data
    print "factorial is:", math.factorial(int(data))
    
    conn.send(str(math.factorial(int(data))))  # echo
conn.close()
