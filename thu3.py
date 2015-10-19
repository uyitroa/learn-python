import time
from threading import Thread
car = ["""
\t\t\t\t\t\t\t\t     ______
\t\t\t\t\t\t\t\t ___/*     \__
\t\t\t\t\t\t\t\t|_____________|
\t\t\t\t\t\t\t\t o          o
"""]
enemy = car[0]
space = " " * 80
ospace = " " * 40
newspace = space + enemy
GPS = ["/*     \ "]
gun = ["""
\t\t __
\t\t|  |\ 
\t\t|  ||
\t\t|  ||
\t\t|  ||
\t\t|  ||
\t\t|  ||
\t\t|  ||
\t\t|  | \ 
\t\t–––-\ \ 
\t\t\    \ |
\t\t \    \|
\t\t  -----
"""]
hawk = gun[0]
place = ospace + hawk
b = 1
def check():
	time.sleep(1)
	if answer != None:
		return
for x in range(100):
	print(str(newspace))
	for a in range(3):
		print()
	print(str(place))
	Thread(target = check).start()
	answe = input("Enter for shoot: ")
	if anwser != None:
		break
	else:	
		newspace = space + "\b" * b + enemy
	b += 8
