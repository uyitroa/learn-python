again = 'yes'
if __name__ == "__main__":
	print("""
* * * * * * * * * * * * * * * * * * *

* W E L C O M E   T O   P Y T H O N *

* * * * * * * * * * * * * * * * * * *
	""")
def dtob(bit):
	cont = 0
	n = 1
	bit = int(bit)
	digit = 0
	while n != 0:
		#print("N: ",n)
		digit = int(digit)
		if cont != 0:
			#print("Digit before: ",digit)
			digit = n % 2
			#print("Digit after: ",digit)
			n = n // 2
			number = str(number)
			digit = str(digit)
			#print("Number before: ",number)
			number = digit + number
			#print("Number after: ",number)
		else:
			n = bit // 2
			number = bit % 2
		cont = cont + 1
	#print("Binary: ",number)
	return number
def get_hexa(number):
	if number == 10:
		number = 'A'
	elif number == 11:
		number = 'B'
	elif number == 12:
		number = 'C'
	elif number == 13:
		number = 'D'
	elif number == 14:
		number = 'E'
	elif number == 15:
		number = 'F'
	return number
def dtoh(bit):
	cont = 0
	n = 1
	bit = int(bit)
	digit = 0
	while n != 0:
		#print("N: ",n)
		digit = int(digit)
		if cont != 0:
			#print("Digit before: ",digit)
			digit = n % 16
			digit = get_hexa(digit)
			#print("Digit after: ",digit)
			n = n // 16
			number = str(number)
			digit = str(digit)
			#print("Number before: ",number)
			number = digit + number
			#print("Number after: ",number)
			digit = 0
		else:
			n = bit // 16
			number = bit % 16
			number = get_hexa(number)
		cont = cont + 1
	#print("Hexa: ",number)
	return number
def nbcount(bit):
	counter = len(bit)
	return counter
def btod(bit):
	number = 0
	n = 0
	count = len(bit) - 1
	counter = nbcount(bit)
	while counter != 0:
		#print(str(bit[n]))
		counter = counter - 1
		number = number + (int(bit[n]) * (pow(2,count)))
		n = n + 1
		count = count - 1
	#print("Decimal: ",number)
	return number
def hexa_get(number):
	number = str(number)
	number = number.replace('A','10')
	number = number.replace('B','11')
	number = number.replace('C','12')
	number = number.replace('D','13')
	number = number.replace('E','14')
	number = number.replace('F','15')
	return number
def htod(bit):
	number = 0
	n = 0
	count = len(bit) - 1
	counter = nbcount(bit)
	#bit = hexa_get(bit)
	#print(bit)
	while counter != 0:
		#print(str(bit[n]))
		counter = counter - 1
		#print("Before: ",number)
		number = number + (int(hexa_get(bit[n])) * (pow(16,count)))
		#print("After",number)
		n = n + 1
		count = count - 1
	#print("Decimal: ",number)
	return number
def binary_get(number):
	if int(number) == 1:
		number = 1
	elif int(number) == 10:
		number = 2
	elif int(number) == 11:
		number = 3
	elif int(number) == 100:
		number = 4
	elif int(number) == 101:
		number = 5
	elif int(number) == 110:
		number = 6
	elif int(number) == 111:
		number = 7
	elif number == '1000':
		number = 8
	elif number == '1001':
		number = 9
	elif number == '1010':
		number = 'A'
	elif number == '1011':
		number = 'B'
	elif number == '1100':
		number = 'C'
	elif number == '1101':
		number = 'D'
	elif number == '1110':
		number = 'E'
	elif number == '1111':
		number = 'F'
	return number
def btoh(bit):
	counter = 0
	q = len(bit) - 1
	min = len(bit)
	for x in range(len(bit) - 1):
		if q -4 < 0:
			if counter != 0:
				digite = digite + str(binary_get(bit[:q+1]))
			else:
				digite = str(binary_get(bit[:q+1]))
			print(digite)
			break
		digit = bit[q-3:q+1]
		#print("Digit: ",digit)
		digit = binary_get(digit)
		#print("Digit: ",digit)
		q = q - 4
		#print("Q: ", q)
		if counter != 0:
			digite = digite + str(digit)
		else:
			digite = str(digit)
		counter = counter + 1
		#print(digite)
		digite = str(digite)
	for x in range(len(digite)):
		if x == 0:
			digiter = str(digite[0])
		else:
			digiter = str(digite[x]) + digiter
	return digiter
def hex_get(number):
	if number == '0':
		number = '0000'
	elif number == '1':
		number = '0001'
	elif number == '2':
		number = '0010'
	elif number == '3':
		number = '0011'
	elif number == '4':
		number = '0100'
	elif number == '5':
		number = '0101'
	elif number == '6':
		number = '0110'
	elif number == '7':
		number = '0111'
	elif number == '8':
		number = 1000
	elif number == '9':
		number = 1001
	elif number == 'A':
		number = 1010
	elif number == 'B':
		number = 1011
	elif number == 'C':
		number = 1100
	elif number == 'D':
		number = 1101
	elif number == 'E':
		number = 1110
	elif number == 'F':
		number = 1111
	return number
def htob(bit):
	for x in range(len(bit)):
		if x == 0:
			digit = bit[0]
			digit = hex_get(digit)
			#print("DIGIT: ",digit)
			digite = str(digit)
			#print(digite)
		else:
			digit = bit[x]
			digit = hex_get(digit)
			#print("DIGIT ",digit)
			digite = digite + str(digit)
	return digite
if  __name__ == "__main__":
	while again == 'yes':
		number = 0
		cont = 0
		bit = input("Number: ")
		system = input("System: ")
		if system == '2':
			if not ('2' in bit):
				if not ('3' in bit):
					if not ('4' in bit):
						if not ('5' in bit):
							if not ('6' in bit):
								if not ('7' in bit):
									if not ('8' in bit):
										if not ('9' in bit):
											number = btod(bit)
											print("To decimal: ",number)
											number = btoh(bit)
											print("To hexa: ",number)
		elif system == '10':
			if bit.isdigit():
				number = dtob(bit)
				print("To binary: ",number)
				number = dtoh(bit)
				print("To hexa: ",number)
		elif system == '16':
			number = htob(bit)
			print("To binary: ",number)
			number = htod(bit)
			print("To decimal: ",number)
		again = input("Do again(yes): ")
