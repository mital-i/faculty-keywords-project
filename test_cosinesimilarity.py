import pandas as pd
import sent2vec
from nltk import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from scipy.spatial import distance

model_path = "/Users/mitalimittal/Downloads"
model = sent2vec.Sent2vecModel()
try:
    model.load_model(model_path)
except Exception as e:
    print(e)
print('model successfully loaded')


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

#make professors dictionary
for i in range(df.shape[0]): 
    keywords = make_keywords_list(df, i)
    professor_name = df.iloc[i].tolist()[0]
    professors[professor_name] = keywords

