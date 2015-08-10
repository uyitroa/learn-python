print("input the first number:")
a=input()
if a.isdigit(): #if a isn't a number, the game end.

	a=int(a)
	print("Input the second number")
	
	b=input()
	if b.isdigit():
		b=int(b)
		print(str(a)+"+"+str(b)+"="+str(a+b))
