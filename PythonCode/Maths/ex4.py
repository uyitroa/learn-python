# Enter a string
print("Enter a string: ",end="",flush=True)
mystring = input()

# Enter a word
print("Enter a word: ",end="",flush=True)
myword = input()

# Print out number of times the word appears in string
print("Number of times the word "+ myword+" appears in string "+mystring+" is: ")

# Using count
print("Using count() function: %d"%(mystring.count(myword)))

# Not using count
counter=0
mynewstring = mystring.replace("."," ").replace(","," ").replace("?"," ").replace("!"," ")
listWord = mynewstring.split(" ")
for x in listWord:
	if x == myword:
		counter += 1
print("Not using count() function: %d"%(counter))

# Replace word
# enter new word
print("Enter new word to replace for: "+myword)
newword = input()

# Replace and save as a new string
newstring = mystring.replace(myword,newword)
print("String after replacing: \n"+newstring)
