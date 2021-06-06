from vncorenlp import VnCoreNLP
import pandas as pd
from collections import Counter


rdrsegmenter = VnCoreNLP('/Users/hieudt/VNU/Thesis/Thesis-Data_Science-main/vncorenlp/VnCoreNLP-1.1.1.jar', annotators="wseg", max_heap_size='-Xmx500m')

def tokenize(text):
    word_segmented_text = rdrsegmenter.tokenize(text)
    return word_segmented_text


def remove_character (text):
    '''
    text: text need to remove characters
    characters: list of removed characters 
        '''
    remove_list_character = ['!','@','#','$','%','^','&','*','(',')','<','>','?',':','"','[',']','{','}','=','...','…','\xa0',',','\n']
    for i in remove_list_character:
        text = text.replace(i,'')
    return text


def uppercase_for_dict_keys(lower_dict):
    upper_dict = {}
    for k, v in lower_dict.items():
        if isinstance(v, dict):
            v = _uppercase_for_dict_keys(v)
        upper_dict[k.upper()] = v
    return upper_dict


def word_freq(sentence):
    word_freq = [sentence.count(p) for p in sentence]
    return dict(zip(sentence,word_freq))


def dict_of_words(text):
    text = remove_character(text)
    text_tokenize = tokenize(text)
    dict_all = {}
    for i in text_tokenize:
        freq = word_freq(i)
        dict_all = Counter(dict_all) + Counter(freq)
        dict_all = uppercase_for_dict_keys(dict_all)
    return dict(dict_all)


def check_subset(dict_of_word, list_of_word):
    '''
    dict_of_word: the dict of word
    list_of_word: the list of the sub-list of word need to be checked if it is subset of set or not
    '''
    dict_of_word = dict_of_word.keys()
    count = 0
    for i in list_of_word:
        if set(i).issubset(dict_of_word)==True:
            count +=1
    return count
