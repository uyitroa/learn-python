# return minium number
def min(a,b):
	if a<b:
		print("The minium number is "+str(a))
		return a
	else:
		print("The minium number is "+str(b))
		return b

# return maxium number
def max(c,d):
	if c<d:
		print("The maxium number is "+str(d))
		return d
	else:
		print("The maxium number is "+str(c))
		return c

print(str(min(6,7)))
print(str(max(6,7)))

# return maxium number
def max2(a,b,c):
	return max(max(a,b),max(b,c))

# return minium number
def min2(a,b,c):
	return min(min(a,b),min(b,c))
print(str(max2(5,6,7)))
print(str(min2(5,6,7)))
