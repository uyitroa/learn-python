# Import math library
import math

# Calculate the perimeter of a circle which have given radius input
# perimeter = 2 * pi * r
def cPerimeter(r):
	p = 2 * math.pi *r
	return p

# Calculate the acreage of a circle wiich have given radius input
# acreage = pi * r**2
def cAcreage(r):
	a = math.pi * r**2
	return a

print("Input the radius of circle: ")
ra = float(input())
per = cPerimeter(ra)
acr = cAcreage(ra)

print("Circle info:")
print("Radius = %f"%(ra))
print("Perimeter = %f"%(per))
print("Acreage = %f"%(acr))

