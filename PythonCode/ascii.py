import os
import reverse
import newtranslatecode
table = open("code.txt","r")
table = table.read()
again = 'yes'
while again == 'yes':
	print(table)
	system = input("A.Ascii to number	B.Number to ascii\nYour choice: ")
	system = system.upper()
	if system == 'A':
		reverse.play()
	else:
		newtranslatecode.play()
	again = input("Again(yes)")
