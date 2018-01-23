import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 502
MESSAGE = input("value: ")

print "TARGET_IP:", UDP_IP
print "TARGET_port:", UDP_PORT
print "value is:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(str(MESSAGE), (UDP_IP, UDP_PORT))

data, addr = sock.recvfrom(1024)
print 'factorial is: ' + data


