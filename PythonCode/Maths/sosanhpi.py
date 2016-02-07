import math
def pi(a,x):
	return math.pi*x*a
print("Enter a number for calcul:")
nb=float(input())

print("Perimeter:")
print(pi(2,nb))
s=pi(2,nb)

print("Acreage:")
print(pi(nb,nb))
d=pi(nb,nb)


print("Enter a number for calcul:")
nb2=float(input())

print("Perimeter:")
print(pi(2,nb2))
c=pi(2,nb2)

print("Acreage:")
print(pi(nb2,nb2))
v=pi(nb2,nb2)

if s==c:
	print("The perimeter of two circle is equal.")
else:
	print(str(max(s,c))+">"+str(min(s,c)))
if d==v:
	print("The acreage of two circle is equal.")
else:
	print(str(max(d,v))+">"+str(min(d,v)))

