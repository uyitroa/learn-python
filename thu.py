string=input("Enter a string: ")
c=0
a=0
v=1
maxindex=-1
for a in range(len(string)):
	my_o=string.index('o',a,len(string))	
	if my_o>maxindex:
		c+=1
		maxindex=my_o
		print(str(my_o))
print("The string has "+str(c)+" o")

