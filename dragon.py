import random
import time

def t(s):
	for x in range(s):
		time.sleep(1)
		print(".",end="",flush=True)
                

def instro():

	print("\n\t\tWelcome to the dragon world.")
	
	print("\nIt has the good dragon and the bad dragon. And it has 2 cave. One for the good dragon. And other is bad dragon...")
	t(3)
	print("")
	
	print("\nYou are stand in front of 2 cave")
	t(3)
	print("")
	
	print("\nYou must go into  one of the 2 cave")
	t(3)
def choice():
	print(" ")
	
	print("\nA. First cave   B.Second cave")
	t(3)
	print("")

	print("\nSo, choose a cave. You must to be careful...")

	choose=input()
	
	return choose

def check(c):
	
	print("\nAre you sureto the "+str(c)+" ? So, let's go!")
	t(3)
	
	print("\nA dragon step out with a scary sound and...")
	t(1)
	print("\a \a")
	t(1)
	print("\a\a")
	t(1)
	print("\a\a")
	print("")


	x=random.randint(1,2)
	choose=1
	if choose== 'A':
		choose=1
	else:
		choose=2
	if x==choose:
		tru()
	else:
		fal()	
def tru():

		print("\nLucky.It's the good dragon. You have treasure.Congratulation. See you again.")
def fal():
	
		print("\nOh no, it's the bad dragon. The dragon will eat you. See you at the cemetery.") 

#Pr
def playgame():
	instro()
	a=choice()
	check(a)
#Start
playgame()

 

