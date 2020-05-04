from socket import *
from os import fork
import sys
import datetime
myHost = ""
myPort = 5000
s=socket(AF_INET, SOCK_DGRAM)
s.bind((myHost, myPort))
while True:
 data, address = s.recvfrom(1024)
 print "UDP server:", data, "from", address
 if data:
  print "Request received"
  print "Processing is done "
  s.sendto("message is " + data + "\n Time recieved from server is:" + str(datetime.datetime.now()), address)
 else:
  break
