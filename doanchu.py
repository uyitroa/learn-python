# Guess a word
# Import library
import random
# Make list of word
Word=['buy','dolphin','machine','mouse','heart','lamp','clock','table','key','water','fire','orange','house','horse']
choose=random.choice(Word)
# The length of the secret word
blanks='_ '*len(choose)
print("Secret word: "+str(blanks))
#Guess the letter
guess=input("Guess the letter of the secret word: ")
# Make a loop infinity
x=100000000000000000000
# Make the time for count
counter=0
def whi(guess):	
	while len(guess)>1 or guess not in 'qwertyuiopasdfghjklzxcvbnm':
		if len(guess)>1:
			print("Guess only a letter in one time.")
		if guess not in 'qwertyuiopasdfghjklzxcvbnm':
			print("Guess only the letter and no other.")
		guess=input("Guess a letter of the secret word: ")
	return guess
for letter in range(x):
	whi(guess)
	if guess in choose:
		if counter==len(choose)-1:
			print("Congratulation!You won!")
			break
		counter+=1
		letterIndex=choose.index(guess)
		newBlanks=blanks[:letterIndex*2] + guess + blanks[letterIndex*2+1:]	
		newBlanks=blanks
		blanks=blanks[:letterIndex*2] + guess + blanks[letterIndex*2+1:]
		print("Secret word: "+str(blanks))
	else:
		print("It's wrong!")
	guess=input("Guess again the letter: ")
