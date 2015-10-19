import random
def cal():
	b=input()
	b=float(b)
	print("")
	print("+.   -.    *.    /.    ^.   √. ")
	choose=input()
	if choose=='√':
		x=random.randint(0,1000)
		while x*x!=b:
                	x=random.randint(0,1000)

		print("√ of "+str(b)+"="+str(x))
		print("+.   -.     *.    /.  ")
		choose=input()
	a=input()
	a=float(a)
	while choose!= '=':
		if choose=='+':
			print(str(b)+"+"+str(a)+"="+str(a+b))
			b=a+b
			
		elif choose=='-':
			print(str(b)+"-"+str(a)+"="+str(b-a))
			b=b-a

		elif choose=='*':
			print(str(b)+"*"+str(a)+"="+str(a*b))
			b=a*b

		elif choose=='/':
			print(str(b)+"/"+str(a)+"="+str(b/a))
			b=b/a
 
		elif choose=='^':
			print(str(b)+"^"+str(a)+"="+str(b**a))
			b=b**a
		print("")
		print("+.   -.     *.    /.    =. end")	
		choose=input()
		if choose=='=':
			break
		a=input()
		a=float(a)	

# start
cal()
