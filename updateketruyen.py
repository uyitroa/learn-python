import time
import os
def music():
	os.system("afplay "+"/Users/NguyenVietHung/learn-python/DeathNoteSuiteDeathNote.mp3")
def t():
	time.sleep(2)
def head():
	print("\t\t\b\b-------------------------------|----------|----------------------------")
	print("\t\t\b\b-------------------------------|DEATH NOTE|----------------------------")
	print("\t\t\b\b-------------------------------|----------|----------------------------")
def speak(firstline):
	irstline = firstline
	for x in range(len(firstline)):
		print(irstline[x],end="",flush=True)
		time.sleep(0.1)
		if firstline[x] == ',':
			time.sleep(0.5)
	t()
head()
music()
speak('\n\t\t\b\bThis note can kill a human... ')
speak("\n\t\t\b\bThe human whose name is written in this note will die in 40 seconds...  ")
speak("\n\t\t\b\bThis note will not take effet unleas the writer has person's face in their mind his/her name...  ")
speak("\n\t\t\b\bIf the cause of death is not specified, the person will simply die of a heart attack...  ")
speak("\n\t\t\b\bAfter writting the cause of death, details of the death should be written next 400 seconds...   ")
speak("\n\t\t\b\bThis note shall become the property of the human world ")
speak("once it touches the ground of arrives in the human world... ")
speak("\n\t\t\b\bThe owner of the note recognize the image and voice of its or original owner.(A god of death)... ")
speak("\n\t\t\b\bThe human who uses this note neither go to Heaven or Hell... ")
speak("\n\t\t\b\bThe person in possession of the Death Note is possessed by 2 god of death, its original owner, until they die...")
speak("\n\t\t\b\bIf the owner leaves this note, the memories of the Death Note will disapear... When regaining ownership of the Death Note, the memories associated with the Death Note will also return... ")
speak("\n\t\t\b\bIn cases where you were ivolved with other Death Notes involved will return...")
speak("\n\t\t\b\bEven without obtaining ownership, memories will return just by touching the Death Note...")
speak("\n\t\t\b\bTHE END.")
speak("See you again and thank you for listen.")
print("\n",end="",flush=True)
