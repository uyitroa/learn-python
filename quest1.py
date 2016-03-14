list = []
for x in range(2000,3200):
	if x % 7 == 0:
		if x % 5 != 0:
			list.append(x)
for x in range(len(list)):
	print(list[x],'; ',end="",flush = True)
print('\n')
