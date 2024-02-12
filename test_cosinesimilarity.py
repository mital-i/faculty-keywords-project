import pandas as pd
from gensim.models import Word2Vec
from collections import defaultdict
import spacy
import logging


df = pd.read_excel("Research keywords - 2024.01.10.xlsx") #open excel spreadsheet

model_name = "BioWordVec_PubMed_MIMICIII_d200.vec.bin"
model = Word2Vec.load("/Users/mitalimittal/Downloads/BioWordVec_PubMed_MIMICIII_d200.vec.bin")

#convert keywords in each row into a list
def make_keywords_list(df, row_index): 
    row_values = df.iloc[row_index].tolist()
    row_values = row_values[6].split("; ")
    return row_values

#professors is a dictionary 
#key: the professor's full name
#value: the keywords associated with that professor
professors = {}

#make professors dictionary
for i in range(df.shape[0]): 
    keywords = make_keywords_list(df, i)
    professor_name = df.iloc[i].tolist()[0]
    professors[professor_name] = keywords

prof1 = 'Yassa, Michael'
keywords1 = professors[prof1]
