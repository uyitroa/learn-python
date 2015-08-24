import time
from threading import Thread
answer = None
def t():
	car=['''
	     ______
	 ___/      \___ 
	|______________|
	 o            o
	''']
	space=' ' * 15
	enemy=car[0]
	def gun():
		print("\t\t __")
		print("\t\t|  |\ ")
		print("\t\t|  ||")
		print("\t\t|  ||")
		print("\t\t|  ||")
		print("\t\t|  | \ ")
		print("\t\t––––\ \ ")
		print("\t\t \   \ |")
		print("\t\t  \   \|")
		print("\t\t   ––––")
	newBlanks = space + enemy
	for x in range(1000000000000000):
		print(str(newBlanks))
		gun()
		anwser = input()
		if answer == None:
			newBlanks = space + "\b\b" + enemy
		else:
			break
def check():
	anwser = input("Enter for shoot: ")
	Thread(target = time.sleep(1)).start()
	t()
check()
