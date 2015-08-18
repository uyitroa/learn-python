def inputnumber():
	print("Enter a number")
	nb = input()
	while not nb.isdigit():
		print(nb + " is not a number. Please enter a number: ")
		nb = input()
	nb = float(nb)
	return nb

def plus(a,b):
	return (a+b)
def minus(a,b):
	return (a-b)
def mul(a,b):
	return (a*b)
def divi(a,b):
	return (a/b)
print("Input value of a: ")
a = inputnumber()

print("Input value of b: ")
b = inputnumber()

print("Enter operator: +, - , * , /")
op = input()
while op !='+' and op != '-' and op !='*' and op !='/':
	print(op + " is not an operator. Enter operator: +, - , * , /")
	op = input()
if op == '+':
	p = plus(a,b)
	print("%f + %f = %f"%(a,b,p))
if op == '-':
	m = minus(a,b)
	print("%f-%f=%f"%(a,b,m))
if op == '*':
	u = mul(a,b)
	print("%f * %f = %f"%(a,b,u))
if op == '/':
	d = divi(a,b)
	print("%f / %f = %f"%(a,b,d))
