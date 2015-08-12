import math
def f(n):
	a=range(n)
	for i in range(1,n):
		k=2
		while k< math.sqrt(n):
			k=k+1	
		if i%k==0:
			a.remove(i)
	return a
f(25)
