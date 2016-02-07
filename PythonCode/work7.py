print("Enter a string: ")
asd=input()
print("Enter a word: ")
sdf=input()
list2=asd.replace("."," ").replace("?"," ").replace(","," ").replace("!"," ").replace(";"," ").replace(":"," ")
list=list2.split(" ")
counter=0
for x in list:
	if x==sdf:
		counter=counter+1
print("The number of this word is: "+str(counter))
