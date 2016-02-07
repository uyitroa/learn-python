mfile = open("date2.txt","r")
myfile = mfile.read()
worddesc = myfile.split(";")
for a in range(len(worddesc)):
	list = worddesc[a].split(":")
	print("Word: "+str(list[0]))
	print("Description: "+str(list[1]))
