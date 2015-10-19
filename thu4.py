import random
where = random.randint(1,3)
car = ["""
     ______
 ___/*  * *\__
|_____________|
 o          o
"""]
enemy = car[0]
spce = " " * 80
space = (spce + "\n") * 4
ospace = " " * 40
newspace = (space + enemy)
print(str(newspace))
GPS = ["\t\t\t\t\t\t\t\t\t\t ___/*  * *\__"]
counter = 0
GUN = ["\t\t\t\t\t __"]
m = -1
first = 0
second = 0
for x in range(len(GPS)):
	my_o = my_string.find('*',x,len(GPS))
	if my_o != -1:
		if my_o != m:	
			m = my_o
			if second == my_o:
				third = my_o
			elif first == my_o:
				second = my_o
			elif first != my_o:
				first = my_o
			
gun = ["""
 __
|  |\ 
|  ||
|  ||
|  ||
|  ||
|  ||
|  ||)
|  | \ 
–––-\ \ 
\    \ |
 \    \|
  -----
"""]
hawk = gun[0]
place = ospace + hawk
b = 0
fire = no
while fire == no:
	newspace = space + enemy 
	fire = input("Enter for shoot. Else enter 'no': ")
