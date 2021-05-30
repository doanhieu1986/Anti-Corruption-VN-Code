from abc import get_cache_token
from collections import Counter
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import utils
import nlp

# test = pd.read_csv('D:/VNU/Thesis/Thesis - Python/vnexpress_all_processing.csv')
# print(test)

# test = pd.read_csv('/Users/hieudt/VNU/Thesis/Thesis-Data_Science-main/vnexpress_all_processing.csv',chunksize=100)
# count_chunk = 0
# for i in test:
#     count_chunk +=1
#     i['Dict'] = i.apply(lambda row: nlp.dict_of_words(row['Title_content']), axis=1)
#     i.to_csv('/Users/hieudt/VNU/Thesis/Thesis-Data_Science-main/vnexpress_processing_chunk_{stt}.csv'.format(stt = count_chunk),index=False, encoding='utf-8-sig')




# test['Dict'] = test.apply(lambda row: nlp.dict_of_words(row['Title_content']), axis=1)
# test.to_csv('/Users/hieudt/VNU/Thesis/Thesis-Data_Science-main/vnexpress_all_processing_test_all.csv',index=False, encoding='utf-8-sig')

x = pd.read_csv('/Users/hieudt/VNU/Thesis/Thesis-Data_Science-main/vnexpress_processing_chunk_4.csv')
print(x)

y = x['Dict'][0]
y = ast.literal_eval(y)
# y = nlp.uppercase_for_dict_keys(y)
print(y)
