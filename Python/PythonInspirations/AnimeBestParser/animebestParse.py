# scraper for https://animebest.org/
# scrap list of all anime posts and his data
# data is name, imageUrl, url, rating, description
# data stored to local sqllite database

#todo: load data from local database for future use
#todo: add a function for checking data diference between local and online parseted data

# import the modules
import os
import time
import pickle
import requests
from bs4 import BeautifulSoup
# import sqlite3
import sqlite3


#var for location of sqlite database


db_location = 'animebest.db'





# declare the variables
url = 'https://animebest.org'




# defain class to store the data of parsed items with fields name, imageUrl, url, rating, description
class AnimeItem:
    def __init__(self, name, imageUrl, url, rating, description):
        self.name = name
        self.imageUrl = imageUrl
        self.url = url
        self.rating = rating
        self.description = description

class AnimeBestparser:
    # list for hold pars htmls and add url to it
    pars_urls = [url]

    # list of parsed urls
    parsed_urls = []

    # list of all anime items
    anime_items = []

    curPageHTML = ""

    def __init__(self):
        self.url = url
    def get_html(self, url):
        # get the html in utf-8
        #create requestvar for request set encoding to utf-8 and get the html
        request = requests.get(url)
        print ('request status:', request.status_code)
        print('request url:', request.url)
        print('request encoding:', request.encoding)
        #sleep tread 5 seconds for read html
        time.sleep(0)

        self.curPageHTML = request.content.decode("utf-8", "ignore")
        # print the url viz "getting html:"
        print('getting html:', url)

    def getListAnimeItems(self):
        # parse the html file
        soup = BeautifulSoup(self.curPageHTML, 'html.parser')
        # get the data
        data = soup.find_all('div', class_='col-md-4sh col-xs-12')
        # print items count foundet viz caption
        print('items count found:', len(data))
        # save the data
        for item in data:
            # get the data
            # faind <a> tag and get title atrribute

            aref = item.find('a')
            if (aref is not None):
                # get the title
                name = aref.get('title')
                # get the url
                url = aref.get('href')
            else:
                name = 'no title'
                url = 'no url'
                print('no title')
                print('no url')

            print('name:', aref.get('title'))
            print('url:', aref.get('href'))
            # get image url for the article by class
            imageItem = item.find('meta', itemprop='image')
            image_url = item.find('meta', itemprop='image').get('content')
            print('image url:', image_url)
            # get the rating
            rating = item.find('span', class_='short-images-rate').text
            print('rating:', rating)
            # todo: get the description
            # save the data
            self.anime_items.append(AnimeItem(name, image_url, url, rating, description=''))

    def getListNextParse(self):
        # parse the html file
        soup = BeautifulSoup(self.curPageHTML, 'html.parser')
        # get the data
        data = soup.find_all('div', class_='pages-numbers')
        # if data lenth is greater than 0
        if len(data) > 0:
            # filter data hold onli <a> tags
            data = [item for item in data[0] if item.name == 'a']
            # save the data
            for item in data:
                # filter items if they are not already parsed
                if item.get('href') not in self.parsed_urls:
                    # add url to the list
                    self.pars_urls.append(item.get('href'))
                    # print url viz "link found:"
                    print('link found:', item.get('href'))
        # else print "no links found"
        else:
            print('no links found')

    #defain for main class logic name parse
    def parse(self):
        # wile loop for parsing the urls by url cursor
        while len(self.pars_urls) > 0:
            # get the url from the list
            url = self.pars_urls.pop(0)
            # if url is not already parsed
            if url not in self.parsed_urls:
                # add url to the list
                self.parsed_urls.append(url)
                # get the html
                self.get_html(url)
                # get the list of anime items
                self.getListAnimeItems()
                # get the list of next parse urls
                self.getListNextParse()

                # print the url viz "parsed:"
                print('parsed:', url)
            # else print "url already parsed"
            else:
                print('url already parsed')




    #defain main function for saving the data as html file
    def save_html(self):
        # create the file wiz javascript items table viz futures of sorting

        #open html file fore write and set encoding to utf-8
        with open('animebest.html', 'w',encoding= "utf-8") as f:
            #write the header
            f.write('<html>\n')
            #write set carset to utf-8 in header
            f.write('<head><meta charset="UTF-8"></head>\n')

            #write the body
            f.write('<body>\n')
            # add javascript sortable-0.8\js\sortable.js
            f.write('<script src="sortable-0.8.0\js\sortable.js"></script>\n')
            f.write('<link rel="stylesheet" href="sortable-0.8.0/css/sortable-theme-finder.css"/>\n')
            #write document title "Animebest articles" viz bold text
            f.write('<h1>Animebest articles</h1>\n')
            #write the table data-sortable
            f.write('<table class="sortable-theme-finder" data-sortable>\n')

            #write the header image,name,rating
            f.write('<thead>\n')
            f.write('<th>Image</th>\n')
            f.write('<th>Name</th>\n')
            f.write('<th>Rating</th>\n')
            f.write('</tr>\n')
            f.write('</thead>\n')
            #write the data first draw image and link it to post url afte draw name and rating
            # use utb8 for correct encoding
            f.write('<tbody>\n')
            for item in self.anime_items:

                f.write('<tr>\n')
                # size of image max width is 100px link image href to post url
                f.write('<td><img href="'+item.url+'" src="' + item.imageUrl + '" width="200px"/></td>\n')
                try:
                    f.write('<td><a href="'+item.url+'">'+item.name+'</a></td>\n')
                except:
                    print('no title')


                f.write('<td>' + item.rating + '</td>\n')

            f.write('</tbody>\n')
            #write the table
            f.write('</table>\n')
            #write the body
            f.write('</body>\n')
            #write the html
            f.write('</html>\n')










class DBManager:
    # defain constructor
    def __init__(self, db_location):
        self.db_location = db_location
        self.conn = sqlite3.connect(db_location)
        self.c = self.conn.cursor()

    # defain create table function
    def create_tables(self):
        # sql query to create items table
        #  fields id as praimari key,name,imageUrl,url,rating is integer,description
        sql_create_table = """CREATE TABLE IF NOT EXISTS animebest (
                            id integer PRIMARY KEY,
                            name text NOT NULL,
                            imageUrl text NOT NULL,
                            url text NOT NULL,
                            rating integer NOT NULL,
                            description text NOT NULL
                            );"""
        self.c.execute(sql_create_table)
        #sql query to create tags table
        # table fields id as praimari key,name
        sql_create_table = """CREATE TABLE IF NOT EXISTS tags (
                            id integer PRIMARY KEY,
                            name text NOT NULL
                            );"""
        self.c.execute(sql_create_table)
        #sql query to create tags_items table
        # table fields id as praimari key,tag_id,item_id
        sql_create_table = """CREATE TABLE IF NOT EXISTS tagsrel (
                            id integer PRIMARY KEY,
                            tag_id integer NOT NULL,
                            item_id integer NOT NULL
                            );"""
        self.c.execute(sql_create_table)
        self.c.execute(sql_create_table)
        # commit the changes
        self.conn.commit()



    # defain check table exist function
    def check_table_exist(self, table_name):
        self.c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        return self.c.fetchall()

    #defain function to create tablse if not exist
    def create_table_if_not_exist(self):
        if not self.check_table_exist('animebest') or not self.check_table_exist('tags') or not self.check_table_exist('tagsrel'):
            self.create_tables()

    # defain insert data function
    def insert_data(self, name, imageUrl, url, rating, description):
        # sql query to insert data into items table
        sql_insert_data = """INSERT INTO animebest (name, imageUrl, url, rating, description)
                            VALUES (?, ?, ?, ?, ?)"""
        self.c.execute(sql_insert_data, (name, imageUrl, url, rating, description))
        self.conn.commit()

    # defain insert tag function
    def insert_tag(self, name):
        self.c.execute("INSERT INTO tags VALUES (NULL, ?)", (name,))
        self.conn.commit()

    # defain insert tag_item function
    def insert_tag_item(self, tag_id, item_id):
        self.c.execute("INSERT INTO tagsrel VALUES (NULL, ?, ?)", (tag_id, item_id))
        self.conn.commit()

    # defain add tag to item function
    def add_tag_to_item(self, tag_name, item_name):
        # get tag id
        self.c.execute("SELECT id FROM tags WHERE name=?", (tag_name,))
        tag_id = self.c.fetchone()[0]
        # if tag id is not found, insert tag
        if tag_id is None:
            self.insert_tag(tag_name)
            tag_id = self.c.lastrowid
        # get item id
        self.c.execute("SELECT id FROM animebest WHERE name=?", (item_name,))
        item_id = self.c.fetchone()[0]
        # insert tag to item
        self.insert_tag_item(tag_id, item_id)


    # defain get tags function
    def get_tags(self, item_id):
        self.c.execute("SELECT tags.name FROM tagsrel INNER JOIN tags ON tagsrel.tag_id = tags.id WHERE tagsrel.item_id = ?", (item_id,))
        return self.c.fetchall()

    # defain select data function
    def select_data(self):
        self.c.execute("SELECT * FROM animebest")
        return self.c.fetchall()

    # defain save animebest data to db function
    def save_animebest_data(self, animebest):
        for item in animebest.anime_items:
            # get item by url
            self.c.execute("SELECT * FROM animebest WHERE url=?", (item.url,))
            item_db = self.c.fetchone()
            # if item is not found, insert item
            if item_db is None:
                self.insert_data(item.name, item.imageUrl, item.url, item.rating, item.description)









def main():
    # create a new instance of the class DBManager
    db = DBManager(db_location)
    db.create_table_if_not_exist()
    parser = AnimeBestparser()
    parser.parse()
    db.save_animebest_data(parser)
    parser.save_html()

    # get the html file
   # html = get_html(pars_urls[0])
   # getListNextParse(html)
   # getListAnimeItems(html)
   # save_csv()
    #convert csv to html
   # save_html()





# call the main function
if __name__ == '__main__':
    main()
