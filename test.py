from abc import get_cache_token
from collections import Counter
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import utils
import nlp

test = pd.read_csv('D:/VNU/Thesis/Thesis - Python/vnexpress_all_processing.csv')
# print(test)

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


def remove_character (text):
    '''
    text: text need to remove characters
    characters: list of removed characters 
        '''
    remove_list_character = ['!','@','#','$','%','^','&','*','(',')','<','>','?',':','"','[',']','{','}','=','...','…','\xa0']
    for i in remove_list_character:
        text = text.replace(i,' ')
    return text


text = test['Title_content'][1000]
text = remove_character(text)
# text_tokenize = nlp.tokenize(text)


def dict_of_words(text):
    text_tokenize = nlp.tokenize(text)
    dict_all = {}
    for i in text_tokenize:
        word_freq = nlp.word_freq(i)
        dict_all = Counter(dict_all) + Counter(word_freq)
    return dict_all

print(dict_of_words(text))




# dict_all = {}
# dict_0 = nlp.word_feq(text_tokenize[0])
# dict_1 = nlp.word_feq(text_tokenize[1])
# dict_2 = nlp.word_feq(text_tokenize[2])
# # dict_all = dict(list(dict_0.items()) + list(dict_1.items()) + list(dict_2.items()))

# from collections import Counter
# dict_all = Counter(dict_0) + Counter(dict_1) + Counter(dict_2)
# print(dict_all.items())

# print(remove_character(text))