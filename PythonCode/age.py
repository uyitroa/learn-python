# If the person is 15 years old or more, he can play game.

# Import library
import random
import time

def t(s): # Make a function (Time).
	for x in range(s):
		time.sleep(1)
		print(".",end="",flush=True)

age=int(input("How old are you?") # Ask the age of the player.)
#+15 years old can play game
if age>=15 :
	#Start game
	#Loading the game
	print("\nLoading game")
	t(3) # The time for wait.
	x=random.randint(0,100) # Random a number.
	a=int(input("Enter a number."))
	counter=1 # Count the time
	while a!=x: # The number is incorrect.
		counter=counter+1 # Each time the player guess.
		#Input again the secret number.
		print("Please try again") # While the number is incorrect.
		if a>x:
			print("The secret number is smaller than "+ str(a)) # The secret number is smaller.
		else:
			print("The secret number is bigger than "+ str(a)) # The secret number is bigger.
		a=int(input("Input a number")) # Input again the secret number
		# If the player win
		print("Congrastulation. You have my number after guessing "+str(counter)+ " times")
		
else: # If the player is less thn 15 years old.
	print("You can't play this game. I'm so sorry.") #If the player is -15 years old, he can't play this game.

