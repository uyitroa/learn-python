# import library
import random
import time

# Wait in s seconds and print out one . per second
def wait(s):
	for i in range(s):
		time.sleep(1)
		print(".",end="")

# Print out game introduction
def introduction():
	print("\n\n- - - - - - - - - - - - - - - - - - - -")
	print("\n-   Welcome to the world of dragon    -")
	print("\n- - - - - - - - - - - - - - - - - - - -")
	time.sleep(3)
	print("\nThere are friendly dragon who will give you their treasure",end="")
	wait(3)
	print("\nalso bad dragon who will eat you",end="")
	wait(3)

# player choose a cave
def chooseCave():
	print("\nNow you are in front of two caves",end="")
	wait(3)
	print("\nOne cave has a friendly dragon inside who will give you the treasure",end="")
	wait(3)
	print("\nand other has a bad dragon who will eat you immediately",end="")
	wait(3)
	print("\nSo which cave are you going to step inside")
	print("\nChoose a cave: A or B:",end="")
	choose = input()
	while choose!='A' and choose!='B' and choose!='a' and choose!='b':
		wait(3)
		print("\nChoose a cave to step inside: A or B:",end="")
		choose = input()
	return choose

# Check the result of player
def checkCave(c):
	x = random.randint(1,2)
	choose = 1
	if (c == 'A' or c == 'a'):
		choose = 1
	elif (c == 'B' or c == 'b' ):
		choose = 2
	else:
		print("\nCannot check value of cave: " + c)
		return
	print("\nSo you are going to step in the cave: " + c,end="")
	wait(3)
	print("\nThere is a very big, blue and scary dragon stand in front of you",end="")
	wait(3)
	print("\nIt is going to your position with many gruu gruu sounds",end="")
	wait(3)
	print("\nThen it ",end="")
	wait(5)
	if x == choose:
		winGame()
	else:
		loseGame()

# Do something when the player win the game
def winGame():
	print("gives you his treasure ... YOU WON THE TREASURE. CONGRATULATIONS!")

# Do something when the player lose the game
def loseGame():
	print("opens its mouth and swallows you in... YOU LOSED YOUR LIFE. SORRY FOR THAT!")

# End of the game
def goodbye():
	print("\nThank you for playing Dragon game. Hope you have good time!")

# Program
introduction()
c = chooseCave()
checkCave(c)
goodbye()

