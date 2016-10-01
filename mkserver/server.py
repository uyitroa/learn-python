#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 23346                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
c, addr = s.accept()     # Establish connection with client.
print 'Got connection from', addr
c.send('Thank you for connecting')
def Conver(x):
	x = str(x)
	x = x.split('+')
	x[0] = int(x[0])
	x[1] = int(x[1])
	result = x[0] + x[1]
	return result
while True:
   msg=c.recv(1024)
   if len(msg)>0:
      print "\n"
      print msg
      result = Conver(msg)
      result = str(result)
      c.send(result)
   
