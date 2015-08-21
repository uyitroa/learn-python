# Search the prime number.

# Import library.
import math
import time
def t():
	time.sleep(1)
def nus(nom):
	sum=0	
	while nom!=0:
		x=nom%10
		sum+=x
		nom=nom/10
		nom=int(nom)
	return sum

# Check the nubmer is or isn't a prime number.
def isprime(nb):
	i = True
	for x in range(2,int(math.sqrt(nb)+1)):
		i=True
		if nb%x==0:
			i=False
			break
	return i
def start():
	choose=int(input("Enter the number of excercice. \nEx 1. 1   Ex 2. 2   Ex 3. 3   Ex 4. 4   Ex 5. 5\n "))
	counter=0
	if choose==1:
		print("Ex 1:")
		num=int(input("Enter a number: "))
		for a in range(1,num-1): # Search a prime number.
			i=isprime(a) # Use function to check prime nubmer.
			if i==True:
				counter+=1
				print(str(a)+". The time: "+str(counter))
		t()
	elif choose==2:
		print("Ex 2:") # Input a times, and print the prime number a times. 
		b=1
		nu=int(input("Enter a number: "))
		while counter<nu:
			i=isprime(b)
			if i:
				counter+=1
				print(str(b)+". Time: "+str(counter))
			b+=1
		t()
	elif choose==3:
		print("Ex 3: ")
		nub=int(input("Enter a number: "))
		counter=0
		while nub!=0:
			counter+=1
			nub/=10
			nub=int(nub)
		print("The number of digit is: "+str(counter))
		t()
	elif choose==4:
		print("Ex 4: ")
		nom=int(input("Enter a number: "))
		sum=nus(nom)
		print(str(sum))
		t()
	else:
		print("Ex 5: ")
		nume=int(input("Enter a number: "))
		sum=nus(nume)
		d1=sum
		print(str(sum))
		nb2=int(input("Enter a nubmer: "))
		sum=nus(nb2)
		d2=sum
		print(sum)
		if d1==d2:
			print("Sum of digit of 2 number is equal")
		else:
			print(str(max(d1,d2))+">"+str(min(d1,d2)))
start()
choice=input("Do you want to play again(y)?: ")
while choice=='y':
	if choice=='y':
		start()
	choice=input("Do you want to play again(y)?: ")
