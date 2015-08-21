# Equation
# Import library
import math
a=int(input("Enter the number a: "))
print(str(a)+"*x**2")
ope=input("+.  -.")
b=int(input("Enter the number b: "))
print(str(a)+"*x**2"+str(ope)+str(b)+"*x")
ope2=input("+.   -. : ")
c=int(input("Enter the number c: "))
print(str(a)+"*x**2"+str(ope)+str(b)+"*x"+str(ope2)+str(c)+"=0")
if ope=='-':
	b=-b
if ope2=='-':
	c=-c
print("a="+str(a))
print("b="+str(b))
print("c="+str(c))
print("∆="+str(b**2)+" - "+str(4*a*c))
print("<=> ∆="+str((b**2)-(4*a*c)))
if (b**2)-(4*a*c)>0:
	print("x1="+str((-b+(math.sqrt((b**2)-(4*a*c))))/(2*a)))
	print("x2="+str((-b-(math.sqrt((b**2)-(4*a*c))))/(2*a)))
elif (b**2)-(4*a*c)==0:
	print("x="+str(-(b/(2*a))))
else:
	print("x don't have any solution.")

