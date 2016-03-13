__author__ = 'rodrigoguimaraes'

from PIL import Image


def steg(listOfChars, looping):
    im = Image.open ("img/input.jpg")
    px = im.load()
    strChar = 0
    charNo = 0
    for i in range(im.height):
        for j in range(im.width):
            bitToInsert = listOfChars[charNo][strChar]
            if(bitToInsert == 0 and px[j,i][0]%2 == 1):
                px[j,i] = (px[j,i][0] - 1,px[j,i][1],px[j,i][2])
            elif(bitToInsert == 1 and px[j,i][0]%2 == 0):
                px[j,i] = (px[j,i][0] + 1,px[j,i][1],px[j,i][2])
            strChar+=1
            if(strChar == 8):
                strChar = 0
                charNo += 1
                if(charNo == len(listOfChars)):
                    if(looping):
                        charNo = 0
                    else:
                        im.save("img/output.bmp","bmp")
                        return
    im.save("img/output.bmp","bmp")
    return

def deSteg():
    im = Image.open ("img/output.bmp")
    px = im.load()
    calc = '0b'
    strChar = 0
    charList = []
    for i in range(im.height):
        for j in range(im.width):
            bitRead = px[j,i][0]%2
            calc = calc + str(bitRead)
            strChar += 1
            if(strChar == 8):
                strChar = 0
                charList.append(chr(int(calc, 2)))
                calc = '0b'
    print(''.join(charList))

def saveToFile(newFileBytes):
    newFileByteArray = bytearray(newFileBytes)
    # make file
    newFile = open ("output2.mid", "wb")
    newFile.write(newFileByteArray)

def deStegToFile(numBytes):
    im = Image.open ("img/output.bmp")
    px = im.load()
    calc = '0b'
    strChar = 0
    charList = []
    charNo = 0
    for i in range(im.height):
        for j in range(im.width):
            bitRead = px[j,i][0]%2
            calc = calc + str(bitRead)
            strChar += 1
            if(strChar == 8):
                strChar = 0
                charList.append(chr(int(calc, 2)))
                calc = '0b'
                charNo += 1
                if(charNo == numBytes):
                    saveToFile(charList)
                    return;
    saveToFile(charList)




def stringToBitArray(input):
    myList = [ord(c) for c in input]
    myListResult = []
    for i in range(len(myList)):
        temp = bin(myList[i])
        temp = temp[2:]
        while(len(temp) < 8):
            temp = "0" + temp
        tempChar = []
        for j in range(8):
            tempChar.append(int (temp[j]))
        myListResult.append(tempChar)
    return myListResult



#steg(stringToBitArray("RODRIGO - "), True)
#deSteg()

strOut = ""
f = open("mario.mid", "rb")
try:
    byte = f.read(1)
    while byte != "":
        strOut = strOut + byte
        byte = f.read(1)
finally:
    f.close()

numBytes = len(strOut)

steg(stringToBitArray(strOut), False)
deStegToFile(numBytes)

