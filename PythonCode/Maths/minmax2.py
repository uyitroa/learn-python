import time
list=[23, 4, 5, 6, 7, 868, 8, 9, 456, 10]
min=list[0]
max=list[0]
a=1
while a!=len(list)-1:
	if min>list[a]:
		min=list[a]
	if max<list[a]:
		max=list[a]
	a=a+1
		
print("The minium number of list is:"+str(min)+"\nThe maxium number of list is:"+str(max))
