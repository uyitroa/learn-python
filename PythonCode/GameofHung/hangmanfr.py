# Guess a word and it has hangman
# Import library
import random
# Make list of word
Word=['acheter','dophin','machine','souris','coeur','lampe','horloge','table','cle','eau','feu','orange','maison','cheval']
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
print("Mot secret: "+str(blanks))
#Guess the letter
guess=input("Guess the letter of the secret word: ")
# Make a loop infinity
x=100000000000000000000
# Make the time for count
counter=0
for x in range(x):
	while len(guess)>1 or guess not in 'qwertyuiopasdfghjklzxcvbnm' or guess == "" or blanks.find(guess) != -1:
		if len(guess)>1:
			print("Devinez seulement le lettre, pas mot.")
		if guess not in 'qwertyuiopasdfghjklzxcvbnm' or guess == "":
			print("Devinez seulement le lettre..")
		if blanks.find(guess) != -1:
			print("Devinez seulement les lettres ne sont pas deviné.")
		guess = input("Redevinez: ")
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
		print("Mot secret: "+str(blanks))
		if counter==len(choose):
			print("Bravo! Vous avez gagné.!")
			break

	else:
		print("Faux!")
		print(str(hang[a]))
		a+=1
		if a==len(hang):
			print("Vous avez perdu!.")
			print("Le mot secret est: "+str(choose))
			break
	guess=input("Devinez un lettre: ")
