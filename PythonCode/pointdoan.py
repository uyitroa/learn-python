# Guess  word
# Import library
import random
# Make list of word
Word=['buy','dolphin','machine','mouse','heart','lamp','clock','table','key','water','fire','orange','house','horse']
choose=random.choice(Word)
choose='lamp'
# Xoay chiếc nón
non=random.randint(1,9)
non*=100
print("You will maybe have "+str(non)+" points")
# The length of the secret word
blanks='_ '*len(choose)
print("Secret word: "+str(blanks))
#Guess the letter
guess=input("Guess the letter of the secret word: ")
# Make a loop infinity
x=10000000000000000000
# Make the time for count
counter=0
# Set count point
count=0
# First player
count1=0
# Second player
count2=0
# Set a turn
turn='first'
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
			if turn=='first':
				print("Congratulation! You won! You have total "+str(count1)+" points")
			else:
				print("Congratulation! You won! You have total "+str(count2)+" points")
			break
		count+=non 
		if turn=='first':
			count1+=count
		else:
			count2+=count
		if turn=='first':
			print("You have "+str(count1)+" points")
		else:
			print("You have "+str(count2)+" points")
		counter+=1
		letterIndex=choose.index(guess)
		newBlanks=blanks[:letterIndex*2] + guess + blanks[letterIndex*2+1:]	
		newBlanks=blanks
		blanks=blanks[:letterIndex*2] + guess + blanks[letterIndex*2+1:]
		print()
		print("Secret word: "+str(blanks))
	else:
		print("It's wrong!")
		print("You don't have any point.")
		if turn=='first':
			print("It's the turn of the second player.")
			turn='second'
		else:
			print("It's the turn of the first player.")
			turn='first'
	count=0
	non=random.randint(1,9)
	non*=100
	print("You will maybe have "+str(non)+" points")
	guess=input("Guess again the letter: ")
