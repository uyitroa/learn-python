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


