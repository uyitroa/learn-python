print("Input a string:")
stri=input()
print("The number of characters: "+str(len(stri)))
print("The number of words: "+str(len(stri.split(" "))))
print("The number of sentences is "+str(len(stri.split(". "))))

