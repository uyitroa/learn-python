import random
x=random.randint(0,1000)
print("The secret number is between 0 and 1000.")
print("Input the secret number.")
a=input()
a=int(a)
counter=1
while a!=x:
	counter=counter+1
	if a>x:
		print("The secret number is smaller than "+str(a))
	else:
		print("The secret number is bigger than "+str(a))
	a=input()
	a=int(a)
print("You have my number after "+str(counter)+" times")
if counter<9:
	print("Ecxellent!")
else:
	print("Nod bad!")
