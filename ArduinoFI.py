#Brian Eubanks
#
#Arduino Fault Injection Tool

from intelhex import IntelHex
from os import path



#Arduino AVR hex files use intelhex format



# CLASS IHexFile - contains methods to read/write and modify AVR hex files\

# loadFromFile - Loads IntelHex file - sets min and max address
# writeToFile - writes the output Hex file and any modifications made
# createHexDump - view obj-dump of hex file
# faultInject - inject a fault at address.
class IHexFile:

    

    def __init__(self):
        self.ihex = IntelHex()
        self.fileName = "None Loaded"
        self.fileLoaded = False
        self.faultList = {}
        
    def loadFromFile(self, infilename):
        self.ihex.fromfile(infilename,format='hex')
        self.fileName = infilename
        self.fileLoaded = True
        self.minAddress = self.ihex.minaddr()
        self.maxAddress = self.ihex.maxaddr()
        return "OK"

    def writeToFile(self, outfilename):
        if not self.fileLoaded:
            return "No File Loaded"
        else:
            self.ihex.write_hex_file(outfilename)
            return "OK"

    def writeHexDump(self, fname):
        if not self.fileLoaded:
            return "No File Loaded"
        else:
            f = open(fname,'w')
            self.ihex.dump(f)
            f.close()
            return "Wrote " + fname

    def faultInjection(self, address, value):
        if not self.fileLoaded:
            return "No Hex File Loaded"
        elif address > self.maxAddress or address < self.minAddress:
            return "Address out of Range"
        else:
            self.ihex[address] = value
            self.ihex[address+1] = value
            self.faultList[address] = value
            #How to handle Low and High Byte!!!
            return "OK"

    def viewFaults(self):
        if not self.fileLoaded:
            return "No Hex File Loaded"
        else:
            return self.faultList            








#Print y newlines
#Formatting for 25 Line Terminal or CommandPrompt
def clearScreen(y):
    for x in range(0,y):
        print(" ")


def loadHex(avrhex,fname):
    if fname.lower() == 'c':
        return "Cancelled"
    elif (path.exists(fname)):
        return(avrhex.loadFromFile(fname))
    else:
        return("File Not Found: " + fname)


def writeHex(avrhex,fname):
    if fname.lower() == 'c':
        return "Cancelled"
    elif (path.exists(fname)):
        
        s = input("Overwrite Existing file? y/n: ")
        if s.lower() == "y":
            return(avrhex.writeToFile(fname))
        else:
            return("File Already Exists!")
    else:
        return(avrhex.writeToFile(fname))
    
def dumpHex(avrhex,fname):
    if fname.lower() == 'c':
        return "Cancelled"
    elif (path.exists(fname)):
        
        s = input("Overwrite Existing file? y/n: ")
        if s.lower() == "y":
            return(avrhex.writeHexDump(fname))
        else:
            return("File Already Exists!")
    else:
        return(avrhex.writeHexDump(fname))


def insertFaults(avrhex):
    print(" ")
    print(hex(avrhex.minAddress))
    print(hex(avrhex.maxAddress))
    addr=int(input("Enter HEX value in address range: 0x"),16)
    return(avrhex.faultInjection(addr,0x0000))

def branchDeletion():
    print('deletion')

def branchModification():
    print('mod')

def branchInsertion():
    print('ins')


def mainMenu():

    avrhex = IHexFile()
    print(" ")
    print("Arduino AVR Fault Injection Tool")
    print(" ")

    selection = 0
    while not (selection == '6'):

        print("AVR Fault Injection Tool")
        print(" ")
        print("1. Load Intel Hex File")
        print("2. Write Intel Hex File")
        print("3. Create Dump File")
        print("4. Insert Faults")
        print("5. View Faults")
        print("6. Quit")
        print(" ")
        
        selection = input("Enter number of your selection: ")
        if(selection is '1'):
            print(loadHex(avrhex,input("Enter HEX File to Load. 'c' to cancel: ")))
            
        elif(selection is '2'):
            print(writeHex(avrhex,input("Enter HEX File to Write. 'c' to cancel: ")))
            
        elif(selection is '3'):
            print(dumpHex(avrhex,input("Enter Dump File name. 'c' to cancel: ")))

        elif(selection is '4'):
            print(insertFaults(avrhex))

        elif(selection is '5'):
            print(avrhex.viewFaults())
            
        elif(selection is '6'):
            reallyQuit = input("Be sure to Write any changes before you quit. Ready to Quit? y/n :")
            if reallyQuit.lower()=='y':
                print("By Bye!")
            elif reallyQuit.lower()=='yes':
                print("So Long!")
            else:
                print("OK")
                selection = 0
        else:
            print("Please make a selection 1, 2, 3, 4, 5, or 6")
        

        
    


mainMenu()

#root = tk.Tk()

#w = tk.Label(root, text="Hello")
#w.pack()



#top.mainloop()



#Init hex
#ih = IntelHex()
#use fromfile to load file
#ih.fromfile('8d64.hex',format='hex')

#ih.dump()
#print(hex(ih.maxaddr()))
#print(hex(ih.minaddr()))


'''
i=0
while i < 32:
    #print(hex(ih[i]))
    ih.
    i+=1

'''






'''
byteList =  []

print("reading")

with open("8d64.hex","rb") as f:
    byte = f.read(1)
    i=0
    while byte != b"":
    #while i < 16:
        #print(byte.hex())
        byteList.append(byte)
        byte = f.read(1)
        i+=1

print("Writing")

with open("new.hex","wb") as f:
    for i in byteList:
        #print(i.hex())
        f.write(i)
'''



        
