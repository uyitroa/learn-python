import time
list=[1, 23, 4, 5, 6, 7, 868, 8, 9, 456,10]
print("The number of element of the string is: "+str(len(list)))

print("list ["+str(0)+"] is : "+str(list[0]))
a=0
while a!=len(list)-1:
	a=a+1
	time.sleep(1)
	print("list ["+str(a)+"] is : "+str(list[a]))
	

