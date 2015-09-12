import copy

list = open("data.txt","r")
	
lis = list.read()
	
lis = lis.lower()
	
lis = lis.replace("."," ")
	
lis = lis.replace(","," ")
	
lis = lis.replace("\n"," ")

for q in range(10):
	
	q = str(q)

	if lis.find(q) != -1:

		lis = lis.replace(q," ")

print("Read this text and search a secret word:\n"+str(lis))

mylist = lis.split(" ")

dif = copy.copy(mylist)

for a in range(len(mylist)):
	
	for b in range(a):
	
		if mylist[a] == mylist[b]:

			dif.remove(mylist[a])
		
			break

dif.remove(dif[len(dif) - 1])

print(str(dif))

list.close()

