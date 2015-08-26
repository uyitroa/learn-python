import random
choice = 'yes'
while choice == 'yes':
	print("""
	\t\t\t\t++––––––––––––––––++
	\t\t\t\t||––––––––––––––––||
	\t\t\t\t||		  ||
	\t\t\t\t||        O	  ||
	\t\t\t\t||       /|\	  ||
	\t\t\t\t||_______/_\______||
		      
	
	
			
			
	
	\t\t\t\t	o
	\t\t\t\t	ª
	\t\t\t\t	      O
	\t\t\t\t	     /|\	
	\t\t\t\t	     / \ 
	""")
	weak = random.randint(6,15)
	good = random.randint(10,20)
	good2 = good
	while (good2 == good or good2 < good + 1): 
		good2 = random.randint(11,21)
	strong = random.randint(17,30)
	Direct = random.randint(1,3)
	print(str(good),str(good2))
	shoot = input("Left.	  	Right. : ")
	level = input("Shoot: ")
	if shoot == 'Left':
		if len(level) <= weak:
			print("""	
				\t\t\t++––––––––––––––––++
				\t\t\t||––––––––––––––––||
				\t\t\t||                ||
				\t\t\t||                ||
				\t\t\t||    -O-         ||
				\t\t\t||___//o\\\________||	
				\t\t	      \	
				\t\t	      \	
				\t\t	      \ O
				\t\t	      \/|\ 
				\t\t	      •/ \ 
				""")
			print("It's not very strong. Try again with more strong.")
		elif good<=len(level)<=good2:
			if Direct == 1:
				print("""
				\t\t\t\t++––––––––––––––––++
				\t\t\t\t||––––––––––––––––||
				\t\t\t\t||  _             ||
				\t\t\t\t||  o\O           ||
				\t\t\t\t||   \–\-         ||
				\t\t\t\t||___\_\ \\________||
				\t\t	     \ 
				\t\t	     \   O
				\t\t	     \  /|\ 
				\t\t          • / \ 
				""")
				print("Oops, the goalie has stopped the ball flew into goal.")
			elif Direct == 2:
				print("""
				\t\t\t\t++––––––––––––––––++
				\t\t\t\t||––––––––––––––––||
				\t\t\t\t||                ||
				\t\t\t\t||   o    O       ||
				\t\t\t\t||    \  \|\      ||
				\t\t\t\t||_____\_/_\______||
				\t\t\t\t	\ 
				\t\t\t\t	\ 
				\t\t\t\t	\ 
				
				
				
				\t\t\t\t        
				\t\t\t\t        
				\t\t\t\t              O
				\t\t\t\t           • /|\ 
				\t\t\t\t             / \ 
				""")
				print("Goals!")
			else:	
				print("""
				\t\t\t\t++––––––––––––––––++
				\t\t\t\t||––––––––––––––––||
				\t\t\t\t||                ||
				\t\t\t\t||   o      O/    ||
				\t\t\t\t||    \   -/      ||
				\t\t\t\t||____\___//______||
				\t\t\t\t       \
				\t\t\t\t       \
				\t\t\t\t	\
	
	
	
				\t\t\t\t        
				\t\t\t\t              O
				\t\t\t\t        •    /|\ 
				\t\t\t\t             / \ 
				""")	
				print("Goals!")
		else:
			print("""
			\t\t\t\t    o
			\t\t\t\t++–––\––––––––––––++
			\t\t\t\t||–––\––––––––––––||
			\t\t\t\t||   \            ||
			\t\t\t\t||   \    O       ||
			\t\t\t\t||       /|\      ||
			\t\t\t\t||_______/_\______||
	
		
		
		
		
	
			\t\t\t\t        
			\t\t\t\t        ª
			\t\t\t\t              O
			\t\t\t\t             /|\ 
			\t\t\t\t             / \ 
			""")
			print("It's vrey strong. Try again with less strong.")
	elif shoot == 'Right':
		
		if good<=len(level)<=good2:
			if Direct == 3:
				print("""
				\t\t\t\t++––––––––––––––––++
				\t\t\t\t||––––––––––––––––||
				\t\t\t\t||            _   ||
				\t\t\t\t||          O/o   ||
				\t\t\t\t||         /-     ||
				\t\t\t\t||_______/_|______||
				\t\t	     	/
				\t\t	       / O
				\t\t	      / /|\ 
				\t\t          • / \ 
				""")
				print("Oops, the goalie has stopped the ball flew into goal.")
			elif Direct == 2:
				print("""
				\t\t\t\t++––––––––––––––––++
				\t\t\t\t||––––––––––––––––||
				\t\t\t\t||                ||
				\t\t\t\t||        O       ||
				\t\t\t\t||       /|\   o  ||
				\t\t\t\t||_______/_\______||
				\t\t\t\t	     /
				\t\t\t\t	    /
				\t\t\t\t	   /		 
				
				
				
				\t\t\t\t        
				\t\t\t\t        
				\t\t\t\t              O
				\t\t\t\t           • /|\ 
				\t\t\t\t             / \ 
				""")
				print("Goals!")
			else:
				print("""
				\t\t\t\t++––––––––––––––––++
				\t\t\t\t||––––––––––––––––||
				\t\t\t\t||                ||
				\t\t\t\t||     \O     o   ||
				\t\t\t\t||       \-  /    ||
				\t\t\t\t||_______\\_/_____||
				\t\t\t\t          /
				\t\t\t\t         /
				\t\t\t\t	/
	
	
	
				\t\t\t\t        
				\t\t\t\t              O
				\t\t\t\t        •    /|\ 
				\t\t\t\t             / \ 
				""")	
				print("Goals!")
		if len(level) <= weak:
			print("""	
			\t\t\t++––––––––––––––––++
			\t\t\t||––––––––––––––––||
			\t\t\t||                ||
			\t\t\t||                ||
			\t\t\t||          -O-   ||
			\t\t\t||_________//o\\\_||	
			\t\t	           \	
			\t\t	           \	
			\t\t	           O
			\t\t	        • /|\ 
			\t\t	          / \ 
			""")
			print("It's not very strong. Try again with more strong.")

		else:
			print("""
			\t\t\t\t               o
			\t\t\t\t++––––––––––––––––++
			\t\t\t\t||–––––––––––––/––||
			\t\t\t\t||           /    ||
			\t\t\t\t||        O /     ||
			\t\t\t\t||       /|\      ||
			\t\t\t\t||_______/_\______||
		
			
			
			
			
		
			\t\t\t\t        
			\t\t\t\t        ª
			\t\t\t\t              O
			\t\t\t\t             /|\ 
			\t\t\t\t             / \ 
			""")
			print("It's very strong.Try again with less strong.")
	choice = input("Do you want to play again? (yes): ")
