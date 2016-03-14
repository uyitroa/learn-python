a = input('Input numbers separe by ";": ')
list = a.split(';')
list2 = []
def giaithua(x):
        ketqua = 1
        while x >= 1:
                ketqua = ketqua * x
                x = x - 1
        return ketqua
for x in range(len(list)):
	list2.append(giaithua(int(list[x])))
for x in range(len(list)):
	print(list2[x],'; ',end = '', flush = True)
print('\n')
