def mini(c,q):
        w=c[0]
        a=1
        while a!=len(c)-1:
                if w>c[a]:
                        w=c[a]
                a=a+1

        print("The minium number of list "+str(q)+" is:"+str(w))
        return w
def maxi(c):
        e=c[0]
        a=1
        while a!=len(c)-1:
                if e<c[a]:
                        e=c[a]
                a=a+1

        print("The maxium number of list is:"+str(e))

        return e

mylist1=[0,234,12,3454,21,1,3,52]
mini(mylist1,1)
maxi(mylist1)

mylist2=[0,45,43,65,2345,12,231,1]
mini(mylist2,2)
maxi(mylist2)
