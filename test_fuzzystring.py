import pandas as pd
from thefuzz import fuzz
import heapq

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

def find_similarity_score(keywords1, keywords2): 
    ratio = []
    heapq.heapify(ratio)
    #num_words = len(keywords1) * len(keywords2)
    for i in keywords1: 
        for j in keywords2: 
            if (i!=j):
                if (fuzz.ratio(i, j)>=30): 
                    heapq.heappush(ratio, fuzz.ratio(i, j))

    return list(ratio)

print("Enter your last name: ")
full_name = input()
print("Enter your first name: ")
full_name += ", " + input()
print(full_name)

keywords1 = professors[full_name]
prof2 = "LaFerla, Frank"
keywords2 = professors[prof2]
nump= 0


for prof2, keywords2 in professors.items(): 
    curr_ratio = find_similarity_score(keywords1, keywords2)
    t_ten = heapq.nlargest(10, curr_ratio)
    if (sum(t_ten)/10) >= 48 and full_name!=prof2: 
        print(f"{full_name} would work well with {prof2}: {sum(t_ten)/10}")
        nump+=1


print(f"Total number of possible collaborators: {nump}")