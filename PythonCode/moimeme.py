print("Do you want to open your game? ")
print("Yes(press '1') and No(press '2') ")
yes=input()
yes=int(yes)
if yes==1:
	print("Input your pass:")
	gmail=input()
	counter=0
	while gmail!="superhung220703":
		if counter>=5:
			print("It's blocked")
			break	
		counter=counter+1
		print("please try again. False "+str(counter)+" time(s)")
		gmail=input()
	if gmail=="superhung220703":
                print("Please waiting")
                print("...")
                print("...")
                print("...")
                print(" ")    

elif yes==2:
	print("See you later")
else:
	print("Error")	
