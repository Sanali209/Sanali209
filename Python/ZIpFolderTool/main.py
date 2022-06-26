# import os
# fileNames = [fileName for fileName in os.listdir("data") if fileName.endswith(".txt")]

# if fnmatch.fnmatch(file.upper(), '*.TXT'):
# Use fnmatch: https://docs.python.org/2/library/fnmatch.html

# import modules
from programvar import vars as pv

import tkgui


# create gui instance
if __name__ == "__main__":
    pv.Initialize()
    gui = tkgui.Application()



#create ui for application
# 2 fielsd and 1 button with text "Zip"
# button "Zip" will call function zipFiles
# 2 fields will be filled with values rootSerchPath and ZipFileName
def askdirectory():
    rootSerchPath = "askdirectory()"
    return "123"



