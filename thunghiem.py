# Guess  word
# Import library
import random
import time
# Make a function of time.
def t(s):
	time.sleep(s)
# Make list of word
Word=['buy','dolphin','machine','mouse','heart','lamp','clock','table','key','water','fire','orange','house','horse']
choose=random.choice(Word)
choose='lamp'
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
# Xoay chiếc nón
non=random.randint(1,13)
print("Turning...")
t(2)
if non<=9:
	non*=100
	print("You will maybe have "+str(non)+" points")
elif non==13:
	turn='second'
	print("You was lost your turn.")
elif non==14:
	print("Opps,you have no points.")
else:
	print("Not thing change.")
# The length of the secret word
blanks='_ '*len(choose)
print("Secret word: "+str(blanks))
#Guess the letter
guess=input("Guess the letter of the secret word: ")
# Make a loop infinity
x=10000000000000000000
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
# Do some thing when you are finish to guess the word.		
		if counter==len(choose)-1:
			if turn=='first':
				print("Congratulation! You won! You have total "+str(count1)+" points")
			else:
				print("Congratulation! You won! You have total "+str(count2)+" points")
			break 
		if turn=='first':
			if non<=9:
				count1+=non
			elif non==10:
				count1*=2
			print("You have "+str(count1)+" points")
		else:
			if non<=9:
				count2+=non
			elif non==10:
				count2*=2
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
	non=random.randint(1,13)
	print("Turning...")
	t(2)
	if non<=9:
		non*=100
		print("You will maybe have "+str(non)+" points")
	elif non==13:
		if turn=='first':
			turn=='second'
			print("You was lost your turn.")
		else:
			turn=='first'
			print("You was lost your turn.")
	elif non==10:
		if turn=='first':
			print("You will maybe have "+str(count1)+" points")
		else:
			print("You will maybe have "+str(count2)+" points")
	elif non==11:
		if turn=='first':
			count1/=2
			print("You have "+str(count1)+" points")
		else:
			count2/=2
			print("You have "+str(count2)+" points")
	elif non==12:
		if turn=='first':
			count1=0
			print("Opps, you was lost all your points.")
		else:
			count2=0
			print("Opps, you was lost all your points.")	
	guess=input("Guess again the letter: ")
