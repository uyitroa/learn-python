ligne = int(input("Ligne: "))
output = []
espace = ligne - 1
chapeau = 1

for x in range(ligne):
	my_str = " " * espace + "^" * chapeau
	output.append(my_str)
	
	espace -= 1
	chapeau += 2

for x in range(len(output)):
	print output[x]
