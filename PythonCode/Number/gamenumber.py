import random
x=random.randint(0,100)
print("The secret number is between 0 and 100.")
print("Input the secret number.")
a=input()
a=int(a)
counter=1
while a!=x:
	counter=counter+1
	print("It's not my number. Please try again")
	if a>x:
		print("The secret number is smaller than "+ str(a))
	else:
		print("The secret number is bigger than "+ str (a))
	a=input()
	a=int(a)
print("Congrastulation.") 
print("You have my number after "+ str(counter)+" times")

