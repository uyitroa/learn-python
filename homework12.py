import math
import random
print("Ex 1:")
nb=int(input("Enter a number: "))
num=random.randint(0,nb-1)
i=True
def prime(c):
	for x in range(2,int(math.sqrt(c)+1)):
		
		if c%x==0:
			i=False
			break
prime(num)
while i=='False':
	num=random.randint(0,nb-1)
	prime(num)
print(str(num))

	
