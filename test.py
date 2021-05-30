from abc import get_cache_token
from collections import Counter
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import utils
import nlp

df = pd.read_csv('/Users/hieudt/VNU/Thesis/Thesis-Data_Science-main/vnexpress_all_processing.csv')
count_chunk = 7
for i in range(700,len(df), 100):
    test = df.iloc[i:i+100]
    count_chunk +=1
    test['Dict'] = test.apply(lambda row: nlp.dict_of_words(row['Title_content']), axis=1)
    test.to_csv('/Users/hieudt/VNU/Thesis/Thesis-Data_Science-main/vnexpress_processing_chunk_{stt}.csv'.format(stt = count_chunk),index=False, encoding='utf-8-sig')


# count_chunk = 4
# for i in test:
#     count_chunk +=1
#     i['Dict'] = i.apply(lambda row: nlp.dict_of_words(row['Title_content']), axis=1)
#     i.to_csv('/Users/hieudt/VNU/Thesis/Thesis-Data_Science-main/vnexpress_processing_chunk_{stt}.csv'.format(stt = count_chunk),index=False, encoding='utf-8-sig')
#     del i
#     gc.collect()




# test['Dict'] = test.apply(lambda row: nlp.dict_of_words(row['Title_content']), axis=1)
# test.to_csv('/Users/hieudt/VNU/Thesis/Thesis-Data_Science-main/vnexpress_all_processing_test_all.csv',index=False, encoding='utf-8-sig')

# x = pd.read_csv('/Users/hieudt/VNU/Thesis/Thesis-Data_Science-main/vnexpress_processing_chunk_5.csv')
# # x['Check'] = x.apply(lambda row: nlp.check_subset(ast.literal_eval(row['Dict']),[['CHỨNG_CỨ','KHÁM_NGHIỆM'],['VKSND'],['CÔNG_AN']]), axis=1)
# print(x)
# g = pd.read_csv('/Users/hieudt/VNU/Thesis/Thesis-Data_Science-main/vnexpress_all_processing.csv')[400:500]
# print(g)
# # y = x['Dict'][0]
# # # # y = ast.literal_eval(y)
# # y = nlp.check_subset(ast.literal_eval(y), [['CHỨNG_CỨ','KHÁM_NGHIỆM'],['VKSND']])
# # print(y)
