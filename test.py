import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import utils

test = pd.read_csv('D:/VNU/Thesis/Thesis - Python/vnexpress_all_processing.csv')
print(test)


# for i in range(52735):
#     print(i)
#     test['Title_time'][i] = convert_date(test['Title_time'][i])
#     print(test['Title_time'][i])

# print(test['Title_link'][30937])

# response = requests.get('https://vnexpress.net/thanh-nien-bi-dam-chet-vi-khong-bo-tien-cho-nu-tiep-vien-karaoke-3946324.html')
# content = BeautifulSoup(response.content, "html.parser").find_all('p', attrs={"class":"Normal"})
# time = BeautifulSoup(response.content, "html.parser").find_all('span', attrs={"class":"date"})[0].text
# location = BeautifulSoup(response.content, "html.parser").find('span', attrs={"class":"location-stamp"})
# print(time, location)

# print(utils.read_content('https://vnexpress.net/thanh-nien-bi-dam-chet-vi-khong-bo-tien-cho-nu-tiep-vien-karaoke-3946324.html'))