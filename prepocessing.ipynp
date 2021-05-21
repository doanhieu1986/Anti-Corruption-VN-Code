import utils
import pandas as pd
import numpy as np
import nlp


# all_file_name = [i for i in glob.glob('*.csv')]
# combined_csv = pd.concat([pd.read_csv(i) for i in all_file_name])
# combined_csv = combined_csv.drop('Unnamed: 0', axis=1)
# vnexpress_all = pd.DataFrame(combined_csv.drop_duplicates())
# vnexpress_all.to_csv('vnexpress_all.csv',index=False, encoding='utf-8-sig')


# concat vnexpress raw file -- Run one time to create file
# vnexpress_all = utils.concat_csv_file('D:/VNU/Thesis/Data/Vnexpress')
# vnexpress_all.to_csv('D:/VNU/Thesis/Thesis - Python/vnexpress_all_raw.csv',index=False, encoding='utf-8-sig')


#processing vnexpress file -- Run one time to create file
# vnexpress_all_processing = utils.vnexpress_processing(pd.read_csv('D:/VNU/Thesis/Thesis - Python/vnexpress_all_raw.csv'))
# vnexpress_all_processing.to_csv('D:/VNU/Thesis/Thesis - Python/vnexpress_all_processing.csv',index=False, encoding='utf-8-sig')


# Check null value
k=500
n=600
df = pd.read_csv('D:/VNU/Thesis/Thesis - Python/vnexpress_all_processing.csv')[k:n]
# print(df)


# Add period column to DataFrame
# df['Month'] = ''
# df['Quarter']= ''
# df['Year']= ''
df['Dict'] = ''
for i in range(k,n):
    # df['Month'][i] = utils.convert_date(df['Title_time'][i])[3]
    # df['Quarter'][i] = utils.convert_date(df['Title_time'][i])[1]
    # df['Year'][i] = utils.convert_date(df['Title_time'][i])[2]
    text = df['Title_content'][i]
    text = nlp.remove_character(text)
    df['Dict'][i] =nlp.dict_of_words(text)
    # print(nlp.dict_of_words(text))
    # print(text)
df.to_csv('D:/VNU/Thesis/Thesis - Python/vnexpress_all_processing_{x}.csv'.format(x=k),index=False, encoding='utf-8-sig')
# print(df)