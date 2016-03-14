__author__ = 'rodrigoguimaraes'

from PIL import Image
import subprocess
import Steganography
import Helpers

# "img/input.jpg"
# "img/output.bmp"

if __name__ == '__main__':


    mode = raw_input('Choose a mode between steg and desteg:')

    if mode == "steg":

        fileName = raw_input('Would You Kindly Give the Name of The File:')
        audioName = raw_input('Would You Kindly Give the Name of the Audio File:')

        strOut = ""
        f = open(audioName, "rb")
        try:
            byte = f.read(1)
            while byte != "":
                strOut = strOut + byte
                byte = f.read(1)
        finally:
            f.close()

        numBytes = len(strOut)

        Steganography.steg(Helpers.stringToBitArray(strOut), False, fileName)

    elif mode == "desteg":

        fileName = raw_input('Would You Kindly Give the Name of the File:')

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

        Steganography.deStegToFile(numBytes, fileName)

        #TO PLAY, IT IS CONSIDERING THAT YOU HAVE Aria Maestosa copied to your applications folder
        pathApp = "/Applications/Aria Maestosa.app/Contents/MacOS/Aria Maestosa"
        pathFile = "output.mid"

        im = Image.open ("img/output.bmp")
        im.show()
        subprocess.call([pathApp, pathFile])
