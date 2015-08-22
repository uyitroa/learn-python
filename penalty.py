# Game of goal
# Import library
import random
far=[' o                                            ','  o                                           ','   o                                          ','    o                                         ','     o                                        ','         o                                    ','          o                                   ','                  o                           ']
guess=random.choice(far)
blanks=' '*len(far)
newBlanks=blanks + guess + ' ¶  ||||'
o=guess.index('o')
goals=newBlanks.count(" ",o, len(newBlanks))
goal=0.75
print(str(goals))
def goal():
	print("\t\t\t\t\t\t\t–\++\ ")
	print(newBlanks)
	print("\t\t\t\t\t\t\t–/++/")
goal()
foot=input("Each charater is a space of the ball, so enter the legth of the charater for shoot the ball.")
newBlanks=blanks + ' '*len(foot) + guess + '\b' * len(foot) + ' ¶  ||||'
goal()
o=newBlanks.index('o')
ball=newBlanks.count(" ",0,o)
ball*=0.75
print(str(ball))
if (goals - 3 <= ball <= goals + 3):
	print("GOALS! You have a goal from "+str(ball)+" meters")
elif ball < goals:
	print("It's very weak, try again with more strong.")
else:
	print("Opps, the goalie was stop the ball flew into the goal.")
