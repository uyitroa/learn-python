# Geuss word

# Import library
import random

# Set
# counter of the correct character of secret word
counter=0
playAgain = 'yes'
blanks = '_ '
secret = 0
# Make a list of letter's alphabet
letter = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
# Make functions

def ChooseLetter():
	chooseLetter = random.choice(letter)
	return chooseLetter
# Remove guessed letters
def rm(chooseLetter):
	letter.remove(chooseLetter)
iden = 'yes'
# If corrected guess
def guessCorrect():
	global blanks,iden,counter
	# counter of the number of repeat character
	counter2 = 0
	a = -1
	m = -1
	inde = input("Enter the position of this letter in the word: ")
	ind = inde.split(";")
	counter += len(ind)
	print(str(ind))
	for nbletter in range(secret):
		if counter2 < len(ind):
			a = a + 1
		else:
			break
		if ind[a] != m:
			m = ind[a]
			counter2+=1
			ind[a] = int(ind[a])
			print(str(ind))
			blanks = blanks[:ind[a] * 2] + chooseLetter + blanks[ind[a] * 2 + 1:]
			print(str(blanks))
	rm(chooseLetter)
	return secret

# Start program
while playAgain == 'yes':
	if playAgain == 'yes':
		letter = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
		secret = int(input("Enter the number of the secret word: "))
		blanks = '_ ' * secret
	while 0 != 1:
		if len(letter) == 0:
			print("YOU CHEAT ME!!!!!!!")
			break
		chooseLetter = ChooseLetter()
		answer = input("Is '"+str(chooseLetter)+"' a letter in the secret word? (y or n) ")
		if answer == 'y':
			secret = guessCorrect()
			if counter == secret:
				print("YES! I won! HAHAHAHAHAHA.....")
				break
		else:
			rm(chooseLetter)
	playAgain = input("Do you want to play again? (yes or no) ")
