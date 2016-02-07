import random
import time
choose = 'yes'
while choose == 'yes':
	abs = random.randint(1,20)
	ord = random.randint(1,10)
	a = 1
	coo = '''
	oooooooooooooooooooo'''
	for x in range(10):
		if ord == x:
			coo = '''
  ||||||||||||||||||||
--oooooooooooooooooooo''' + '''
--oooooooooooooooooooo''' * (ord - 2) + '\n' + '--' + 'o' * (abs - 1) + 'ø' + 'o' * (20 - abs) + '''
--oooooooooooooooooooo''' * (10 - ord)
	print("Search the letter 'ø'.")
	print(str(coo))
	answer = int(input("Enter the coordinate of ø\n Abscissa: "))
	answer2 = int(input(" Ordinate: "))
	if answer == abs and answer2 == ord:
		print("Congratulation! ")
	else:
		print("False!")
	choose = input("Do you want play again? (yes)")
