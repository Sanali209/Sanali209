# use https://github.com/ramnes/notion-sdk-py
#before run the programm, set the token
# and install the notion python library
# pip install notion-client

from notion_client import Client

token = 'secret_jBtg9jwGsBpYHy62OoMrFDCtQcsctBhTbGkFdE78J5Q'
db_id="c297f36903434c818cc8aeeee9cf0035"

def notion_test():
    notion = Client(auth=token)
    query = notion.databases.query(db_id)
    print (query)
    for item in query["results"]:
        bloc = notion.blocks.children.list(item["id"])
        print(bloc)

# call the main function
if __name__ == '__main__':
    notion_test()