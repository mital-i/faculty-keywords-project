import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
full_name = 'Allison, Steven'
full_name2 = 'Arora, Kavita'
keywords1 = 'soil microbiome; carbon cycling; microbial ecology; mathematical modeling; decomposition; extracellular enzymes; ecosystem science; global change; climate change; drought; environmental justice; biodiversity; photosynthesis; renewable energy; community engagement; sustainable agriculture; urbanization; social equity; atmospheric pollution; water scarcity; public health; conservation efforts'.split(';')
keywords2 = 'model organisms; developmental biology; genetics; TGF-ß signaling; metabolism; laboratory mice; embryogenesis; heredity; cell division; energy expenditure; fruit flies; morphogenesis; inheritance patterns; growth factors; biochemical pathways; zebrafish; genetic traits; insulin sensitivity; enzyme kinetics'.split(';')
print(keywords1)

df = pd.DataFrame({
    full_name: keywords1
})

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(df[full_name])

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