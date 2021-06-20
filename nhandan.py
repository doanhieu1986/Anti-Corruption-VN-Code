from time import time
from bs4 import BeautifulSoup
from numpy.lib import utils
import requests
import os
import glob
import pandas as pd
from datetime import datetime, date, timedelta
import utils


# Function read content from link
def read_content(link):
    content_list = []
    response = requests.get(link)
    soup = BeautifulSoup(response.content, "html.parser")

    content = soup.find_all('p')
    for i in content:
        i = i.text
        for k in (('©2021. Bản quyền thuộc về Báo Nhân Dân', ''),
                  ('Tổng Biên tập: Lê Quốc Minh', ''),
                  ('Phó Tổng Biên tập phụ trách: Đinh Như Hoan', ''),
                  ('Trụ sở Bộ biên tập: 71 Hàng Trống - Hà Nội.', ''),
                  ('Tel: (84) 24 382 54231/382 54232 Fax: (84) 24 382 55593.', ''),
                  ('E-mail: nhandandientu@nhandan.org.vn - nhandandientutiengviet@gmail.com', '')):
            i = i.replace(*k)
        i = i.replace('\n', '')
        content_list.append(i)


    time = soup.find('div', attrs={"class": "box-date pull-left"})
    if time is None:
        time = "Not defined"
    else:
        time = time.text

    location = soup.find('h3', attrs={"class": "dt-news__subtitle"})
    if location is None:
        location = "Not defined"
    else:
        location = location.text.replace('\r\n', '')
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
    soup = BeautifulSoup(response.content, "html.parser")

    paper = []
    title_name = []
    title_link = []
    tilte_content = []
    tilte_time = []
    location = []

    for i in soup.find_all('article'):
        paper.append('nhandan.vn')
        title_name.append(i.a['title'])
        title_link.append(i.a['href'])
        tilte_content.append(read_content('https://nhandan.vn' + i.a['href'])[0])
        tilte_time.append(read_content('https://nhandan.vn' + i.a['href'])[1])
        location.append(read_content('https://nhandan.vn' + i.a['href'])[2])

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
        if is_subset(i, text):
            count += 1
    return count


def nhandan_collection():
    start_date = date(2006, 5, 31)
    end_date = date(2019, 12, 31)
    delta = end_date - start_date
    for i in range(delta.days + 1):
        day = start_date + timedelta(days=i)
        page_date = datetime.strptime(str(day), "%Y-%m-%d").strftime("%d-%m-%Y")
        day = datetime.strptime(str(day), "%Y-%m-%d").strftime("%d/%m/%Y")
        page_link = 'https://nhandan.vn/article/Paging?categoryId=1287&pageIndex=1&pageSize=15&fromDate={k}&toDate={l}&displayView=PagingPartial'.format(k=day, l=day)
        df = get_data_from_page(page_link)
        df.to_csv('C:/Users/admin/Downloads/nhandan/nhandan_{page_date}.csv'.format(page_date=page_date), encoding='utf-8-sig')
        print(page_date)


def location_process(text):
    text = text.strip()
    text = text.replace(':', '')
    return text


def time_process(text):
    if text != 'Not defined':
        text = text.split(',')[1].split('-')[0]
        text = utils.convert_date(text)
    return text


def dantri_all_processing():
    dantri = pd.read_csv('/Users/hieudt/VNU/Thesis/Dantri/dantri_collection.csv')
    dantri['Location'] = dantri.apply(lambda row: location_process(row['Location']), axis=1)
    dantri['Month'] = dantri.apply(lambda row: time_process(row['Title_time'])[3], axis=1)
    dantri['Quarter'] = dantri.apply(lambda row: time_process(row['Title_time'])[1], axis=1)
    dantri['Year'] = dantri.apply(lambda row: time_process(row['Title_time'])[2], axis=1)
    dantri = dantri.drop(dantri[dantri['Year'] == 2021].index, axis=0)
    dantri.to_csv('/Users/hieudt/VNU/Thesis/Thesis-Data_Science-main/dantri_all_processing.csv', index=False,
                  encoding='utf-8-sig')


def dantri_result():
    list_of_group_words = utils.word_combination('word_combination.xlsx')
    data = pd.read_csv('dantri_all_processing.csv')
    data['based_index'] = data.apply(lambda row: utils.base_index(list_of_group_words, row['Title_content']), axis=1)
    data = data[data['based_index'] > 0]
    data.to_excel('dantri_result.xlsx', index=False, encoding='utf-8-sig')

# link = 'https://nhandan.vn/article/Paging?categoryId=1287&pageIndex=1&pageSize=15&fromDate=07/06/2020&toDate=08/06/2020&displayView=PagingPartial'
# link1 = 'https://nhandan.vn' + get_data_from_page(link)['Title_link'][1]
# print(get_data_from_page(link)['Title_time'])
nhandan_collection()
