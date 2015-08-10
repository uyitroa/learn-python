import random
x=random.randint(0,1000)
print("What's your name?")
name=input()
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

