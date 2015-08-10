import random
import time
def t(s):
        for x in range(s):
                time.sleep(1)
                print(".",end="",flush=True)
		
		
print("Do you want to open your game?")
print(" ")
print("1.Yes     2.No")
q=input()
q=int(q)
if q==1:
	print("Please input your pass to open")
	passe=input()
	
	while passe!="hung221407":
		print("Please try again:")
		passe=input()
	if passe=="hung221407":
		print("The game is opening")
		t(3)
		
		print("What's your name?")
		name=input()
		print("So, you are "+str(name))
		print("Do you want to you guess(1) or Mac guess(2)?")
		anwser=input()
		anwser=int(anwser)
		if anwser==1:
			print("Input the max times for guess")
			b=input()
			b=int(b)
			print("Input the minium number:")
			min=input()
			min=int(min)
			print("Input the maxium number")
			max=input()
			max=int(max)
			print("So,the secret number is between " +str(min)+" and "+ str(max))
			x=random.randint(min,max)
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
			        print("It's false. And it's more than "+str(b)+" time(s). GAME OVER. You lost. The secret number is "+str(x))
			else:
			        print("CONGRASTULATION. The secret number is "+str(x)+". You have my number after guessing "+str(counter)+" times")
		else:	
			print("Input the minium  number:")
			min=input()
			min=int(min)
			print("Input the maxium number:")
			max=input()
			max=int(max)
			print("Input the time(s)for guess")
			c=input()
			c=int(c)
			userchoice=2
			counter=0
			while userchoice!=1:
			        if counter>=c:
			                print("OOPS!!! I lost. You are not bad.")
			                break
			        counter=counter+1
			        x=random.randint(min,max)
			        print("Is "+str(x)+ " the secret number? It,s true(1) or false(2)")
			        userchoice=input()
			        userchoice=int(userchoice)
			        if userchoice==1:
			                print("Yes! I won.HA HA HA... I have your number after guessing "+str(counter)+" time(s)")
			        else:
			                print("The secret number is bigger(1) or smaller(2) than "+str(x))
			                qwerty=input()
			                qwerty=int(qwerty)
			                if qwerty==1:
		        	                min=x+1
		                	else:
		                        	max=x-1
elif q==2:
	print("See you later")
else:
	print("ERROR")		



