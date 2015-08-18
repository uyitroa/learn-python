print("Enter the first edge of triangle:")
ed=float(input())

print("Enter the second edge of triangle:")
edg=float(input())

print("Enter the third edge of triangle:")
edge=float(input())

if (ed+edg<=edge or ed==0 or edg==0 or edge==0 or edg+edge<=ed or ed+edge<=edg):
	print("It's not a triangle")
	
elif (ed==edg and ed!=edge or ed==edge and ed!=edg or edg==edge and edg!=ed):
	print("This triangle is the triangle 'cân'") #I don't know what's 'cân' in english

elif ed==edg==edge:
	print("This triangle is the triangle 'đều'") #'đều' too.

else:
	print("This triangle is a normal triangle")

 
