import networkx
import matplotlib.pyplot as plt

G = networkx.Graph()

G.add_edge("Alzheimer's", "Dementia")
print(G.nodes())
print(G)