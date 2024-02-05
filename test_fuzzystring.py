import pandas as pd
from thefuzz import fuzz
import math

#open excel spreadsheet
df = pd.read_excel("Research keywords - 2024.01.10.xlsx")

#convert keywords in each row into a list
def make_keywords_list(df, row_index): 
    row_values = df.iloc[row_index].tolist()
    row_values = row_values[6].split("; ")
    return row_values

professors = {}

for i in range(df.shape[0]): 
    keywords = make_keywords_list(df, i)
    professor_name = df.iloc[i].tolist()[0]
    professors[professor_name] = keywords

name = "Kurtis Pykes"
full_name = "Kurtis K D Pykes"

word1 = "Down Syndrome"
word2 = "Dementia"

key1 = ['microbes', 'soil', 'climate change', 'fungi', 'biogeochemistry', 'ecosystem', 'ecology', 'science communication', 'science policy']
key2 = ['human microbiome', 'metabolomics', 'next generation sequencing', 'microbial ecology', 'clinical microbiology', 'phage therapy', 'virome', 'cystic fibrosis', 'wastewater surveillance', 'Alzheimers Disease', 'dietary intervention', 'fiber', 'health', 'cancer treatment', 'microbiome', 'biomarkers', 'diagnostics', 'longitudinal studies', 'random forest', 'team science', 'clinical translational science', 'preterm birth', 'anaerobic cultivation', 'bioinformatics consulting', 'volatiles', 'breath', 'gas chromatography mass spec']

print(f"Similarity score: {fuzz.ratio(key1[0], key2[0])}")

def find_similarity_score(keywords1, keywords2): 
    ratio = 1
    curr_ratio = 1
    num_words = len(keywords1) * len(keywords2)
    print(num_words)
    for i in keywords1: 
        for j in keywords2: 
            if (i!=j):
                if (fuzz.ratio(i, j)!=0): 
                    ratio *= fuzz.ratio(i, j)
                    ratio = math.sqrt(ratio)
                    print(ratio, i, j)
    return ratio


print(find_similarity_score(key1, key2))
