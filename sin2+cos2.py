import math
def sin(x):
	return math.sin(math.radians(x))
print("Enter the number for calcul the sin")
degr=float(input())
print(str(sin(degr)**2))
a=sin(degr)**2
print(str(a))
def cos(x):
	return math.cos(math.radians(x))
b=cos(degr)**2
print("So, sin**2+cos**2="+str(a+b))
