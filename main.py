# -*- coding: utf-8 -*-
import pandas as pd
import spacy
import en_core_web_sm

#api key: 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

nlp = spacy.load("en_core_web_sm")
nlp = en_core_web_sm.load()

#open excel spreadsheet
df = pd.read_excel("Research keywords - 2024.01.10.xlsx")

#convert keywords in each row into a list
def make_keywords_list(df, row_index): 
    row_values = df.iloc[row_index].tolist()
    row_values = row_values[6].split("; ")
    return row_values

# Display the values
##print(f"Values in row {row_index + 1}: {row_values}")
num_rows = df.shape[0]
#print(num_rows)
#print(make_keywords_list(df, 2))
keywords1 = make_keywords_list(df, 6)
keywords2 = make_keywords_list(df, 25)
print(keywords1)
print()
print(keywords2)

