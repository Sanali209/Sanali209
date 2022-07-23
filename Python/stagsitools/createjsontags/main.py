# script for discovering files in a directory and creating a json file with tags by rules

# import modules
import fnmatch
import os
import json
import re
import shutil
import zipfile
import time
import sys
import datetime
import csv
import requests
import urllib.request
import urllib.parse
import urllib.error

# define a master folder and suffix name
folder = r"Y:\_Materials\CGAxis - Physical 2\4K Physical 2 Fabrics"

# variable for mascking the file name for search
mask = "*.jpg"

#rule for taging the files
rules = {"vildcard": "*cgaxis*.*", "tag": "cgaxis"}, {"vildcard": "*fabric*.*", "tag": "fabric"}

# variable for hold json data
# import using a simple JSON file containing an array of objects with keys: File (imported file’s path, relative to the JSON file),
# Tags (array of objects). Tags has two keys: mandatory Tag (array of strings – tag path) and optional Weight (defaults to 0).
# This example assigns two tags: Artists/"Yuno Nagasaki" (with -1 weight) and Year/1990s/1999 (with 0 weight
# json example:
# [
#  {
#    "File": "..\\music.mp3",
#    "Tags": [
#      {"Tag": ["Artists", "Yuno Nagasaki"], "Weight": -1},
#      {"Tag": ["Year", "1990s", "1999"]}
#    ]
#  }
# ]
jsonData = []

jsonfilepath = r"tags.json"

# function get files recursive in directory and subdir and filter by vildcard
def getFiles(rootDir, vildcard):
    files = []
    for root, sub_dirs, all_files in os.walk(rootDir):
        for filename in all_files:
            if fnmatch.fnmatch(filename, vildcard):
                files.append(os.path.join(root, filename))
    return files

#function for compare filepaths with rules and return tags
def getTags(filePath, rules):
    tags = []
    for rule in rules:
        if fnmatch.fnmatch(filePath, rule["vildcard"]):
            tags.append(rule["tag"])
    return tags

# function for apend json data tags as objects for tag item to jsonData as  {"Tag": ["Artists", "Yuno Nagasaki"], }
def appendJsonData(filePath, tags):
    jsonfortags = {}
    #append file path in relative to json file
    jsonfortags["File"] = filePath
    jsonfortags["Tags"] = []
    for tag in tags:
        jsonfortags["Tags"].append({"Tag": [tag]})
    print (jsonfortags)

    jsonData.append(jsonfortags)



# main function
def main():
    # get files in directory and filter by mask
    files = getFiles(folder, mask)
    #set jsonfilepath to current root directory
    jsonfilepath = folder+"\\tags.json"

    print(files)
    # get tags for files
    for file in files:
        # set file path relative to current root directory

        tags = getTags(file, rules)
        print(tags)
        # append json data
        appendJsonData(file, tags)
    # save json data to json file



    with open(jsonfilepath, 'w') as outfile:
        json.dump(jsonData, outfile)
    # print("Done")

    # call main function
main()