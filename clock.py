import time
def clock(s):
	counter=0
	for x in range(60*s):
		counter+=1
		time.sleep(1)
		print("\aTime:"+str(counter)+"sec.")
print("Enter the time(minute) for count:")
tim=input()
tim=float(tim)
print("Enter to start:")
enter=input()
clock(tim)
print("§End")
