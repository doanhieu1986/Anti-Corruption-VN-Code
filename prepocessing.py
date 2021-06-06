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

def add_dict_column():
    df = pd.read_csv('/Users/hieudt/VNU/Thesis/Thesis-Data_Science-main/vnexpress_all_processing.csv')
    df = df.drop(26804, axis=0)
    df['Dict'] = df.apply(lambda row: nlp.dict_of_words(row['Title_content']), axis=1)
    df.to_csv('/Users/hieudt/VNU/Thesis/Thesis-Data_Science-main/data.csv',index=False, encoding='utf-8-sig')
