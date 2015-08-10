import random
import time
def t(s):
	for x in range(s):
		time.sleep(1)
		print(".",end="",flush=True)

print("How old are you?")
age=input()
age=int(age)
#+15 years old can play game
if age>=15:
#Start game
	#Loading the game
	print("\nLoading game")
	t(3)
	x=random.randint(0,100)
	print("\nInput a number")
	a=input()
	a=int(a)
	counter=1
	while a!=x:
		counter=counter+1
		#Input again the secret number.
		print("Please try again")
		if a>x:
			print("The secret number is smaller than "+ str(a))
		else:
			print("The secret number is bigger than "+ str(a))
		print("Input a number")
		a=input()
		a=int(a)
	print("congrastulation. You have my number after guessing "+str(counter)+ " times")
		
else:
	print("You can't play this game. I'm so sorry.") #If the player is -15 years old, he can't play this game.

