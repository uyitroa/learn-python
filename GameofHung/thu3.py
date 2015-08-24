import time
from threading import Thread

answer = None
car = ["""
     ______
 ___/      \__
|_____________|
 o          o
"""]
enemy = car[0]
space = " " * 80
ospace = " " * 40
newspace = space + enemy
GPS = ["/      \"]
gia
gun = ["""
 __
|  |\
|  ||
|  ||
|  ||
|  ||
|  ||
|  ||
|  | \
–––-\ \
\    \ |
 \    \|
  -----
"""]
hawk = gun[0]
place = ospace + hawk
b = 1

def check():
	time.sleep(2)
	if answer != None:
 		return
	for x in range(100):
		print(str(newspace))
		for a in range(3):
			print()
		print(str(place))
		if anwser == None:
			newspace = space + "\b" * b + enemy
		elif anwser != None:
			break
		b += 8
check()
Thread(target = check).start()
answer = input("Enter for shoot: ")
