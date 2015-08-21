import random
#The program of game
def play(min,max):
	print("So, the secret number is between "+str(min)+" and "+str(max))
	print("Input the max time(s)for guess")
	a=input()
	a=int(a)
	userchoice=2
	counter=0
	while userchoice!=1:
		if counter>=a:
			print("GAME OVER. It's more than "+str(a)+" time(s) . I lose. You are good.")
			break
		counter=counter+1
		x=random.randint(min,max)
		print("Is "+str(x)+ " the secret number? It,s true(1) or false(2)")
		userchoice=input()
		userchoice=int(userchoice)
		if userchoice==1:
			print("Yes! I won. HA HA HA... I have your number after guessing "+str(counter)+" time(s)")
		else:
			print("The secret number is bigger(1) or smaller(2) than "+str(x))	
			qwerty=input()
			qwerty=int(qwerty)	
			if qwerty==1:
				min=x+1
			else:
				max=x-1
#Starting game
print("Choose the level:")
print("press 1.Beginner(0-100)    2.Semi-pro(0-1000)     3.Pro(0-10000)    4.Other")
choose=input()
choose=int(choose)
if choose==1:
	play(0,100)
elif choose==2:
	play(0,1000)
elif choose==3:
	play(0,10000)
elif choose==4:
        print("Input the minium  number:")
        min=input()
        min=int(min)
        print("Input the maxium number:")
        max=input()
        max=int(max)

        play(min,max)
else:
	print("ERROR")
