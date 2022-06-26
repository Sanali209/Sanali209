
# webscraper for the website https://blendermarket.com/products
# to get articles placed on the website
# and save them in a html file

#import libraries
import requests
from bs4 import BeautifulSoup
import csv
import alipars

import FileIHave

# defain variables
url = 'https://blendermarket.com/products?sort_rating=4'
file_name = 'blendermarket.html'


# defain main function
def main():
    get_html(url, file_name)
    # parse the html file
    parse_html(file_name)



# defain function to get the html file
def get_html(url, file_name):
    # get the html file from the website
    response = requests.get(url)
    # save the html file
    with open(file_name, 'wb') as f:
        f.write(response.content)

# defain function to parse the html file
def parse_html(file_name):
    # open the html file
    with open(file_name, 'r') as f:
        # read the html file
        html = f.read()
    # parse the html file
    soup = BeautifulSoup(html, 'html.parser')
    # get the data
    data = soup.find_all('div', class_='card-product')
    # save the data
    save_data(data)

# defain function to save the data
def save_data(data):
    # create a list to save the data
    data_list = []
    # loop through the data
    for item in data:
        # get the data
        title = item.find('h5', class_='card-title').text
        # get image url for the article by class
        image_url = item.find('img', class_='card-img-top')['src']


        # save the data
        data_list.append([title, image_url])
    # save the data
    save_csv(data_list)

# defain function to save the data in a csv file
def save_csv(data_list):
    # create a csv file
    with open('blendermarket.csv', 'w', newline='') as f:
        # create a csv writer
        writer = csv.writer(f)
        # write the data
        writer.writerows(data_list)
    # open the csv file location in the browser
    open_csv()

# defain function to open the csv file location in the windows Explorer
def open_csv():
    # open the csv file location in the browser
    import os
    #convert csv file to a html file
    #title as the item file name and image as tumbnail
    os.system('csv2html.py blendermarket.csv blendermarket.html --title="blendermarket" --image="blendermarket"')
    # open the html file in the browser
    os.system('start blendermarket.html')


# call the fileIHave.py file
if __name__ == '__main__':
    alipars.open_max_file('Y:\_assetPacksRe\_unknown\3d model GROHE\Grohtherm\34179000 2.max')


