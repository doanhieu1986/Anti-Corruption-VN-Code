from time import time
from bs4 import BeautifulSoup
from numpy.lib import utils
from pandas.core.reshape.concat import concat
import requests
import os
import glob
import pandas as pd
from datetime import datetime
import utils


# Function read content from link
def read_content(link):
    content_list = []
    response = requests.get(link)   
    bts = BeautifulSoup(response.content, "html.parser")
    
    content = bts.find_all('p')
    for i in content:
        content_list.append(i.text)
    
    time = bts.find('span', attrs= {"class":"dt-news__time"})
    if time is None:
        time = "Not defined"
    else:
        time = time.text
    
    location = bts.find('h3', attrs={"class":"dt-news__subtitle"})
    if location is None:
        location = "Not defined"
    else:
        location = location.text.replace('\r\n','')
    return ' '.join(content_list), time, location


def concat_csv_file(link):
    os.chdir(link)
    all_file_name = [i for i in glob.glob('*.csv')]
    combined_csv = pd.concat([pd.read_csv(i) for i in all_file_name])
    combined_csv = combined_csv.drop('Unnamed: 0', axis=1)
    combined_csv = pd.DataFrame(combined_csv.drop_duplicates())
    return combined_csv


def get_data_from_page(page_link):
    response = requests.get(page_link)
    bts = BeautifulSoup(response.content, "html.parser")

    paper = []
    title_name = []
    title_link = []
    tilte_content = []
    tilte_time = []
    location = []

    for i in bts.find_all('h3', attrs={"class":"news-item__title"}):
        paper.append('dantri.com.vn')
        title_name.append(i.a['title'])
        title_link.append(i.a['href'])
        tilte_content.append(read_content('https://dantri.com.vn'+i.a['href'])[0])
        tilte_time.append(read_content('https://dantri.com.vn'+i.a['href'])[1])
        location.append(read_content('https://dantri.com.vn'+i.a['href'])[2])

    dantri = { 
                "Paper": paper, 
                "Title_name": title_name, 
                "Title_link": title_link, 
                "Title_content": tilte_content, 
                "Title_time": tilte_time, 
                "Location": location
                    }
    return pd.DataFrame(dantri)


def convert_date(date):
    '''
        convert string to date: dd/mm/yyyy
    '''
    date = date.split('/')
    year = int(date[2])
    month = int(date[1])
    day = int(date[0])
    return datetime(year, month, day), pd.Timestamp(datetime(year, month, day)).quarter, year, month


def base_index(list_of_group_words, text):
    count = 0
    for i in list_of_group_words:
        if is_subset(i,text):
            count +=1
    return count


def dantri_collection():
    start_date = date(2006,3,30)
    end_date = date(2019,12,31)
    delta = end_date - start_date
    for i in range(delta.days + 1):
        day = start_date + timedelta(days=i)
        day = datetime.strptime(str(day), "%Y-%m-%d").strftime("%d-%m-%Y")
        page_link = 'https://dantri.com.vn/phap-luat/{page_date}.htm'.format(page_date = day)
        df = dantri.get_data_from_page(page_link)
        df.to_csv('/Users/hieudt/VNU/Thesis/Dantri/dantri_{page_date}.csv'.format(page_date=day))
        print(page_link)


def location_process(text):
    text = text.strip()
    text = text.replace(':','')
    return text


def time_process(text):
    if text != 'Not defined':
        text = text.split(',')[1].split('-')[0]
        text = utils.convert_date(text)
    return text

def dantri_all_processing ():
    dantri = pd.read_csv('/Users/hieudt/VNU/Thesis/Dantri/dantri_collection.csv')
    dantri['Location'] = dantri.apply(lambda row: location_process(row['Location']), axis=1)
    dantri['Month'] = dantri.apply(lambda row: time_process(row['Title_time'])[3], axis=1)
    dantri['Quarter'] = dantri.apply(lambda row: time_process(row['Title_time'])[1], axis=1)
    dantri['Year'] = dantri.apply(lambda row: time_process(row['Title_time'])[2], axis=1)
    dantri = dantri.drop(dantri[dantri['Year'] == 2021].index, axis=0)
    dantri.to_csv('/Users/hieudt/VNU/Thesis/Thesis-Data_Science-main/dantri_all_processing.csv',index=False, encoding='utf-8-sig')

def dantri_result():
    list_of_group_words = utils.word_combination('word_combination.xlsx')
    data = pd.read_csv('dantri_all_processing.csv')
    data['based_index'] = data.apply(lambda row: utils.base_index(list_of_group_words,row['Title_content']),axis=1)
    data = data[data['based_index']>0]
    data.to_excel('dantri_result.xlsx',index=False, encoding='utf-8-sig')

