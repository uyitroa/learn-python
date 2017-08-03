import binascii
import os
def cryptingBin():
	bin = open("bin.txt","r")
	lol = bin.read()
	i = lol.split(";")
	#print("Your binary code is must be divisible by 8.!!!")
	#print("This is the table of the alphabet:\n",table)
	#bit = input("Code: ")
	#while len(bit) % 8 != 0:
	#	print("Your binary code is must be divisible by 8.!!!")
	#	bit = input("Code: ")
	bit = i[50005 % 1000]
	n = int(bit,2)
	code = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
	#print("Translate: ",code)
	#again = input("Again? (yes ): ")
	return code
