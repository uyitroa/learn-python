print("Input a number from 1 to 3")
a=input()
a=int(a)
def sayhello(x):
	if x==1:
		print("Welcome")
	elif x==2:
		print('Bienvenue')
	elif x==3:
		print('Chao mung')
	else:
		print(str(x)+" it's not a number between 1 and 3. Please try again. ")
sayhello(a)	
sayhello(a-1)
