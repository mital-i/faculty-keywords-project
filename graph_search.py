import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import networkx as nx
import matplotlib.pyplot as plt
full_name = 'Allison, Steven'
full_name2 = 'Arora, Kavita'
keywords1 = 'soil microbiome; carbon cycling; microbial ecology; mathematical modeling; decomposition; extracellular enzymes; ecosystem science; global change; climate change; drought; environmental justice; biodiversity; photosynthesis; renewable energy; community engagement; sustainable agriculture; urbanization; social equity; atmospheric pollution; water scarcity; public health; conservation efforts'.split(';')
keywords2 = 'model organisms; developmental biology; genetics; TGF-ß signaling; metabolism; laboratory mice; embryogenesis; heredity; cell division; energy expenditure; fruit flies; morphogenesis; inheritance patterns; growth factors; biochemical pathways; zebrafish; genetic traits; insulin sensitivity; enzyme kinetics'.split(';')
print(keywords1)


#process excel file, make dataframe of all the professors and keywords instead of using a dictionary
df = pd.read_excel("/Users/mitalimittal/Documents/GitHub/faculty-keywords-project/Research keywords with word clouds.xlsx") #open excel spreadsheet

profs = {
}

word_graph = {
    
}

for i in range(df.shape[0]): 
    row_values = df.iloc[i].tolist()
    print(row_values)
    full_name = row_values[0]
    row_values = row_values[7].split("; ")
    for i in range(len(row_values)): 
        if len(row_values[i].split())>1: 
            temp = row_values[i].split()
            temp = temp[0]+"_"+temp[1]
            row_values[i]=temp
    profs[full_name] = row_values
print(profs)

dframe = pd.DataFrame(profs)

def run_clustering(df): 
    vectorizer = TfidfVectorizer()

    X = vectorizer.fit_transform()

    #create a kmeans clustering model

    kmeans = KMeans(n_clusters=10)
    kmeans.fit(X)

    labels = kmeans.predict(X)

    print(labels)
    cluster_labels = {}

    for i in range(10): 
        cluster_labels[i] = []

    for i in range(len(labels)): 
        cluster_labels[labels[i]].append(keywords1[i])

    print(cluster_labels)