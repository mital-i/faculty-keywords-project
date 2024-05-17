import pandas as pd
from gensim.models import KeyedVectors
from gensim.test.utils import datapath
import numpy as np
from numpy.linalg import norm
import heapq

wv_from_bin = KeyedVectors.load_word2vec_format(datapath('/Users/mitalimittal/keyword_matching/GoogleNews-vectors-negative300.bin'), binary=True)

vector1 = wv_from_bin['Alzheimers']

#cosine = np.dot(vector1, vector2)/ (norm(vector1, axis=1)*norm(vector2))
#print(cosine) 

df = pd.read_excel("Research keywords with word clouds.xlsx") #open excel spreadsheet

#convert keywords in each row into a list
def make_keywords_list(df, row_index): 
    row_values = df.iloc[row_index].tolist()
    print(row_values)
    row_values = row_values[7].split("; ")
    for i in range(len(row_values)): 
        if len(row_values[i].split())>1: 
            temp = row_values[i].split()
            temp = temp[0]+"_"+temp[1]
            row_values[i]=temp
    return row_values

def find_similarity_score(keywords1, keywords2): 
    score_heap = []
    heapq.heapify(score_heap)
    for i in range(len(keywords1)): 
        for j in range(len(keywords2)): 
            if (keywords1[i]!=keywords2[j]) and (keywords1[i] in wv_from_bin.key_to_index) and (keywords2[j] in wv_from_bin.key_to_index):
                vector1 = wv_from_bin[list(keywords1[i].split())[0]]
                print(vector1)
                vector2 = wv_from_bin[list(keywords2[j].split())[0]]
                heapq.heappush(score_heap, np.dot(vector1, vector2)/ (norm(vector1)*norm(vector2)))

    return heapq.nlargest(10, list(score_heap))

#professors is a dictionary, key: the professor's full name, value: the keywords associated with that professor
professors = {}

#make professors dictionary
for i in range(df.shape[0]): 
    keywords = make_keywords_list(df, i)
    professor_name = df.iloc[i].tolist()[0]
    professors[professor_name] = keywords

full_name = 'Allison, Steven'
keywords1 = make_keywords_list(df, 0)

for prof2, keywords2 in professors.items(): 
    curr_ratio = find_similarity_score(keywords1, keywords2)
    if (sum(curr_ratio)/10) >= 0.45 and full_name!=prof2: 
        print(f"{full_name} would work well with {prof2}: {sum(curr_ratio)/10}")
