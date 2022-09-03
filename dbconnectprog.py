#this is a full working program to scrape the data and load it into mongodb
from pymongo import MongoClient
import pymongo
from input_urls import Url_To_Download
from scraper_function import Get_data_to_analyse
client = MongoClient('localhost',27017)
db = client['scrapindb']
#print(db.list_collection_names())
input_urls = Url_To_Download()
collection = db['Blackkoffer']
# cursor = collection.find({})
# for document in cursor:
#     print(document)

#db.collection.find({})
'''to insert a whole dictionary with title and data key,value pais we call the
functionn from within insert many column 
this will be second step after scraper does scraping we save the data in our own databse'''
#for i in range(0,len(input_urls)):
for i in range(0,len(input_urls)):
    item_to_insert = Get_data_to_analyse(i)
    collection.insert_one(item_to_insert)

