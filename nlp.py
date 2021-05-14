from vncorenlp import VnCoreNLP
import pandas as pd


def tokenize(text):
    rdrsegmenter = VnCoreNLP('D:/VNU/Thesis/Thesis - Python/vncorenlp/VnCoreNLP-1.1.1.jar', annotators="wseg", max_heap_size='-Xmx500m')
    word_segmented_text = rdrsegmenter.tokenize(text)
    return word_segmented_text


def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist,wordfreq))


text = '\nThu sang Tôn Ngộ Không phò Đường Tăng đi thỉnh kinh tại Tây Trúc..,., Tội danh tham nhũng được Viện kiểm sát khẳng định.'

print(tokenize(text))

# test = pd.read_csv('D:/VNU/Thesis/Thesis - Python/vnexpress_all_processing.csv')
# text = test['Title_content'][0]
