# utility for stagis

#resarch for all words in file and join them to one string


import fnmatch
import os
import csv


#search root
import re

dir = r"Y:\_Materials"

# stopwords variable for stopwords list wiz "the","a","an","and","or","but","for","is","in","of","on","to","with"
stopwords = ["the","a","an","and","or","but","for","is","in","of","on","to","with"]



#all pats words string
all_pats_words = ""

# function for recursive search all files in directory and subdir
def getFiles(rootDir, vildcard):
    files = []
    for root, sub_dirs, all_files in os.walk(rootDir):
        for filename in all_files:
            if fnmatch.fnmatch(filename, vildcard):
                files.append(os.path.join(root, filename))
    return files

# function for tocenize filepath for joining to list
def prepareFilePath(filePath):
    # all pat to lower case
    filePath = filePath.lower()

    # replase in  filepath strings : "\","/",":","_","-","." to " "
    filePath = filePath.replace("\\", " ")
    filePath = filePath.replace("/", " ")
    filePath = filePath.replace(":", " ")
    filePath = filePath.replace("_", " ")
    filePath = filePath.replace("-", " ")
    filePath = filePath.replace(".", " ")

    # todo: faind more easy way
    # replace all numbers chars  to " "
    filePath = re.sub(r'\s\d+\s', ' ', filePath)
    filePath = re.sub(r'\s+\d+\s+', ' ', filePath)

    # reprlace all allone 1 leter chars  to " "
    filePath = re.sub(r'\b[a-zA-Z]\b', ' ', filePath)

    # replace in filepath stopwords to waithspace
    # stopword have waithspaces
    for stopword in stopwords:
        filePath = filePath.replace(" "+stopword+" ", " ")

    print(filePath)
    return filePath

#function for loading .csv file and return list data csv separated by ","
def load_csv(file_name):
    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data = list(reader)
    #remuve captions from list
    data.pop(0)
    return data




# main function for script
# serch all files in directory and subdir and prepare each file path for tokenization
# joint all preapered file paths to one string
# split string to list of words
# delete all duplicates words
# join list of words to one string
# print string
# save string to file
def main():
    all_pats_words= ""
    # get files in directory and filter by mask
    files = getFiles(dir, "*.jpg")
    for file in files:
        #prepare file path
        filePath = prepareFilePath(file)
        #join list of words to one string
        all_pats_words = all_pats_words + " " + filePath
        #print string
        print(filePath)
    #split string to list of words
    all_pats_words = all_pats_words.split()
    #delete all empty words
    all_pats_words = [word for word in all_pats_words if word != ""]
    # sort words by frequency and store in dictionary word:frequency
    all_pats_words = dict(zip(all_pats_words, [all_pats_words.count(w) for w in all_pats_words]))

    # sort dictionary by frequency
    all_pats_words = sorted(all_pats_words.items(), key=lambda x: x[1], reverse=True)

    # load csv file
    data = load_csv(r"material taging.csv")
    completed_words = []
    # get list of words from csv file in column 3 if column 1 is "1"
    for item in data:
        if item[0] == "1":
           completed_words.append(item[2])
    print ("completed:",completed_words)
    listof_del_words = []

    count = 0

    # remuve words from all_pats_words list(compare as tuple) comparing with data list
    for word in all_pats_words:
        count=count+1
        print(count,word)
        keyword = word[0]
        print(keyword)
        if keyword in completed_words:
            listof_del_words.append(word)

    #remuve words from all_pats_words list
    for word in listof_del_words:
        all_pats_words.remove(word)

    print("list of deleted:",listof_del_words)


    # join dictionary to string
    all_pats_words = str(all_pats_words)

    #print string
    print(all_pats_words)
    #save string to file
    with open(r"all_pats_words.txt", "w") as outfile:
        outfile.write(all_pats_words)
    return all_pats_words





#call main function
main()