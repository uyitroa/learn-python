import random
def play(min,max):
	print("Donc, le numero secret est entre "+str(min)+" et "+str(max))
	print("Entrez le maximum de fois pour deviner")
	a=input()
	a=int(a)
	userchoice=2
	counter=0
	while userchoice!=1:
		if counter>=a:
			print("GAME OVER.")
			break
		counter=counter+1
		x=random.randint(min,max)
		print("Est-ce que "+str(x)+ " est le numero secret? C'est vrai(1) ou faux(2)")
		userchoice=input()
		userchoice=int(userchoice)
		if userchoice==1:
			print("Oui! J'ai gagne. HA HA HA...")
		else:
			print("Le numero secret est grand(1) or petit(2) que "+str(x))	
			qwerty=input()
			qwerty=int(qwerty)	
			if qwerty==1:
				min=x+1
			else:
				max=x-1
print("Choisissez le niveau:")
print("press 1.Debutant(0-100)    2.Semi-pro(0-1000)     3.Pro(0-10000)    4.Autre")
choose=input()
choose=int(choose)
if choose==1:
	play(0,100)
elif choose==2:
	play(0,1000)
elif choose==3:
	play(0,10000)
elif choose==4:
        print("Entrez le minimum numero:")
        min=input()
        min=int(min)
        print("Entrez le maximum numero:")
        max=input()
        max=int(max)

        play(min,max)
else:
	print("ERROR")
