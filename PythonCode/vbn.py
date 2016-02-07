print("Input the time(s) to do some thing")

def inputNumber():
	a = input()
	a = int(a)
	return a

a = inputNumber()

print("Input a number")
b = inputNumber()

print("Input the step")
c = inputNumber()

# repeat from x to y with step is z
def qwe(x,y,z):
	#print("hola...: "+str(x)+" "+str(y)+" "+str(z))
	for b in range(x,y,z):
		print("Ni Hao "+str(b))

for x in range(a,a+c):
	# print(str(x))
	if x%c==0:
		qwe(x,b,c)
		break
		
