# Guess a word and it has hangman
# Import library
import random
# Make list of word
Word=['buy','dolphin','machine','mouse','heart','lamp','clock','table','key','water','fire','orange','house','horse']
# Make a list of hangman
hang=['''
 +---+
 |   |
     |
     |
     |
     |
     |
 =========''','''
 +---+
 |   |
 O   |
     |
     |
     |
     |
 =========''','''
 +---+
 |   |
 O   |
 |   |
     |
     |
     |
 =========''','''
 +---+
 |   |
 O   |
/|   |
     |
     |
     |
==========''','''
 +---+
 |   |
 O   |
/|\  |
     |
     | 
     |
==========''','''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
     |
==========''',''' 
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
     |
==========''']
a=1
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
for x in range(x):
	while len(guess)>1 or guess not in 'qwertyuiopasdfghjklzxcvbnm' or guess == "" or blanks.find(guess) != -1:
		if len(guess)>1:
			print("Guess only a letter in one time.")
		if guess not in 'qwertyuiopasdfghjklzxcvbnm' or guess == "":
			print("Guess only the letter and no other.")
		if blanks.find(guess) != -1:
			print("Guess only the letter hasn't guessed.")
		guess = input("Guess again the letter: ")
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
		print(str(hang[a]))
		a+=1
		if a==len(hang):
			print("YOU LOSE.")
			print("The secret word is "+str(choose))
			break
	guess=input("Enter again a letter: ")
