# scraper for https://animebest.org/
# scrap list of all anime posts and his data
# data is name, imageUrl, url, rating, description
# data stored to local csv file







# import the modules
import os
import requests
from bs4 import BeautifulSoup
import csv





# declare the variables
url = 'https://animebest.org'

# list for hold pars htmls and add url to it
pars_html = [url]

# list of parsed urls
parsed_urls = []

# list of all anime items
anime_items = []


# defain class to store the data of parsed items with fields name, imageUrl, url, rating, description
class AnimeItem:
    def __init__(self, name, imageUrl, url, rating, description):
        self.name = name
        self.imageUrl = imageUrl
        self.url = url
        self.rating = rating
        self.description = description


# defain get_html function to get the html file and return response content
def get_html(url_Path):
    # get the html file from the website
    response = requests.get(url_Path)
    # print pars_html[url_index] and response.status_code all in new line
    print(url_Path, response.status_code, '\n')
    # save the html file
    return response.content


# defain getList os url pars next pages from the html file
def getListNextParse(response_content):
    html = response_content
    # parse the html file
    soup = BeautifulSoup(html, 'html.parser')
    # get the data
    data = soup.find_all('div', class_='pages-numbers')
    # if data lenth is greater than 0
    if len(data) > 0:
        # filter data hold onli <a> tags
        data = [item for item in data[0] if item.name == 'a']
        # save the data
        for item in data:
            # filter items if they are not already parsed
            if item.get('href') not in parsed_urls:
                # add url to the list
                pars_html.append(item.get('href'))
                # print url viz "link found:"
                print('link found:', item.get('href'))
    # else print "no links found"
    else:
        print('no links found')


# defain getList of anime items from html string
def getListAnimeItems(html):
    # parse the html file
    soup = BeautifulSoup(html, 'html.parser')
    # get the data
    data = soup.find_all('div', class_='col-md-4sh col-xs-12')
    # print items count foundet viz caption
    print('items count found:', len(data))
    # save the data
    for item in data:
        # get the data
        # faind <a> tag and get title atrribute

        aref= item.find('a')
        if(aref is not None):
            #get the title
            name = aref.get('title')
            #get the url
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
        anime_items.append(AnimeItem(name, image_url, url, rating,description=''))

# function to save items list to csv file
def save_csv():
    # create a csv file
    with open('animebest.csv', 'w', newline='') as f:
        # create a csv writer
        writer = csv.writer(f)
        # write the header
        writer.writerow(['name', 'imageUrl', 'url', 'rating', 'description'])
        # write the data
        for item in anime_items:
            writer.writerow([item.name, item.imageUrl, item.url, item.rating, item.description])

#defain main function for saving the data as html file
def save_html():
    #open html file fore write
    with open('animebest.html', 'w') as f:
        #write the header
        f.write('<html>\n')
        #write the body
        f.write('<body>\n')
        #write document title "Animebest articles" viz bold text
        f.write('<h1>Animebest articles</h1>\n')
        #write the table
        f.write('<table>\n')
        #write the header image,name,rating
        f.write('<tr>\n')
        f.write('<th>Image</th>\n')
        f.write('<th>Name</th>\n')
        f.write('<th>Rating</th>\n')
        f.write('</tr>\n')

        #write the data first draw image and link it to post url afte draw name and rating
        for item in anime_items:
            f.write('<tr>\n')
            f.write('<td><img href="'+item.url+'" src="' + item.imageUrl + '"/></td>\n')
            f.write('<td><a href="' + item.url + '">' + item.name + '</a></td>\n')
            f.write('<td>' + item.rating + '</td>\n')

        #write the table
        f.write('</table>\n')
        #write the body
        f.write('</body>\n')
        #write the html
        f.write('</html>\n')

# defain main function to start the program
def main():

    # get the html file
    html = get_html(pars_html[0])
    getListNextParse(html)
    getListAnimeItems(html)
    save_csv()
    #convert csv to html
    save_html()




# call the main function
if __name__ == '__main__':
    main()
