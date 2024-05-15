import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import networkx as nx
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from collections import Counter
full_name = 'Allison, Steven'
full_name2 = 'Arora, Kavita'
keywords1 = 'soil microbiome; carbon cycling; microbial ecology; mathematical modeling; decomposition; extracellular enzymes; ecosystem science; global change; climate change; drought; environmental justice; biodiversity; photosynthesis; renewable energy; community engagement; sustainable agriculture; urbanization; social equity; atmospheric pollution; water scarcity; public health; conservation efforts'.split(';')
keywords2 = 'model organisms; developmental biology; genetics; TGF-ß signaling; metabolism; laboratory mice; embryogenesis; heredity; cell division; energy expenditure; fruit flies; morphogenesis; inheritance patterns; growth factors; biochemical pathways; zebrafish; genetic traits; insulin sensitivity; enzyme kinetics'.split(';')
print(keywords1)


#process excel file, make dataframe of all the professors and keywords instead of using a dictionary
df = pd.read_excel("/Users/mitalimittal/Documents/GitHub/faculty-keywords-project/Research keywords with word clouds.xlsx") #open excel spreadsheet

profs = {}

word_graph = {}

#create dictionary of professors and keywords

for i in range(4): #replace parameter with df.shape[0]
    row_values = df.iloc[i].tolist()
    #print(row_values)
    full_name = row_values[0]
    row_values = row_values[7].split("; ")
    for i in range(len(row_values)): 
        if len(row_values[i].split())>1: 
            temp = row_values[i].split()
            temp = temp[0]+"_"+temp[1]
            row_values[i]=temp
    profs[full_name] = row_values


#print(profs)

#create a document-term matrix (DTM)
#professor_data = profs
dtm = []
for name, keywords in profs.items(): 
    doc_vect = {}
    for word in keywords: 
        doc_vect[word] = doc_vect.get(word, 0) + 1

    dtm.append(doc_vect)


def run_clustering(): 
    scaler = StandardScaler()
    dtm_scaled = scaler.fit_transform(dtm)  # Normalize DTM

    pca = PCA(n_components=12)  # Adjust the number of components as needed
    pca_data = pca.fit_transform(dtm_scaled)

    # Clustering
    kmeans = KMeans(n_clusters=12)  # Adjust the number of clusters as needed
    kmeans.fit(pca_data)

    # Assign clusters to professors (replace data with your actual data structure)
    for i, keywords in enumerate(profs):
        cluster = kmeans.predict([pca_data[i]])[0]
        print(f"Professor {i+1}: Research area keywords - {keywords}, Cluster - {cluster}")

run_clustering()