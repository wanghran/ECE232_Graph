import networkx as nx
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
import numpy as np

G = nx.Graph()

with open('../output/edge_list.txt', 'r') as f:
    edge_list = f.readlines()
    edges = []
    for line in edge_list:
        temp = line.split('\t')
        src = int(temp[0])
        dst = int(temp[1])
        weight = float(temp[2].split('\n')[0])
        edges.append((src, dst, weight))

with open('../output/feat_list.txt', 'r') as f:
    feat_list = f.readlines()[1:]
    pos = {}
    attr = {}
    loc = {}
    for line in feat_list:
        temp = line.split('|')
        movement_id = int(temp[0])
        name = temp[1]
        loc_x = float(temp[2].split(',')[0])
        loc_y = float(temp[2].split(',')[1])
        pos[movement_id] = (loc_x, loc_y)
        attr[movement_id] = {'name': name, 'pos': [loc_x, loc_y]}
        loc[(loc_x, loc_y)] = movement_id

G.add_weighted_edges_from(edges)
nx.set_node_attributes(G, attr)
giant = max(nx.connected_component_subgraphs(G), key=len)
# nx.draw(giant, pos=pos, nodecolor='r', node_size=50, edge_color='b', edge_tickness=1)
# plt.show()

pos_giant = nx.get_node_attributes(giant, 'pos')
points = np.array(list(pos_giant.values()))
tris = Delaunay(points)

sub_edges = []
sub_pos = {}
sub_attr = {}
for tri in points[tris.simplices]:
    for i in range(3):
        sub_pos[loc[(tri[i][0], tri[i][1])]] = (tri[i][0], tri[i][1])



    # if [tri[0], tri[1]] not in sub_edges:
    #     sub_edges.append([tri[0], tri[1]])
    # if [tri[1], tri[2]] not in sub_edges:
    #     sub_edges.append([tri[1], tri[2]])
    # if [tri[0], tri[2]] not in sub_edges:
    #     sub_edges.append([tri[0], tri[2]])


# plt.triplot(points[:, 0], points[:, 1], tri.simplices.copy(), color='blue')
# plt.plot(points[:, 0], points[:, 1], 'ro')
# plt.show()
