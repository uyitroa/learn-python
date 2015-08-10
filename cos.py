import math
def cos(x):
	return math.cos(math.radians(x))
print("Enter a number for calcul cos:")
degr=float(input())
print(str(cos(degr)**2))
