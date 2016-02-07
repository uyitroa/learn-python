import time
""" Game of goal
Help:
	For shoot, you must enter a long/short string, and not a number, ex: if you enter a long string, you have a strong shoot. And if you have a short string, you will have a weak shoot.
	This is the ball: o
	This is the goalie: ¶
			 	–\++\ 
        This is the goal:      ¶  ||||                                  
				–/++/
	This is fooballer: ƒ
"""
# Import library
import random
far=['  o                                          ','    o                                        ','      o                                       ','      o                                      ','        o                                    ','           o                                 ','             o                               ','                  o                          ']
guess=random.choice(far)
blanks=' '*len(far)
newBlanks=blanks + guess + ' ¶  ||||'
o=guess.index('o')
goals=newBlanks.count(" ",o, len(newBlanks))
goals*=0.75
goals+=1
print(str(goals))
def goal(newBlanks):
	for x in range(5):
		print()
	print("\t\t\t\t\t\t\t–\++\ ")
	print(newBlanks)
	print("\t\t\t\t\t\t\t–/++/")
	for x in range(5):
		print()
goal(newBlanks)
long = 1
foot=input("Each charater is a space of the ball, so enter the legth of the charater for shoot the ball.")
goal(newBlanks)
oldBlanks = blanks + ' ' * len(foot) + guess + '\b' * len(foot) + '¶  ||||'
o = oldBlanks.index('o')
ba = oldBlanks.count(" ",0,o)
print(str(long))
while not long > len(foot):
	ball = newBlanks.count(" ",0,o)
	newBlanks=blanks + ' ' * long + guess + '\b' * long + ' ¶  ||||'
	goal(newBlanks)
	time.sleep(1)
	long+=5
	print(str(long))
	print(str(len(foot)))
	if goals + 3 > ba > goals - 5:
		break
oldBlanks = blanks + '                                             ' + ' ¶  ||||'
goal(oldBlanks)
o=newBlanks.find('o')
ball=newBlanks.count(" ",0,o)
ball*=0.75
print(str(ball))
if (goals - 2 <= ball <= goals + 3):
	print("GOALS! You have a goal from "+str(goals)+" meters")
elif ball < goals - 5:
	print("It's weak, try again with more strong.")
else:
	print("Opps, the goalie was stop the ball flew into the goal.")
