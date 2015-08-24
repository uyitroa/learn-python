# Guess  word
# Import library
import random
import time
def t(s):
	time.sleep(s)
# Make list of word
Word=['buy','dolphin','machine','mouse','heart','lamp','clock','table','key','water','fire','orange','house','horse']
choose=random.choice(Word)
choose='lamp'
# Xoay chiếc nón
non=random.randint(1,13)
#  Print the point of the player.
print("Turn of the first player")
print("You are having 0 point")
print("Turning...")
t(2)
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
# Set a infinty loop
x=100000000000000000
if non<=9:
	non*=100
	print("You will maybe have "+str(non)+" points")
elif non==13:
	turn='second'
	print("Opps, you was lost your turn.")
else:
	print("Not thing change.")
# The length of the secret word
blanks='_ '*len(choose)
print("Secret word: "+str(blanks))
#Guess the letter
guess=input("Guess the letter of the secret word: ")
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
		count+=non 
		if turn=='first':
			count1+=count
		else:
			count2+=count
		if turn=='first':
			if non<=9:
				count1+=non
			elif non==10:
				count1*=2
		else:
			if non<=9:
				count2+=non
			elif non==10:
				count2*=2
			print("You have "+str(count2)+" points")
		if counter==len(choose)-1:
			if turn=='first':
				print("Congratulation! You won! You have total "+str(count1)+" points")
			else:
				print("Congratulation! You won! You have total "+str(count2)+" points")
			break
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
	if turn=='first':
		print("You are having "+str(count1)+" points.")
	else:
		print("You are having "+str(count2)+" points.")
	print("Turning...")
	t(2)
	if non<=9:
		non*=100
		print("You will maybe have "+str(non)+" points")
	elif turn=='first':
		if non==10:
			print("You will maybe have double point. You will have maybe "+str(count1*2)+" points.")
		elif non==11:
			count1/=2
			print("You was lost a half of your point. You have now "+str(count1)+" points")
		elif non==12:
			count1=0
			print("Opps, you was lost all your points. You have now 0 point.")
		elif non==13:
			print("You was lost your turn. It's turn of the second player.")
	elif turn=='second':
		if non==10:
			print("You will maybe have double point. You will have maybe "+str(count2*2)+" points.")
		elif non==11:
			count2/=2
			print("You was lost a half of your point. You have now "+str(count2)+" points")
		elif non==12:
			count2=0
			print("Opps, you was lost all your point. You have now 0 point.")
		elif non==13:
			print("Opps, you was lost your turn. It's of the first player.")
	guess=input("Guess again the letter: ")
