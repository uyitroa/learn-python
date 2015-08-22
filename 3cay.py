# Game of card: three card
# Import library
import random
import time
# Set a turn
turn='first'
# Set card of player
card1=0
card2=0
# Make a function of time
def t():
	time.sleep(2)
for x in range(6):
	card=random.randint(1,9)
	if turn=='first':
		card1+=card
		set=card
		print()
		t()
		print("You have "+str(set))
		turn='second'
		if card1 > 10:
			card1-=10
		t()
		print("Sum of your card: "+str(card1))
	else:
		card2+=card
		set=card
		print()
		t()
		print("The computer have "+str(set))
		if card2 > 10:
			card2-=10
		t()
		print("Sum of computer's card: "+str(card2))
		turn='first'
t()
if card1>card2:
	print("You won.")
elif card1<card2:
	print("The computer won, you lost.")
else:
	print("Equal.")
print("You have "+str(card1)+" ponts. The computer have "+str(card2)+" points.")
