# depenci
#  pip install  pyexiftool
# todo: report taging progress
# todo:improve performance by using batch processing
# todo:improve performance by using rewrite metadata
# bug: fnmatch matching for files with no word separated pattern
import fnmatch
import os
import re
import sys
import time
import csv

from exiftool import ExifToolHelper

worc_dir = r"Y:\_Materials\cgaxis\CGAxis PBR Textures Collection"
# scan dir and create tag list write tags to xmp file
# stopwords variable for stopwords list wiz "the","a","an","and","or","but","for","is","in","of","on","to","with"
stopwords = ["the", "a", "an", "and", "or", "but", "for", "is", "in", "of", "on", "to", "with"]

tag_rewrite = True

# variables for hold list of taging rules format key:value
# key - tag wildcard
# value - tag value
tag_rules = {}


# function for recursive search all files in directory and subdir
def getFiles(root_dir, wildcard):
    files = []
    for root, sub_dirs, all_files in os.walk(root_dir):
        for filename in all_files:
            if fnmatch.fnmatch(filename, wildcard):
                files.append(os.path.join(root, filename))
    return files


# function for tokenize filepath for joining to list
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
        filePath = filePath.replace(" " + stopword + " ", " ")

    return filePath


# get tags by rules from filepath
def getTagsByRules(filePath):
    # create list of tags by rules
    tags = []
    # filepath to lower case
    filePath = filePath.lower()
    for rule in tag_rules:
        getvildkard = tag_rules[rule]
        if fnmatch.fnmatch(filePath, getvildkard):
            tags.append(rule)
    return tags


# function create proposition tags
def createPropositionTags(workPath, vildcard):
    files = getFiles(workPath, vildcard)
    # all pats words text string
    all_pats_words_text: str = ""
    for file in files:
        all_pats_words_text += prepareFilePath(file)
    all_pats_words_list = all_pats_words_text.split()
    # delete all empty words
    all_pats_words_list = [word for word in all_pats_words_list if word != ""]

    # create words by frequency and store in dictionary viz list hold word:frequency:count
    all_pats_words_dict = {}
    counter = 0
    for word in all_pats_words_list:
        if word in all_pats_words_dict:
            all_pats_words_dict[word][0] += 1
        else:
            freq = 1
            all_pats_words_dict[word] = [freq, counter]
            counter += 1

    # sort dictionary by frequency
    all_pats_words_dict = sorted(all_pats_words_dict.items(), key=lambda x: x[1], reverse=True)

    return all_pats_words_dict


# function for create rule
def createRule(tag, vildkard):
    tag_rules[tag] = vildkard
    return tag_rules


# function save rules to csv use csv module fore separate tags and vildkard use ";"
def saveRules(rules):
    with open("rules.csv", "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=";", lineterminator='\n')
        for rule in rules:
            tag = rule
            vildkard = tag_rules[rule]
            writer.writerow([tag, vildkard])


# function load rules from csv use csv module
def loadRules():
    if os.path.exists("rules.csv"):
        with open("rules.csv", "r") as csv_file:
            reader = csv.reader(csv_file, delimiter=";")
            for row in reader:
                tag = row[0]
                vildkard = row[1]
                createRule(tag, vildkard)


# funcyion for read tags from file IPTC metadata
def readTags(file):
    with ExifToolHelper() as et:
        for d in et.get_tags(file, tags=["IPTC:Keywords"]):
            for k, v in d.items():
                if (k == "IPTC:Keywords"):
                    return v


# function for set tags to file from list of tags
def setTags(file, tags):
    try:
        with ExifToolHelper() as et:
            et.set_tags(file, tags={"IPTC:Keywords": tags})

    except Exception as e:
        print(e)
        print("Error set tags to file: " + file)
        return False


# main function
# on the start load rules from csv file
# loop function he ask user to choose action
# if user choose 1 - show all rules
# if user choose 2 - create new rule
# if user choose 3 - edit rules (change tag or wildcard)
# if user choose 4 - edit rules viz proposition tags
# if user choose 5 - delete rule
# if user choose 6 - process files and set tags
# if user choose 0 - exit
# on the end save rules to csv file
def main():
    loadRules()
    while True:
        print("1 - show all rules")
        print("2 - create new rule")
        print("3 - edit rules (change tag or vildkard)")
        print("4 - edit rules viz proposition tags")
        print("5 - delete rule")
        print("6 - process files and set tags")
        print("0 - exit")
        choice = input("Enter your choice: ")
        print("_________________________________________")
        if choice == "1":
            print("Rules:")
            counter = 1
            for rule in tag_rules:
                print(str(counter) + ":" + rule + ": " + tag_rules[rule])
                counter += 1
        elif choice == "2":
            print("create new rule")
            tag = input("Enter tag: ")
            vildkard = input("Enter vildkard: ")
            createRule(tag, vildkard)
        elif choice == "3":
            print("edit rules")
            tag = input("Enter tag: ")
            vildkard = input("Enter vildkard: ")
            tag_rules[tag] = vildkard
        elif choice == "4":
            print("Proposition tags:")
            # get input from user vildkard viz default value="*"
            vildkard = input("Enter vildkard: ")
            if vildkard == "":
                vildkard = "*"

            # get all proposition tags
            all_pats_words_dict = createPropositionTags(worc_dir, vildkard)
            # filter proposition tags if they no exist in rules
            all_pats_words_dict = [tag for tag in all_pats_words_dict if not tag[0] in tag_rules]
            # print all proposition tags wis word wrap
            tags_text = ""
            counter = 1
            for tag in all_pats_words_dict:
                tags_text += tag[0] + ": " + str(tag[1][0]) + ": " + str(tag[1][1]) + " "
                val = counter % 5
                if val == 0:
                    tags_text += "\n"
                counter += 1

            print(tags_text)
            # print(all_pats_words_dict)
            noexit = True
            while noexit:
                # ask user to choose tag to edit by number
                tag_number = input("Enter tag number,separate tags by" "waith space: ")
                multiple_tags = tag_number.split(" ")
                for tag_number in multiple_tags:
                    if tag_number.isdigit():
                        tag_number = int(tag_number)
                        # faind tag in list by number
                        tag = None
                        for key, value in all_pats_words_dict:
                            if value[1] == tag_number:
                                tag = [key, value[0], value[1]]
                                break
                        if tag is not None:
                            print(
                                "Tag proposition: " + tag[0] + " Frequency: " + str(tag[1]) + " Number: " + str(tag[2]))
                            # ask user add new rule or not
                            add_rule = input("Add rule? (y/n): ")
                            if add_rule == "y":
                                tag_rules[tag[0]] = "*" + tag[0] + "*"

                    else:
                        print("Wrong tag number")
                        noexit = False
                        break


        elif choice == "5":
            print("delete rule")
            tag = input("Enter tag: ")
            del tag_rules[tag]
        elif choice == "6":
            # get input from user wildcard viz default value="*"
            vildkard = input("Enter wildcard: ")
            if vildkard == "":
                vildkard = "*"
            files = getFiles(worc_dir, vildkard)
            for file in files:
                if not tag_rewrite:
                    # process filepath and get tags
                    tags = readTags(file)
                else:
                    tags = None
                # process tags and get new tags by rules
                new_tags = getTagsByRules(file)
                # todo: no write tags if the ecvals in files metadata and tags by rules
                # merge unique tags
                if tags is None:
                    # check if tags not equal to none string
                    tags = "None"

                # check tags if they typeof string
                if type(tags) is str:
                    # check if tags not empty in lower case
                    if tags.lower() == "none":
                        tags = []
                    else:
                        tags = [tags]
                new_tags = list(set(tags + new_tags))

                # set tags to file
                print("Set tags to file: " + file)
                print(new_tags)
                sys.stdout.flush()
                time.sleep(.2)
                setTags(file, new_tags)



        elif choice == "0":
            saveRules(tag_rules)
            break
        else:
            print("Invalid choice")


main()
