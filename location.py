import binascii
class encrypting:
    def __init__(self,input):
        self.input = input
        self.lol = "print"
        self.mate = "(list[len(i)])"
        self.string = self.lol + self.mate    
    
    def encrypt(self):
        namesArray = []
        fo = open("decrypt.txt","r")
        of = fo.read()
        list = of.split(";")
        bin = open("bin.txt","r")
        lol = bin.read()
        i = lol.split(";")
        codeOfThnig = ""
        location = ""
        print("\n\nEndroit est:")
        code = binascii.cryptingBin()
        if code in self.input:
           exec(self.string)
        print(codeOfThnig)
        print(location)


inputed = input("Password: ")
a = encrypting(inputed)
a.encrypt()
print("Toshiba USB EXT")
