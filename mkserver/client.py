#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 23346                # Reserve a port for your service.
s.connect((host, port))
print(s.recv(1024))
nb=0
while nb<10:
	nb += 1
	print("Going to send "+str(nb))
#	print(s.recv(1024))
	x=raw_input()
#	print("Hello "+x)
	s.send(x)
	msg = s.recv(1024)
	if len(msg) > 0:
		print('\n')
		print(msg)
