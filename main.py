# -*- coding: utf-8 -*-
import pandas as pd
import spacy
import en_core_web_sm

nlp = spacy.load("en_core_web_sm")
nlp = en_core_web_sm.load()

df = pd.read_excel("Research keywords - 2024.01.10.xlsx")

def find_similarity(keywords1, keywords2): 
    return 0;


def make_keywords_list(df, row_index): 
    row_values = df.iloc[row_index].tolist()
    row_values = row_values[6].split("; ")
    doc = nlp(row_values)
    keywords_object = set(token.text.lower() for token in docz if not token.is_stop and token.is_alpha)

# Display the values
##print(f"Values in row {row_index + 1}: {row_values}")
num_rows = df.shape[0]
#print(num_rows)
#print(make_keywords_list(df, 2))
keywords1 = make_keywords_list(df, 6)
keywords2 = make_keywords_list(df, 31)
print(len(keywords1 | keywords2))
print(len(keywords1 & keywords2))

