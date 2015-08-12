import math
print("Enter a number:")
nb=int(input())
for x in range(2,int(math.sqrt(nb)+1)):
	i=True
	if nb%x==0:
		i=False
		break
if i:
	print("The number is a prime number.")
else:		
	print("The number isn't a prime number.")
	
