def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1

alist=[1,4,2,30,21,900,34,27]
print("The list is:"+str(alist))
shortBubbleSort(alist)
print("The minium number is: "+str(alist[0]))
print("The maxium number is:"+str(alist[7]))
