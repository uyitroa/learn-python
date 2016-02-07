answer = 'yes'
text = open("date2.txt","w")
while answer == 'yes':
	word = input("Word: ")
	desc = input("Description: ")
	text.write(str(word)+":"+str(desc)+";")
	answer = input("More? (yes or no): ")
text.close()
