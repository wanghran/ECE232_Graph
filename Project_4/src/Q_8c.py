import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt

with open('../output/8c.txt', 'r') as f:
    data = f.readlines()

actors = []
movies = []
labels = []
for line in data:
    a_name = line.split('\t')[0]
    m_title = line.split('\t')[1]
    actors.append(a_name)
    labels.append(a_name)
    movies.append(m_title)

B = nx.Graph()
# Add nodes with the node attribute "bipartite"
B.add_nodes_from(actors, bipartite=0)
B.add_nodes_from(movies, bipartite=1)

edges = []
for line in data:
    a_name = line.split('\t')[0]
    m_title = line.split('\t')[1]
    labels.append(m_title)

    edges.append((a_name, m_title))

B.add_edges_from(edges)

X, Y = bipartite.sets(B)
pos = dict()
pos.update( (n, (1, i)) for i, n in enumerate(X) ) # put nodes from X at x=1
pos.update( (n, (2, i)) for i, n in enumerate(Y) ) # put nodes from Y at x=2
nx.draw(B, pos=pos, with_labels=True, font_size=10)
plt.show()