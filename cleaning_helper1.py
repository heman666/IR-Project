import pandas as pd
import numpy as np
import string
import re
import nltk
from nltk.corpus import stopwords
from textblob import Word
nltk_stopwords = stopwords.words('english')

def clean_column(dataframe, column_to_clean, new_col):
    df_copy = dataframe.copy()
    df_copy['copied_column'] = df_copy[column_to_clean]
    df_copy['copied_column'] = df_copy['copied_column'].str.lower()
    cleaned_column = []
    for label in df_copy.index:
        row = df_copy.loc[label, :]['copied_column']
        clean = [x for x in row.split() if x not in string.punctuation]
        clean = [x for x in clean if x not in nltk_stopwords]
        clean = [x for x in clean if len(x) != 1]
        clean1 = []
        for each in clean:
            temp = purify(each)
            if len(temp) > 1:
                if(temp[len(temp) - 1] == '.'):
                    temp = temp[:-1]
                clean1.append(temp)
        clean1 = " ".join(clean1)
        clean1 = clean1.strip()
        if '.' in clean1:
            print(clean1)
        cleaned_column.append(clean1)
    df_copy[new_col] = cleaned_column
    del df_copy['copied_column']
    return df_copy

def purify(word):
    word = word.lower()
    new_word_2 = ""
    if '-' in word:
        new_word_1 = word.split('-')
        for i in new_word_1:
            new_word_2 = new_word_2 + i + " "
        return new_word_2[:-1]
    word = re.sub('[^A-Za-z0-9.]',' ',word)
    if len(str(word.strip())) <= 1:
        return "a"
    word = Word(word.strip().split()[0]).lemmatize()
    return word