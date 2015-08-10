print("The first number is")
a=input()
a=int(a)
print("The second nnumber is")
b=input()
b=int(b)
print("The third number is")
c=input()
c=int(c)
if a<=b<=c:
	print("The minium number is "+ str(a))
	print("The maxium number is "+str(c))
elif a>=b>=c:
	print("The minium number is "+ str(c))
	print("The maxium number is "+str(a))
elif b<=a<=c:
	print("The minium number is "+str(b))
	print("The maxium number is "+str(c))
elif b<=c<=a:
	print("The minium number is "+str(b))
	print("The maxium number is "+str(a))
elif b>=a>=c:
	print("The minium number is "+str(c))
	print("The maxium number is "+str(b))
else:
	print("The minium number is "+str(a))
	print("The maxium number is "+str(b))
