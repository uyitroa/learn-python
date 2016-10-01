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
def converplus(x):
	x = str(x)
	x = x.split('+')
	x[0] = int(x[0])
	x[1] = int(x[1])
	result = x[0] + x[1]
	return result
def converminus(x):
	x = str(x)
	x = x.split('-')
	x[0] = int(x[0])
	x[1] = int(x[1])
	result = x[0] - x[1]
	return result
def convermul(x):
	x = str(x)
	x = x.split('*')
	x[0] = int(x[0])
	x[1] = int(x[1])
	result = x[0] * x[1]
	return result
def converdiv(x):
	x = str(x)
	x = x.split('/')
	x[0] = float(x[0])
	x[1] = float(x[1])
	result = x[0] / x[1]
	return result
while True:
   msg=c.recv(1024)
   if len(msg)>0:
      print "\n"
      print msg
      if '+' in msg:  
         result = converplus(msg)
         result = str(result)
      elif '-' in msg:
         result = converminus(msg)
         result = str(result)
      elif '*' in msg:
         result = convermul(msg)
         result = str(result)
      elif '/' in msg:
         result = converdiv(msg)
         result = str(result)
      c.send(result)
   
