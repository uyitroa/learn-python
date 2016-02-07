# Guess a word
# Import library
import random
# Make list of word
Word=['taire','con','machine','portable','coeur','hunter','table','cle','eau','feu','orange','maison','cheval']
choose=random.choice(Word)
# The length of the secret word
blanks='_ '*len(choose)
print("Mot secret: "+str(blanks))
#Guess the letter
guess=input("Devinez un lettre du mot secret: ")
# Make a loop infinity
x=100000000000000000000
# Make the time for count
counter=0
def whi(guess):	
	while len(guess)>1 or guess not in 'qwertyuiopasdfghjklzxcvbnm':
		if len(guess)>1:
			print("Devinez seulement un lettre chaque fois.")
		if guess not in 'qwertyuiopasdfghjklzxcvbnm':
			print("Devinez seulement le lettre.")
		guess=input("Devinez un lettre du mot secret: ")
	return guess
for letter in range(x):
	whi(guess)
	if guess in choose:
		if counter==len(choose)-1:
			print("Bravo! T'as gagne")
			break
		counter+=1
		letterIndex=choose.index(guess)
		newBlanks=blanks[:letterIndex*2] + guess + blanks[letterIndex*2+1:]	
		newBlanks=blanks
		blanks=blanks[:letterIndex*2] + guess + blanks[letterIndex*2+1:]
		print("Mot secret: "+str(blanks))
	else:
		print("C'est faux!")
	guess=input("Redevinez un lettre du mot secret: ")
