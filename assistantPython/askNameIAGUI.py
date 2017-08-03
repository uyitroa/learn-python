import random

class whatsYourName():

	def __init__(self):
		self.openFile()
		limitRange = len(self.listWayAskName) - 1
		choiceOfWay = random.randint(0,limitRange)
		ask = raw_input(self.listWayAskName[choiceOfWay])
		sentenceWithName = ask.split(' ')
		usersName = self.findName(sentenceWithName)
		if usersName in self.listUsersKnown:
			print "Welcome come back " + usersName + " ! "
		else:
			print "Nice to meet you " + usersName + " ! "
			askFileOpen = open("usersMemory.txt", "wb")
			newUsersKnown = self.forChange + usersName + ","
			askFileOpen.write(newUsersKnown)

	def openFile(self):
		askFileOpen = open("wayToAskName.txt","r+")
		fileOpenReader = askFileOpen.read().splitlines()
		fileOpenReader = fileOpenReader[0]
		self.listWayAskName = fileOpenReader.split(',')
		self.listWayAskName.remove(self.listWayAskName[len(self.listWayAskName) - 1])
		askFileOpen.close()

		knownUsers = open("usersMemory.txt","r+")
		readUser = knownUsers.read().splitlines()
		readUser = readUser[0]
		self.forChange = readUser
		self.listUsersKnown = readUser.split(',')
		self.listUsersKnown.remove(self.listUsersKnown[len(self.listUsersKnown) - 1])

	def findName(self,list):
		alpha = 'QWERTYUIOPASDFGHJKLZXCVBNM'
		for letter in alpha:
			for i in range(len(list)):
				if letter in list[i]:
					if i != 0 or len(list) == 1:
						usersName = list[i]
						break
		return usersName

if __name__ == '__main__':
	ask = whatsYourName()