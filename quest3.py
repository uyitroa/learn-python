a = int(input('NUmber: '))
dict = {}
x = 1
while x <= a:
	dict2 = {x : x ** 2}
	dict.update(dict2)
	x += 1
print(dict)
