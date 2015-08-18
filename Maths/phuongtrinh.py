# Equation

#Import library
import math
tim=int(input("Enter the number a: "))
an=input("Enter the hide number(x): ")
ope=input("+.   -.   *.   /.: ")
nb=int(input("Enter the number b: "))
equal=int(input("Enter the result of equation: "))
if ope=='+':
	print(str(tim)+"*"+str(an)+str(ope)+str(nb)+"="+str(equal))
	print("<=> "+str(tim)+"*"+str(an)+" = "+str(equal)+"-"+str(nb))
	print("<=> "+str(an)+" = "+str(equal-nb)+"/"+str(tim))
	print("<=> "+str(an)+" = "+str((equal-nb)/tim))
elif ope=='-':
	print(str(tim)+"*"+str(an)+str(ope)+str(nb)+"="+str(equal))
	print("<=> "+str(tim)+"*"+str(an)+" = "+str(equal)+"+"+str(nb))
	print("<=> "+str(an)+" = "+str(equal+nb)+"/"+str(tim))
	print("<=> "+str(an)+" = "+str((equal+nb)/tim))
elif ope=='*':
	print(str(tim)+"*"+str(an)+str(ope)+str(nb)+"="+str(equal))
	print("<=> "+str(tim)+"*"+str(an)+" = "+str(equal)+"/"+str(nb))
	print("<=> "+str(an)+" = "+str(equal*nb)+"/"+str(tim))
	print("<=> "+str(an)+" = "+str((equal/nb)/tim))
else:
	print(str(tim)+"*"+str(an)+str(ope)+str(nb)+"="+str(equal))
	print("<=> "+str(tim)+"*"+str(an)+" = "+str(equal)+"*"+str(nb))
	print("<=> "+str(an)+" = "+str(equal/nb)+"/"+str(tim))
	print("<=> "+str(an)+" = "+str((equal*nb)/tim))

