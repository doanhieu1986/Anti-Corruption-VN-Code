import pandas as pd
import nlp
import utils


list_of_group_words = utils.word_combination('word_combination.xlsx')
data = pd.read_csv('vnexpress_all_processing.csv')
data['based_index'] = data.apply(lambda row: utils.base_index(list_of_group_words,row['Title_content']),axis=1)
data = data[data['based_index']>0]
data.to_excel('vnexpress_result.xlsx')


# print(utils.base_index(list_of_group_words,text))

# test['Dict'] = test.apply(lambda row: nlp.dict_of_words(row['Title_content']), axis=1)
# test.to_csv('/Users/hieudt/VNU/Thesis/Thesis-Data_Science-main/vnexpress_all_processing_test_all.csv',index=False, encoding='utf-8-sig')


# y = x['Dict'][0]
# # # y = ast.literal_eval(y)
# y = nlp.check_subset(ast.literal_eval(y), [['CHỨNG_CỨ','KHÁM_NGHIỆM'],['VKSND']])
# print(y)
