import random

wordlist = ['giraffe','dog','dolphin','rabbit','butterfly',\
        'apple','pineapple','durian','orange','rambutan',\
        'red','blue','yellow','green','purple', \
        'heart','circle','rectangle','square','diamond']

#Obtain random word
randWord = random.choice(wordlist)
print(str(randWord))
#Determine length of random word and display number of blanks
blanks = '_ ' * len(randWord)
print ()
print ("Word: ",blanks)


#Set number of failed attempts
count = 6

#Obtain guess
while True:
    print ()
    guess = input ("Please make a guess: ")   
    if len(guess) != 1:
        print ("Please guess one letter at a time!")
    elif guess not in 'abcdefghijklmnopqrstuvwxyz':
       print ("Please only guess letters!")

#Check if guess is found in random word
    for letters in randWord:
        if guess == letters:
            letterIndex = randWord.index(guess)
            newBlanks = blanks[:letterIndex*2] + guess + blanks[letterIndex*2+1:]
            print ("Guess is correct!")
        else:
            count -=1
            print ("Guess is wrong! ", count, " more failed attempts allowed.")
        guess = input("Please make a guess again: ")
    print() 
    print("Word: ",newBlanks) 
