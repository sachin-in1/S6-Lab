import sys, time
from socket import *
serverHost = "localhost"
serverPort = 5000
s=socket(AF_INET, SOCK_DGRAM)
s.connect((serverHost, serverPort))
s.send("Hello world")
data = s.recv(1024)
print data

