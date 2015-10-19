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
choose = 'clock'
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
		m = -1
		for fi in range(len(choose)):
			my_guess = choose.find(guess,fi,len(choose))
			if my_guess != -1:
				if my_guess != m:
					m = my_guess
					counter+=1
					blanks=blanks[:m*2] + guess + blanks[m*2+1:]			
					counter+=1
		print("Secret word: "+str(blanks))
		if counter==len(choose):
			print("Congratulation!You won!")
			break

	else:
		print("It's wrong!")
		print(str(hang[a]))
		a+=1
		if a==len(hang):
			print("YOU LOSE.")
			print("The secret word is "+str(choose))
			break
	guess=input("Enter again a letter: ")
