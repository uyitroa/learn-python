import thunghiem
import calculatedate
again = 'yes'
while again == 'yes':
	s = input("a.Input date		b.Automatic take date\n Your choice: ")
	if s == 'a':
		thunghiem.play()
	else:
		calculatedate.play()
	again = input("Again(yes) ?")
