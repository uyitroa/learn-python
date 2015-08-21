import random
import time

def t(s):
	for x in range(s):
		time.sleep(1)
		print(".",end="",flush=True)#. wait . wait . wait
                

def instro():

	print("Welcome to the dragon world.")
	
	print("It has the good dragon and the bad dragon.\n And it has 2 cave. One for the good dragon. And other is bad dragon...")
	t(2)
	print("")
	
	print("You are stand in front of 2 cave")
	t(3)
	print("")
	
	print("You must go into  one of the 2 cave")
	t(2)
def choice():
	print(" ")
	
	print("A. First cave   B.Second cave")
	t(2)
	print("")

	print("So, choose a cave. You must to be careful...")

	choose=input()
	
	return choose

def check(c):
	
	print("Are you sure to the "+str(c)+" ? So, let's go!")
	t(2)
	
	print("\nA dragon step out with a scary sound and...")
	t(4)
	print("")


	x=random.randint(1,2)
	choose=1
	if c== 'A':
		choose=1
	else:
		choose=2
	print(str(choose))
	if x==choose:
		tru()
	
	else:
		fal()	
def tru():

		print("Lucky.It's the good dragon. You have treasure.Congratulation. See you again.")
def fal():
	
		print("Oh no, it's the bad dragon. The dragon will eat you. See you at the cemetery.") 

#Program
def playgame():
	instro()
	a=choice()
	check(a)
#Start
playgame()

 
print("Do you want to play again? 'yes' or 'no'")
anwser=input()
if anwser=='yes':
	while anwser=='yes':
		playgame()
		print("Do you want to play again? 'yes' or 'no'")
		anwser=input()
		if anwser=='no':
			print("See you later")
else:
	print("See you later")	

