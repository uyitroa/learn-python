import random
print("Welcome to the guess game, what's your name?")
name=input()
print("So you are "+str(name))

print(" ")
#For read easier

print("Well, "+str(name)+" do you want to you guess or the computer guess")  
print("If You want guess, press '1'")

print(" ")
#For read easier

print("And else, press '2'")
print(" ")
print("So please enter the number")
choose=input()
choose=int(choose)

if choose==1:
	print("So, you want to guess.")
	print(" ")
	print("Input the minium number:")
	min=input()
	min=int(min)
	print("And input the maxium number:")
	max=input()
	max=int(max)
	x=random.randint(min,max)
	print("So the secret number is between " +str(min)+" and "+str(max))
	print(" ")
	print("Input the max times for guess:")
	time=input()
	time=int(time)
	print("Well, please guess the secret number")
	secret=input()
	secret=int(secret)
	while secret!=x:
			print("OOPS!!! It's not the secret number")
			if secret>=x:
				print("The secret number is bigger than "+str(secret))
			else:
				print("The secret number is smaller than "+str(secret))
	print("Please try angain. Guess the secret number")
print("Congratulation")

elif choose=2:
	print("So you want to create a number for the computer guess.")	
	print(" ")
	print("Input the minium number:")
	min=input()
	min=int(min)
	print(" ")
	print("Input the maxium number:")
	max=input()
	max=int(max)
	x=random.randint(min,max)
	print(" ")
	print("So the secret number is between "+str(min)+" and "+str(max))
	print(" ")
	print("Input the max times for guess:")
