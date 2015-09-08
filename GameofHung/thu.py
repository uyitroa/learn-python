list = open("data.txt","r")
lis = list.read()
lis = lis.lower()
print(str(lis))
mylist = lis.split(" ")
dif = [mylist[0]]
diffe = 'True'
for a in range(len(mylist)):
	for b in range(len(mylist)):
		if b != a:
			if mylist[a] != mylist[b]:
				diffe = 'True'
			if mylist[a] == mylist[b]:
				diffe = 'False'
				break
	if diffe == 'True':
		dif.append(mylist[a])
print(str(dif))
list.close()
