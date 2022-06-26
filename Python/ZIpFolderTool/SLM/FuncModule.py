# import
import fnmatch
import os

# function get files in directory and filter by filter delegate
def getZipingdFiles(curZipDir):
    ZipedFiles = []
    for curentFile in os.listdir(curZipDir):
        if not fnmatch.fnmatch(curentFile.lower(), '*render*') and not fnmatch.fnmatch(curentFile.lower(), '*.zip'):
            ZipedFiles.append(curentFile)
    return ZipedFiles

# function for print to console and save to file
def printToConsoleAndFile(text):
    print(text)
    with open("log.txt", "a") as myFile:
        myFile.write(text + "\n")

# funvtion get directories in directory recursively
def getDirectories(rootSerchPath):
    Directories = []
    for file in os.listdir(rootSerchPath):
        if os.path.isdir(os.path.join(rootSerchPath, file)):
            Directories.append(os.path.join(rootSerchPath, file))
    return Directories

