#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 23346                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
c, addr = s.accept()     # Establish connection with client.
s.listen(4)
c2, addr2 = s.accept()
print 'Got connection from', addr
print 'Got second connection from ',addr2
c.send('Thank you for connecting')
c2.send('Thank you for connecting')
while True:
	msg=c.recv(1024)
	if len(msg)>0:
		c2.send('\n')
		c2.send(msg)
#	msg2 = c2.recv(1024)
#	if len(msg2) > 0:
#		c.send('\n')
#		c.send(msg2)
