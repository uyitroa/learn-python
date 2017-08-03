import random

class sayHello():

	def __init__(self,input,input2):

		self.input = input
		self.openFileText()
		maxRange = len(self.listWordtoSayHello) - 1
		self.choiceOfWord = random.randint(0,maxRange)
		print self.listWordtoSayHello[self.choiceOfWord]
		if input.lower() in self.listIfdontUnderstand:
			self.userDoesntUnderstand(input2)

	def openFileText(self):
		fileOpen = open("sentenceToSayHello.txt", "r+")
		strFileOpen = fileOpen.read().splitlines()
		strFileOpen = strFileOpen[0]
		self.listWordtoSayHello = strFileOpen.split(',')
		self.listWordtoSayHello.remove(self.listWordtoSayHello[len(self.listWordtoSayHello) - 1])
		fileOpen.close()

		fileOpen1 = open("donotUnderstand.txt", "r+")
		strFileOpen1 = fileOpen1.read().splitlines()
		strFileOpen1 = strFileOpen1[0]
		self.listIfdontUnderstand = strFileOpen1.split(',')
		self.listIfdontUnderstand.remove(self.listIfdontUnderstand[len(self.listIfdontUnderstand) - 1])

		fileOpen2 = open("isThisWrong.txt","r+")
		strFileOpen2 = fileOpen2.read().splitlines()
		strFileOpen2 = strFileOpen2[0]
		self.listisThisWrong = strFileOpen2.split(',')
		self.listisThisWrong.remove(self.listisThisWrong[len(self.listisThisWrong) - 1])

	def userDoesntUnderstand(self,input2):
		maxLengthOfList = len(self.listisThisWrong) - 1
		chooseSentence = random.randint(0,maxLengthOfList)

		if input2.lower() == 'no':
			print "Okay, thank you to noticed me :)"
			self.listWordtoSayHello.remove(self.listWordtoSayHello[self.choiceOfWord])
			stringToWrite = self.convertListToString(self.listWordtoSayHello)
			fileOpen = open("sentenceToSayHello.txt","wb")
			fileOpen.write(stringToWrite)
			fileOpen.close()

	def convertListToString(self,listtoConvert):
		for x in range(len(listtoConvert)):
			if x == 0:
				stringConverted = listtoConvert[x] + ','
			else:
				stringConverted += listtoConvert[x] + ','
		return stringConverted


if __name__ == '__main__':
		say = sayHello("what?","no")






