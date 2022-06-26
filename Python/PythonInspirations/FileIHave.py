# parsing content of folder "Y:\Soft"
# and create html file viz parset data and store to folder "Y:\Soft\soft catalog.html"

# imort the library
import sys
import os

# for pdf writing use report lab
# import the library
from reportlab.pdfgen import canvas
#defain clas to store the data of parsed items with fields name, image, location




class Item:
    def __init__(self, name, image, location):
        self.name = name
        self.image = image
        self.location = location



#defain recursive function to get files and folders in a folder "Y:\Soft"
# store the all items data in a list of Item class
def get_files_and_folders(path):
    # create a list to store the data
    data_list = []
    # get the files and folders in the folder "Y:\Soft"
    for item in os.listdir(path):
        # get the item path
        item_path = os.path.join(path, item)
        # check if the item is a file
        if os.path.isfile(item_path):
            # get the item name
            name = item
            # get the item image if item is image
            if item.endswith('.jpg') or item.endswith('.png'):
                image = item_path
                # if item not image get icon of file
            else:
                image = 'https://www.iconfinder.com/data/icons/file-type-icons-8/512/' + item + '.png'
            # get the item location
            location = path
            # create an item object
            item_object = Item(name, image, location)
            # add the item object to the list
            data_list.append(item_object)
        # check if the item is a folder
        elif os.path.isdir(item_path):
            # get the item name
            name = item
            # get the folder image
            image = 'https://www.iconfinder.com/data/icons/file-type-icons-8/512/folder.png'
            # get the item location
            location = path
            # create an item object
            item_object = Item(name, image, location)
            # add the item object to the list
            data_list.append(item_object)
            # get the files and folders in the folder "Y:\Soft\item"
            data_list.extend(get_files_and_folders(item_path))
    # return the list
    return data_list

# defain function to save the data in pdf file
def save_pdf(data_list):
    # create a pdf file
    c = canvas.Canvas('soft catalog.pdf')

    # create a counter to store the number of items
    counter = 0
    pcounter = 0
    # create vars for storing writeing position
    x = 0
    y = 0
    # loop through the data
    for item in data_list:
        #bild layout of the pdf file
        # increase vars for writing position

        y = 200*pcounter

        # get the item name
        name = item.name
        # get the item image
        image = item.image
        # get the item location
        location = item.location
        #get file viz location
        file_viz = os.path.join(location, name)

        # get the icon path
        #icon_path = get_icon_filename(file_viz,32)
        #c.drawImage(icon_path, x, y, width=100, height=100)
        # create a image and draw if image is jpg
        if image.endswith('.jpg'):
            c.drawImage(image, x, y, width=200, height=180)

        # create a text name and draw in position
        c.setFont('Helvetica', 20)
        c.drawString(x, y, name)
        # create a text location and draw in position
        c.setFont('Helvetica', 10)
        c.drawString(x, y-20, location)
        # add 1 page to the document
        pcounter += 1
        if pcounter == 4:
            c.showPage()
            pcounter = 0

        # increase the counter
        counter += 1
    #save the pdf file
    c.save()
    #open the pdf file
    os.startfile('soft catalog.pdf')