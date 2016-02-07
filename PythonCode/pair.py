import random
a=random.randint(1,2)
if a==1:
	aa=random.randint(1,2)
	if aa==1:
		aa='A'
	
	else:
		aa='C'
	b=random.randint(1,2)
	if b==1:
		b='B'
	else:
		b='D'
elif a==2:
	aa=random.randint(1,2)
	if aa==1:
		aa='B'
	else:
		aa='D'
	b=random.randint(1,2)
	if b==1:
		b='A'
	else:
		b='C'

def game():
	print("A.\tB.\nC.\tD.")
	choose=input()
	
	if choose=='A':
		print("")
		print("B.\nC.\tD.")
		choice=input()
	elif choose=='B':
		print("")
		print("A.\nC.\tD.")
		choice=input()
	elif choose=='C':
		print("")
		print("A.\tB.\nD.")
		choice=input()
	else:
		print("")
		print("A.\tB.\nC.")
		choice=input()
	if str(str(choose))==str(str(choice)):
		print("Congratulation!")
	else:
		print("It's not a pair. Please try again")
game()
