import random
x=random.randint(0,100)
print("x="+ str(x)) 
if x<10:
	print("x+10="+str(x+10))
elif x>10 :
	print("x-10="+str(x-10))
else:
	print("x*10"+str(x*10))
