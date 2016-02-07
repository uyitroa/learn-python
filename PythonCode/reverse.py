# import library
# import binary to ascii
import os
import convert
#open file, this file contain the table of the code
table = open("code.txt","r")
#read  file
table = table.read()
again = 'yes'
def binary_get(bit):
	for x in range(len(bit)):
		if x == 0:
			code = str(ord(bit[x]))
		else:	
			code = code + " " + str(ord(bit[x]))
	bit = code
	bit = bit.split(" ")
	for x in range(len(bit)):
		bite = convert.dtob(bit[x])
		if x == 0:
			bi = str(bite)
		else:
			bi = bi + " " + str(bite)
	bit = bi
	return bit
def decimal_get(bit):
	for x in range(len(bit)):
		if x == 0:
			code = str(ord(bit[x]))
		else:
			code = code + " " + str(ord(bit[x]))
	bit = code
	return bit
def hexa_get(bit):
	for x in range(len(bit)):
		if x == 0:
			code = str(ord(bit[x]))
		else:	
			code = code + " " + str(ord(bit[x]))
	bit = code
	bit = bit.split(" ")
	for x in range(len(bit)):
		bite = convert.dtoh(bit[x])
		if x == 0:
			bi = str(bite)
		else:
			bi = bi + " " + str(bite)
		bit = bi
		return bit
def play():
	bit = input("Code: ")
	print("Binary:\n",binary_get(bit))
	print("Decimal:\n",decimal_get(bit))
	print("Hexa:\n",hexa_get(bit))
if __name__ == "__main__":
		play()
