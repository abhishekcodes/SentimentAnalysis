from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as BS4
from input_urls import Url_To_Download

input_urls = Url_To_Download()

def Get_data_to_analyse(i):
    Posts_Data = {}
    req = Request(url=input_urls[i],headers={'user-agent':'Sentiapp'})
    response = urlopen(req)
    html = BS4(response,'lxml')
    #print(html)
    title = html.find("h1",{"class":"entry-title"}).get_text()
    date = html.find("time",{"class":"entry-date updated td-module-date"}).get_text()
    time = html.time["datetime"][11:16]
    print(title,date,time)
    post_data = html.find("div", {"class":"td-post-content"}).get_text()
    #print(post_data)
    Posts_Data['article_name']= title
    Posts_Data['article_data'] = post_data
    Posts_Data['article_date'] = date
    Posts_Data['article_time'] = time
     #It is here to run the loop just one time for efficiency
    return Posts_Data


#Get_data_to_analyse()
#print(Posts_Data)
