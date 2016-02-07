import os
import time
import random
def typeslow(firstline):
	irstline = firstline
	for x in range(len(firstline)):
		print(irstline[x],end="",flush=True)
		time.sleep(0.1)
		if firstline[x] == ',':
			time.sleep(0.5)
def music(mu):
	os.system("afplay "+mu)
def digitin(string):
	has = -1
	for x in range(len(string)):
		if isdigit(string[x]):
			has = x
			break
		else:
			has = -1
	return has
def rm(string,ch):
	string = string.replace(ch," ")
	string = string.split(" ")
	for x in range(len(string)):
		if x != 0:
			sting = sting + string[x]
		else:
			sting = string[x]
	return sting
def randomnumber(cent,a,b,c):
	if len(str(cent)) != 1 and cent <= 5 and cent == 100 and cent == 0:
		cent = cent/10
		print("Cent: ",cent)
		cent = int(cent)
		print("After: ",cent)
		for x in range(cent):
			q = random.randint(a,b)
			if q == c:
				break
	elif cent == 0:
		q = "None"
	elif len(str(cent)) == 1:
		q = random.randint(a,b)
	elif cent == 100:
		q = c
	return q
print(randomnumber(4,10,20,15))
print(randomnumber(44,10,20,15))
print(randomnumber(87,10,20,15))
print(randomnumber(99,10,20,15))
print(randomnumber(100,10,20,15))
