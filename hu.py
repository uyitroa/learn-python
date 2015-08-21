# Import library
import random
wordlist = ['giraffe','dolphin','pineapple','durian','bliue','piurple','hieart','reictangle']

#Obtain random word
randWord = random.choice(wordlist)

#Determine length of random word and display number of blanks
blanks = '_ ' * len(randWord)
print ()
print ("Word: "+str(blanks))


#Set number of failed attempts
count = 10
x=1000
#Obtain guess
while True:
	print ()
	guess = input ("Please make a guess: ")   
	if len(guess) != 1:
		print ("Please guess one letter at a time!")
	elif guess not in 'abcdefghijklmnopqrstuvwxyz':
		print ("Please only guess letters!")
#Check if guess is found in random word
	for letters in range(x):
		x+=100
		if guess == letters:
			letterIndex = randWord.index(guess)
			newBlanks = blanks[:letterIndex*2] + guess + blanks[letterIndex*2+1:]
			print ("Guess is correct!")
			Blank = newBlanks[:letterIndex*2] + guess + newBlanks[letterIndex*2+1:]
			print("Secret word: "+str(Blank))
		else:
			count -=1
			print ("Guess is wrong! ", count, " more failed attempts allowed.")
		guess = input("Please guess again: ")
	print() 
