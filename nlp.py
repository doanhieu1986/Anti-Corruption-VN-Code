from vncorenlp import VnCoreNLP
import pandas as pd
from collections import Counter


def tokenize(text):
    rdrsegmenter = VnCoreNLP('D:/VNU/Thesis/Thesis - Python/vncorenlp/VnCoreNLP-1.1.1.jar', annotators="wseg", max_heap_size='-Xmx500m')
    word_segmented_text = rdrsegmenter.tokenize(text)
    return word_segmented_text


def remove_character (text):
    '''
    text: text need to remove characters
    characters: list of removed characters 
        '''
    remove_list_character = ['!','@','#','$','%','^','&','*','(',')','<','>','?',':','"','[',']','{','}','=','...','…','\xa0']
    for i in remove_list_character:
        text = text.replace(i,'')
    return text


def word_freq(sentence):
    word_freq = [sentence.count(p) for p in sentence]
    return dict(zip(sentence,word_freq))


def dict_of_words(text):
    text_tokenize = tokenize(text)
    dict_all = {}
    for i in text_tokenize:
        freq = word_freq(i)
        dict_all = Counter(dict_all) + Counter(freq)
    return dict_all