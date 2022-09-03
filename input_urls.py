#this file will give input to the scraper_function file

import pandas as pd
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

#input_df = Url_To_Download()

