import random
print("What's your name?")
name=input()
print("So, you are "+str(name))
print("You want the Mac guess(1) or you guess(2)?")
anwser=input()
anwser=int(anwser)
if anwser==1:
	print("Input the time(s)for guess")
	a=input()
	a=int(a)
	print("The minium  number:")
	min=input()
	min=int(min)
	print("The maxium number:")
	max=input()
	max=int(max)
	userchoice=2
	counter=0
	while userchoice!=1:
	        if counter>=a:
	                print("GAME OVER.")
	                break
	        counter=counter+1
	        x=random.randint(min,max)
	        print("Is "+str(x)+ " the secret number? It,s true(1) or false(2)")
	        userchoice=input()
	        userchoice=int(userchoice)
	        if userchoice==1:
	                print("I won. I have your number after guessing "+str(counter)+" time(s)")
	        else:
	                print("The secret number is bigger(1) or smaller(2) than "+str(x))
	                qwerty=input()
	                qwerty=int(qwerty)
	                if qwerty==1:
	                        min=x+1
	                else:
	                        max=x-1
else:
	x=random.randint(0,1000)
	print("So you are "+str(name)+". You are playing the guessing number game.")
	print("The secret number is between 0 and 1000.")
	print("Input the max times for guess")
	b=input()
	b=int(b)
	print("Guess the secret number.")
	a=input()
	a=int(a)
	counter=1
	while a!=x:
	        if counter>=b:
	                break
	        counter=counter+1
	        if a>x:
	                print("The secret number is smaller than "+str(a))
	        else:
	                print("The secret number is bigger than "+str(a))
	        a=input()
	        a=int(a)
	if a!=x:
	        print("It's false.And it's more than "+str(b)+" time(s). GAME OVER. You lose. The secret number is "+str(x))
	else:
	        print("CONGRASTULATION. The secret number is "+str(x)+" You have my number after guessing "+str(counter)+" times")
