
# Import library.
import math
import time
def t():
	time.sleep(1)
print("Ex 1:")
num=int(input("Enter a number: "))
# Check the nubmer is or isn't a prime number.
def isprime(nb):
	i = True
	for x in range(2,int(math.sqrt(nb)+1)):
		i=True
		if nb%x==0:
			i=False
			break
	return i
counter=0
for a in range(1,num-1): # Search a prime number.
	i=isprime(a) # Use function to check prime nubmer.
	if i==True:
		counter+=1
		print(str(a)+". The time: "+str(counter))
t()
print("Ex 2:")
b=1
nu=int(input("Enter a number: "))
while counter<nu:
	i=isprime(b)
	if i:
		counter+=1
		print(str(b)+". Time: "+str(counter))
	b+=1
