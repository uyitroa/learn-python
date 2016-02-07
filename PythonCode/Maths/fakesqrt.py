# Define a function to find sqrt of a number
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
	# Enter a number
	print("Enter a number: ",end="",flush=True)
	nb = input()
	while not nb.isdigit():
		print(nb+ " is not a number. Please input a number: ")
		nb = input()
	nb = int(nb)

	# Find the sqrt(n)
	fakeSqrt = mySqrt(nb)
	if fakeSqrt != -1:
		print("sqrt(%d)=%d"%(nb,fakeSqrt))
	
	# Ask for play again
	print("Would you like to check more number (yes): ",end="",flush=True)
	playAgain=input()
