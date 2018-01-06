def turnToNum(alpha,word,maxLen):
	# turnToNum(alphabeticList, word)  turn all to number to simplify task ex: abc = 123
	decoded = ""
	for x in range(len(word)):
		for y in range(len(alpha)):
			if word[x] == alpha[y]:
				decoded += str(int(y) + 1)
	decoded += '0' * (maxLen - len(decoded))
	return int(decoded)


def BubbleSort(lst,listWord):  
	lst = list(lst) #copy collection to list   
	for passesLeft in range(len(lst)-1, 0, -1):  
		for i in range(passesLeft):  
			if lst[i] > lst[i + 1]: 
				print(lst)
				lst[i], lst[i + 1] = lst[i + 1],lst[i]
				listWord[i], listWord[i + 1] = listWord[i + 1], listWord[i]	  
	return listWord  

	
def main():
	list = input("list of word split by , ")
	list = list.split(",")
	
	alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	
	maxLen = len(max(list, key=len))
	decodedList = []
	for x in range(len(list)):
		decodedList.append(turnToNum(alpha,list[x],maxLen))

	lst = BubbleSort(decodedList,list)
	print(lst)

if __name__ == "__main__":
	main()
