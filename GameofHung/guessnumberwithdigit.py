# Game guess number
#import library
import random
# set variables
playAgain = 'yes'
while playAgain == 'yes':
	count = 0
	countposition =  0
	guess = 'sd'
	nosamedigit = 'False'
	print("The secret number has 3 digit")
	while nosamedigit == 'False':
		secretnb = random.randint(100,999)
		secretnb = str(secretnb)
		for x in range(3):
			for i in range(3):
				if i != x:
					if secretnb[x] != secretnb[i]:
						nosamedigit = 'True'
					else:
						nosamedigit = 'False'
						break
			if nosamedigit == 'False':
				break
	while len(guess) != 3:
		guess = int(input("Guess the number: "))
		guess = str(guess)
	while guess != secretnb:
		count = 0
		countposition = 0
		for digitcorrect in range(3):
			for compare in range(3):
				if guess[digitcorrect] == secretnb[compare]:
					count = count + 1
					if digitcorrect == compare:
						countposition = countposition + 1
		print("Number of correct digit: ",count,"\nNumber of correct position: ",countposition)
		guess = int(input("Guess the number: "))
		guess = str(guess)
		while len(guess) != 3:
			guess = int(input("Guess the number has 3 digit: "))
			guess = str(guess)
	print("Congratulation!")
	playAgain = input("Do you want to play again? (yes or no)")
