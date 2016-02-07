# import library
# import binary to ascii
import os
import convert
#open file, this file contain the table of the code
#read  file
again = 'yes'
def newconvert(bit):
	bit = str(bit)
	bit = bit.split(" ")
	for x in range(len(bit)):
		bite = convert.btod(bit[x])
		if x == 0:
			bi = str(bite)
		else:
			bi = bi + " " + str(bite)
	bit = bi
	return bit
def play():
	system = int(input("1.Bina\n2.Decimal\n3.Hexa\nYour choice: "))
	if system == 1:
		bit = input("Code: ")
		bit = newconvert(bit)
	elif system == 2:
		bit = input("Code: ")
	else:
		bit = input("Code: ")
		bit = bit.upper()
		bit = newconvert(bit)
	bit = str(bit)
	bit = bit.split(" ")
	for x in range(len(bit)):
		if x == 0:
			code = str(chr(int(bit[x])))
		else:	
			code = code + str(chr(int(bit[x])))
	print("Translate: ",code)
if __name__ == "__main__":
	play()
	again = input("Again? (yes ): ")
