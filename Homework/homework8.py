again = 'yes'
print("""
* * * * * * * * * * * * * * * * * * *

* W E L C O M E   T O   P Y T H O N *

* * * * * * * * * * * * * * * * * * *
""")
while again == 'yes':
	number = 0
	cont = 0
	print("Which type do you want to change??\n1. From binary to decimal\n2. From decimal to binary")
	type = int(input("Your choice: "))
	bit = input("Enter value of input number: ")
	if type == 1:
		n = 0
		count = len(bit) - 1
		counter = len(bit)
		while counter != 0:
			print(str(bit[n]))
			counter = counter - 1
			number = number + (int(bit[n]) * (pow(2,count)))
			n = n + 1
			count = count - 1
		print("Decimal: ",number)
	elif type == 2:
		n = 1
		bit = int(bit)
		digit = 0
		while n != 0:
			print("N: ",n)
			digit = int(digit)
			if cont != 0:
				print("Digit before: ",digit)
				digit = n % 2
				print("Digit after: ",digit)
				n = n // 2
				number = str(number)
				digit = str(digit)
				print("Number before: ",number)
				number = digit + number
				print("Number after: ",number)
			else:
				n = bit // 2
				number = bit % 2
			cont = cont + 1
		print("Binary: ",number)
	again = input("Do again ? : ")
