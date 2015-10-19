# Game guess number
#import library
import random
# set variables
playAgain = 'yes'
count = 0	
countposition = 0
guess = 0
#function random number
def randnb():
	global secretnb
	#random number
	secretnb = random.randint(100,999)
	#return
	return secretnb
#function guess nubmer
def guessNumber():
	print("The secret number has 3 digit.")
	guess = input("Guess a number: ")
	#if the number is not a number
	while not guess.isdigit():
		guess = input("Guess a number: ")
	while len(guess) != 3:
		guess = input("Guess a number has 3 digit: ")
	#return
	return guess
def guessAgain():
	global guess,secretnb
	count = 0
	countposition = 0
	#print("Secret: ",secretnb)
	#print("Guess: ",guess)
	guess = str(guess)
	for digitcorrect in range(3):
		for compare in range(3):
			if guess[digitcorrect] == str(secretnb)[compare]:
				count = count + 1
				if digitcorrect == compare:
					countposition += 1
	print("Number of correct digit: ",count,"\nNumber of digit has right position: ",countposition)
#function play game
def playGame():
	global guess,secretnb
	secretnb = randnb()
	secretnb = 303
	guess = guessNumber()
	secretnb  = str(secretnb)
	guess = str(guess)
	while guess != secretnb:
		guessAgain()
		guess = guessNumber()
		guess = str(guess)
		secretnb = str(secretnb)
# start game
while playAgain == 'yes':
	#set variables
	playAgain = 'yes' 
	count = 0       
	countposition = 0
	playGame()
	print("Congratulation!")
	playAgain = input("Do you want to play again? (yes or no): ")
