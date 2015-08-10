# n!=n*(n-1)*(n-2)*(n-3)*(n-4)...2*1
print("Input a number")
a=input()
a=int(a)
def giaithua(x):
	ketqua=1
	while x>=1:
		ketqua=ketqua*x
		x=x-1
	return ketqua
c=giaithua(a)
print(str(a)+"!="+str(c))
d=giaithua(a+10)
print(str(d))
def saygoodbye():
	print("Goodbye")
for x in range(0,10):
	saygoodbye()
