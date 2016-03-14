__author__ = 'FlavioMatheus'

from PIL import Image

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