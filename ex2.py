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
# The first circle
print("Input the radius of circle 1: ")
ra1 = float(input())
per1 = cPerimeter(ra1)
acr1 = cAcreage(ra1)

print("Circle 1 info:")
print("Radius 1 = %f"%(ra1))
print("Perimeter 1 = %f"%(per1))
print("Acreage 1 = %f"%(acr1))

# The second circle
print("Input the radius of circle 2: ")
ra2 = float(input())
per2 = cPerimeter(ra2)
acr2 = cAcreage(ra2)

print("Circle 2 info:")
print("Radius 2 = %f"%(ra2))
print("Perimeter 2 = %f"%(per2))
print("Acreage 2 = %f"%(acr2))

# Compare:
print("Circle 1 \t| Circle 2 \t| Result")
print("r1 = %f \t> r2 = %f \t| %s"%(ra1,ra2,ra1>ra2))
print("p1 = %f \t> p2 = %f \t| %s"%(per1,per2,per1>per2))
print("a1 = %f \t> a2 = %f \t| %s"%(acr1,acr2,acr1>acr2))
