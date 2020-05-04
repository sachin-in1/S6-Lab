

import socket, sys
from struct import *
try:
	if(sys.argv[1]=="tcp"):
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
		except socket.error , msg:
			print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
			sys.exit()
	elif(sys.argv[1]=="udp"):
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
		except socket.error , msg:
			print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
			sys.exit()
except IndexError,msg:
	print "Specify protocol"

# receive a packet
while True:
	packet = s.recvfrom(65565)
	
	packet = packet[0]
	
	ip_header = packet[0:20]
	
	iph = unpack('!BBHHHBBH4s4s' , ip_header)
	
	version_ihl = iph[0]
	ihl = version_ihl & 0xF
	
	iph_length = ihl * 4
	

	s_addr = socket.inet_ntoa(iph[8]);
	d_addr = socket.inet_ntoa(iph[9]);
	
	tcp_header = packet[iph_length:iph_length+20]
	
	tcph = unpack('!HHLLBBHHH' , tcp_header)
	
	source_port = tcph[0]
	dest_port = tcph[1]
	acknowledgement = tcph[3]
	doff_reserved = tcph[4]
	tcph_length = doff_reserved >> 4
	
	print 'Source Address : ' + str(s_addr)+'.'+ str(source_port) + '\nDestination Address : ' + str(d_addr) +'.'+ str(dest_port) 
	
	h_size = iph_length + tcph_length * 4
	data_size = len(packet) - h_size
	print 'Data Size: ' + str(data_size)
	#get data from the packet
	if(sys.argv[1]=='udp'):
		data = packet[h_size:]
		print 'Data : ' + data
	
	print

