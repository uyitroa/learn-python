import math
def pi(a,x):
	return math.pi*x*a
print("Enter a number for calcul:")
nb=float(input())
print("Perimeter:")
print(pi(2,nb))
print("Acreage:")
print(pi(nb,nb))
