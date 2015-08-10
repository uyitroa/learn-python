def mySqrt(n):
	if n <0:
		print(str(n)+ " < 0")
		return -1
	else:
		ret = 0
		while ret*2 <=n+1:
			if (ret*ret) == n:
				return ret
			ret += 1
		print(str(n)+" doesn't have sqrt() is a integer number")
		return -1
playAgain = "yes"
while playAgain=="yes":
	print("Enter a number: ",end="",flush=True)
	nb = input()
	while not nb.isdigit():
		print(nb+ " is not a number. Please input a number: ")
		nb = input()
	nb = int(nb)

	fakeSqrt = mySqrt(nb)
	if fakeSqrt != -1:
		print("sqrt(%d)=%d"%(nb,fakeSqrt))
	
	print("Would you like to check more number (yes): ",end="",flush=True)
	playAgain=input()
