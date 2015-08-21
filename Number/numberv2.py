import random
print("What's your name?")
name=input()
print("So, you are "+str(name)+". Welcome to the guessing game.")
print("Input the minium  number:")
min=input()
min=int(min)
print("Input the maxium number:")
max=input()
max=int(max)
print("So, the secret number is between "+str(min)+" and "+str(max))
print("Input the max time(s)for guess")
a=input()
a=int(a)
userchoice=2
counter=0
while userchoice!=1:
	if counter>=a:
		print("GAME OVER.It's more than "+str(a)+" time(s) . I lose. You are good.")
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
