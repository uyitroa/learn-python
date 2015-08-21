import random
print("Choisissez votre niveau:")
print("1. Debutant    2.Semi-Pro    3.Professionel   ")
choose=input()
choose=int(choose)
def play(min,max):
	x=random.randint(min,max)
	print("Entrez le maximum de fois pour deviner: ")
	time=input()
	time=int(time)
	print("Donc, devinez le numero secret:")
	secret=input()
	secret=int(secret)
	counter=1
	while secret!=x:
		if counter>=time:
			print("Vous avez perdu!")
			break
		counter=counter+1
		if x>=secret:
			print("Le numero secret est plus grand que "+str(secret))
		else:
			print("Le numero secret est plus petit que "+str(secret))
		print("Redevinez le numero secret:")
		secret=input()
		secret=int(secret)
	if secret==x:
		print("Congrulations: Vous avez gagnez apres "+str(counter)+" fois")
if choose==1:
	print("Le numero secret est entre 0 et 100")
	play(0,100)
elif choose==2:
	print("Le numero secret est entre 0 et 1000")
	play(0,1000)
elif choose==3:
	print("Le numero secret est entre 0 et 10000")
	play(0,10000)
else:
	print("ERROR")
