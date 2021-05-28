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

test = pd.read_csv('/Users/hieudt/VNU/Thesis/Thesis-Data_Science-main/vnexpress_all_processing.csv')[:100]
test['Dict'] = test.apply(lambda row: nlp.dict_of_words(row['Title_content']), axis=1)
test.to_csv('/Users/hieudt/VNU/Thesis/Thesis-Data_Science-main/vnexpress_all_processing_test.csv',index=False, encoding='utf-8-sig')
