# Game of goal
# Import library
import random
far=[' o                                            ','  o                                           ','   o                                          ','    o                                         ','     o                                        ','         o                                    ','          o                                   ','                  o                           ']
guess=random.choice(far)
go = '     |'
blanks=' '*len(far)
newBlanks=blanks + guess + go
def goal():
	print("\t\t\t\t\t\t\t\b\b Goal")
	print("\t\t\t\t\t\t\t|")
	print("\t\t\t\t\t\t\t|")
	print("\t\t\t\t\t\t\t|")
	print("\t\t\t\t\t\t\t\b\  /")
	print("\t\t\t\t\t\t\t\b \/")
	print()
	print("\t\t\t\t\t\t\t---\ ")
	print(str(newBlanks))
	print("\t\t\t\t\t\t\t_ _/")
goal()
foot=input("Each charater is a space of the ball, so enter the legth of the charater for shoot the ball: ")
newBlanks=blanks + ' '*len(foot) + guess + '\b' * len(foot) + go
ball=newBlanks.index('o')
goals=newBlanks.index('|')
goal()
if ball==goals or ball==goals-1 or ball==goals-2 or ball==goals-3:
	print("GOAL! You have a goal from "+str(ball)+" meters")
