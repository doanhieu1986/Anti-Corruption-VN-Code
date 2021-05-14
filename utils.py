from bs4 import BeautifulSoup
import requests
import os
import glob
import pandas as pd
from datetime import datetime


# Function get content from link
def read_content(link_vnexpress):
    if link_vnexpress.split('/')[2] == "video.vnexpress.net":
        return ["Not defined", "Not defined", "Not defined"]
    else:
        content_list = []
        response = requests.get(link_vnexpress)   
        content = BeautifulSoup(response.content, "html.parser").find_all('p')
        if BeautifulSoup(response.content, "html.parser").find('span', attrs={"class":"date"}) is not None:
            time = BeautifulSoup(response.content, "html.parser").find('span', attrs={"class":"date"}).text
        elif BeautifulSoup(response.content, "html.parser").find('span', attrs={"class":"block_timer left txt_666"}) is not None:
            time = BeautifulSoup(response.content, "html.parser").find('span', attrs={"class":"block_timer left txt_666"}).text
        elif BeautifulSoup(response.content, "html.parser").find('span', attrs={"class":"publised-timer"}) is not None:
            time = BeautifulSoup(response.content, "html.parser").find('span', attrs={"class":"publised-timer"}).text
        elif BeautifulSoup(response.content, "html.parser").find('span', attrs={"class":"time left"}) is not None:
            time = BeautifulSoup(response.content, "html.parser").find('span', attrs={"class":"time left"}).text
        elif BeautifulSoup(response.content, "html.parser").find('p', attrs={"class":"published-timer"}) is not None:
            time = BeautifulSoup(response.content, "html.parser").find('p', attrs={"class":"published-timer"}).text
        else:
            time = "Not defined"
        
        if BeautifulSoup(response.content, "html.parser").find('span', attrs={"class":"location-stamp"}) is None:
            location = "Not defined"
        else:
            location = BeautifulSoup(response.content, "html.parser").find('span', attrs={"class":"location-stamp"}).text
        for i in content:
            content_list.append(i.text)

        return ''.join(content_list), time, location


def concat_csv_file(link):
    os.chdir(link)
    all_file_name = [i for i in glob.glob('*.csv')]
    combined_csv = pd.concat([pd.read_csv(i) for i in all_file_name])
    combined_csv = combined_csv.drop('Unnamed: 0', axis=1)
    combined_csv = pd.DataFrame(combined_csv.drop_duplicates())
    return combined_csv


def get_data_from_page(page_link):
    page_response = requests.get(page_link)
    page_content = BeautifulSoup(page_response.content, "html.parser")

    title_name = []
    title_link = []
    paper = []
    tilte_time = []
    tilte_content = []
    location = []
    for i in page_content.find_all('h3'):
        paper.append(i.a['href'].split('/')[2])
        title_name.append(i.text)
        title_link.append(i.a['href'])
        tilte_content.append(read_content(i.a['href'])[0])
        tilte_time.append(read_content(i.a['href'])[1])
        location.append(read_content(i.a['href'])[2])

    vnexpress = {"Paper": paper, 
                    "Title_name": title_name, 
                    "Title_link": title_link, 
                    "Title_content": tilte_content, 
                    "Title_time": tilte_time, 
                    "Location": location}
    df = pd.DataFrame(vnexpress)
    df.to_csv('vnexpress_{number}.csv'.format(number=page_links[-4:]))


def vnexpress_processing(df):
    '''
       1. Split Tiltle_time to get Date of paper -- dd/mm/yyyy
       2. Remove all video new -- no content
       3. Remove all foreign news
       '''
    for i in range(len(df)):
        if len(df['Title_time'][i].split(','))>1:
            df['Title_time'][i] = df['Title_time'][i].split(',')[1]
        else:
            df['Title_time'][i] = df['Title_time'][i].split(',')[0]
    df = df.drop(df.loc[df['Paper']=='video.vnexpress.net'].index)
    df = df.drop(df.loc[df['Location'].isin(['Thái Lan', 'Italy', 'Nga', 'Mexico', 'Hà Lan', 'Đức', 'Argentina', 'Hong Kong', 'Tây Ban Nha',
                                                                                'Trung Quốc', 'Mỹ', 'Pháp', 'Nhật Bản', 'Ấn Độ', 'Anh', 'Australia', 'Colombia', 'Canada',
                                                                                'Brazil', 'Hàn Quốc', 'Nigeria', 'Singapore'])].index)
    return df


def convert_date(date):
    '''
        convert string to date: dd/mm/yyyy
    '''
    date = date.split('/')
    year = int(date[2])
    month = int(date[1])
    day = int(date[0])
    return datetime(year, month, day), pd.Timestamp(datetime(year, month, day)).quarter, year, month

def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist,wordfreq))
