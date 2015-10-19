my_string = input("Enter a string: ")
my_let = input("Enter the charater you want search: ")
counter = 0
m = 0
a = 0
for x in range(len(my_string)):
	my_o = my_string.find(my_let,a,len(my_string))
	if my_o != -1:
		if my_o != m:	
			m = my_o
			counter += 1
			print("Index: "+str(m))
	a += 1
print("The nubmer of "+str(my_let)+" is "+str(counter))
