file_path =r'C:\Users\abhis\Downloads\Input.xlsx'

def Url_To_Download():
    import pandas as pd
    file_path = r'C:\Users\abhis\Downloads\Input.xlsx'
    df = pd.read_excel(file_path,engine='openpyxl')
    df.dropna(axis=1,inplace=True)
    #print(df.head())
    url_to_download = df['URL']
    #print(url_to_download)
    return url_to_download


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as BS4
from input_urls import Url_To_Download

input_urls = Url_To_Download()
def Get_data_to_analyse():
    Posts_Data={}
    for i in range(0,5):
        req = Request(url=input_urls[i],headers={'user-agent':'Sentiapp'})
        response = urlopen(req)
        html = BS4(response,'lxml')
        #print(html)
        title = html.find("h1",{"class":"entry-title"}).get_text()
        print(title)
        post_data = html.find("div", {"class":"td-post-content"}).get_text()
        #print(post_data)
        Posts_Data[title] = post_data
         #It is here to run the loop just one time for efficiency
        i +=1
    return Posts_Data

from scraper_function import Get_data_to_analyse
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
Data = Get_data_to_analyse()

def getList(dict):
    '''to return a list of key so that relevant data can be picked form
        dictionary'''
    return list(Data)

article_name = getList(Data)
print(article_name)

sentimentList = []

def dataToProcess(i):
    article_data = str(Data[article_name[i]])
    return article_data

for i in range(0,len(Data)):
    article = dataToProcess(i)
#print(article)

#nltk analysis
#1 removing stopwords
    def preProcesstext(article):
        stop_words = set(stopwords.words('english'))
        wnl = WordNetLemmatizer()
        tokenizer = RegexpTokenizer(r"\w+")
        word_tokens = tokenizer.tokenize(article)
        filtered_article = [w for w in word_tokens if not w.lower() in stop_words]
        filtered_article = []
        for w in word_tokens:
            if w not in stop_words:
                filtered_article.append(w)
        return filtered_article

    vader_text = preProcesstext(article)
    print(vader_text)

    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    import pandas as pd

    column=['text']
    df_SI = pd.DataFrame(vader_text,columns=column)

    vader = SentimentIntensityAnalyzer()
    f = lambda text: vader.polarity_scores(text)['compound']
    df_SI['compound'] = df_SI['text'].apply(f)

    sum = df_SI['compound'].sum()

    sentimentList.append(sum)
    print(sentimentList)
    if sum > 0:
        print("this is a positive text")
    else:
        print("this is a negative text")
