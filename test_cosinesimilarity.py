import pandas as pd
import gensim
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from gensim.test.utils import datapath
import numpy as np
from numpy.linalg import norm

wv_from_bin = KeyedVectors.load_word2vec_format(datapath(
    '/Users/mitalimittal/keyword_matching/GoogleNews-vectors-negative300.bin'), binary=True)

#result = wv_from_bin.doesnt_match("breakfast cereal puppy lunch".split())
vector1 = wv_from_bin['Alzheimers']


#cosine for Alzheimers and Dementia: 0.6454646
#cosine for Alzheimers and Dog: 0.17926827
#cosine for Alzheimers and Memory: 0.31218246
#cosine for Alzheimers and Alzheimers: 1.0


print(vector1)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(vector2)

cosine = np.dot(vector1, vector2)/ (norm(vector1)*norm(vector2))
print(cosine)

df = pd.read_excel("Research keywords - 2024.01.10.xlsx") #open excel spreadsheet

#convert keywords in each row into a list
def make_keywords_list(df, row_index): 
    row_values = df.iloc[row_index].tolist()
    row_values = row_values[6].split("; ")
    return row_values

#professors is a dictionary 
#key: the professor's full name
#value: the keywords associated with that professor
professors = {}
keyword_arr = []

#make professors dictionary
for i in range(df.shape[0]): 
    keywords = make_keywords_list(df, i)
    professor_name = df.iloc[i].tolist()[0]
    professors[professor_name] = keywords
    keyword_arr.append(keywords)

prof1 = 'Yassa, Michael'
keywords1 = professors[prof1]
