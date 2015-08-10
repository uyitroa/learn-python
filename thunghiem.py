import math
import random
print("Enter the electricity of the first family:")
family=float(input())
def m(a):
	return a
print("Enter the electricity of the second family:")
family2=float(input())

def money(fa):
	if fa<=50:
		c=fa*4
	elif 50<fa<=100:
		c=200+(fa-50)*3
	else:
		c=350+(fa-100)*2
	return c

c=money(family)
print("The money for pay of family 1 is: "+str(c))

c1=money(family2)
print("The money for pay of family 2 is: "+str(c1))

if family!=family2:
	print(str(min(c,c1))+"<"+str(max(c1,c)))
else:
	print("The money for pay of two family is equal.")
