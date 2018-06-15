import networkx as nx
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
import numpy as np
import math
from networkx.algorithms.flow import shortest_augmenting_path

# Q11
disp = False
with open('../output/edge_list.txt', 'r') as f:
    edge_list = f.readlines()
    edges = []
    edge_dict = {}
    for line in edge_list:
        temp = line.split('\t')
        src = int(temp[0])
        dst = int(temp[1])
        weight = float(temp[2].split('\n')[0])
        edges.append((src, dst, weight))
        edge_dict[(src, dst)] = weight
        edge_dict[(dst, src)] = weight

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

G = nx.Graph()
G.add_weighted_edges_from(edges)
nx.set_node_attributes(G, attr)
giant = max(nx.connected_component_subgraphs(G), key=len)

if disp:
    nx.draw(giant, pos=pos, nodecolor='r', node_size=50, edge_color='b', edge_tickness=1)
    plt.show()

pos_giant = nx.get_node_attributes(giant, 'pos')
points = np.array(list(pos_giant.values()))
tris = Delaunay(points)

if disp:
    plt.triplot(points[:, 0], points[:, 1], tris.simplices.copy(), color='blue')
    plt.plot(points[:, 0], points[:, 1], 'ro')
    plt.show()

# for tri in points[tris.simplices]:
#     if (np.array([-122.0646, 36.9742]) in tri) and (np.array([-122.1760, 37.4297]) in tri):
#         print('true')

sub_edges = []
sub_edge_dict = {}
sub_pos = {}
sub_attr = {}

# num_d = 0
# num_sl = 0
# num = 0
for tri in points[tris.simplices]:
    for i in range(3):
        sub_pos[loc[(tri[i][0], tri[i][1])]] = (tri[i][0], tri[i][1])

        if i < 2:
            src = loc[(tri[i][0], tri[i][1])]
            dst = loc[(tri[i+1][0], tri[i+1][1])]
        else:
            src = loc[(tri[i][0], tri[i][1])]
            dst = loc[(tri[0][0], tri[0][1])]

        pair1 = (src, dst)
        pair2 = (dst, src)
        if pair1 in sub_edge_dict:
            pass
        elif pair2 in sub_edge_dict:
            pass
        else:
            # num += 1
            if pair1 in edge_dict:
                # num_d += 1
                sub_edge_dict[pair1] = edge_dict[pair1]
            else:
                # shortest path
                # num_sl += 1
                shortest_path = nx.shortest_path(G, source=src, target=dst)
                sum = 0
                for j in range(len(shortest_path)-1):
                    sum += edge_dict[(shortest_path[j], shortest_path[j+1])]
                sub_edge_dict[pair1] = sum

for k, v in sub_edge_dict.items():
    sub_edges.append((k[0], k[1], v))

# print(len(edge_dict))
# print(len(sub_edges))
# print(num)
# print(num_d)
# print(num_sl)
# print(sub_pos)

for k, v in sub_pos.items():
    sub_attr[k] = {'name': attr[k]['name'], 'pos': attr[k]['pos']}

sub_G = nx.Graph()
sub_G.add_weighted_edges_from(sub_edges)
nx.set_node_attributes(sub_G, sub_attr)

# print(len(sub_G.edges))

if disp:
    nx.draw(sub_G, pos=sub_pos, nodecolor='r', node_size=50, edge_color='b', edge_tickness=1)
    plt.show()


# Q12
capacity_dict = {}
for edge in sub_edges:
    loc_src = sub_pos[edge[0]]
    loc_dst = sub_pos[edge[1]]
    # print(loc_src)
    # print(loc_dst)
    dist = math.sqrt((loc_src[0] - loc_dst[0]) ** 2 + (loc_src[1] - loc_dst[1]) ** 2) * 69
    # print(dist)
    travel_time = edge[2]
    speed = dist / travel_time
    # print(speed)
    capacity = 3600 / ((0.003 / speed) + 2) * 4
    capacity_dict[(edge[0], edge[1])] = {'capacity': capacity}
    # print(capacity)
# print(capacity_dict)
nx.set_edge_attributes(sub_G, capacity_dict)
capa = nx.get_edge_attributes(sub_G, 'capacity')
# print(capa)

# Q13
flow_value, flow_dict = nx.maximum_flow(sub_G, 2607, 1968)  # Stanford and UCSC
print(flow_value)
print(len(list(nx.edge_disjoint_paths(sub_G, 2607, 1968, flow_func=shortest_augmenting_path))))

labels = {2607: 'Stanford', 1968: 'UCSC'}
if disp:
    nx.draw(sub_G, pos=sub_pos, nodecolor='r', node_size=5, edge_color='b', edge_tickness=1)
    nx.draw_networkx_labels(sub_G, pos=sub_pos, labels=labels)
    nx.draw_networkx_nodes(sub_G, pos=sub_pos, nodelist=[2607, 1989], node_color='k', node_size=5, alpha=1)
    plt.show()

# Q14
Threshold = 1198
reduced_G = nx.Graph()
reduced_edges = []
times = []
for edge in sub_edges:
    times.append(edge[2])
    if edge[2] < Threshold:
        reduced_edges.append(edge)
print(max(times))
plt.hist(times, 100)
plt.xlim((0, 4000))
plt.xticks(np.arange(0, 4000, 100))
plt.xticks(rotation=90)
plt.show()

reduced_G.add_weighted_edges_from(reduced_edges)
nx.set_node_attributes(reduced_G, sub_attr)

reduced_G.add_node('1_l')
sub_pos['1_l'] = (-122.475, 37.806)
reduced_G.add_node('1_r')
sub_pos['1_r'] = (-122.479, 37.83)

reduced_G.add_node('2_l')
sub_pos['2_l'] = (-122.501, 37.956)
reduced_G.add_node('2_r')
sub_pos['2_r'] = (-122.387, 37.93)

reduced_G.add_node('3_l')
sub_pos['3_l'] = (-122.273, 37.563)
reduced_G.add_node('3_r')
sub_pos['3_r'] = (-122.122, 37.627)

reduced_G.add_node('4_l')
sub_pos['4_l'] = (-122.142, 37.486)
reduced_G.add_node('4_r')
sub_pos['4_r'] = (-122.067, 37.54)

reduced_G.add_node('5_l')
sub_pos['5_l'] = (-122.388, 37.788)
reduced_G.add_node('5_r')
sub_pos['5_r'] = (-122.302, 37.825)

nx.draw(reduced_G, pos=sub_pos, nodecolor='r', node_size=1, edge_color='b', edge_tickness=1)
nx.draw_networkx_nodes(reduced_G, pos=sub_pos, nodelist=['1_l', '1_r'], node_color='k', node_size=5, alpha=1)
nx.draw_networkx_nodes(reduced_G, pos=sub_pos, nodelist=['2_l', '2_r'], node_color='g', node_size=5, alpha=1)
nx.draw_networkx_nodes(reduced_G, pos=sub_pos, nodelist=['3_l', '3_r'], node_color='c', node_size=5, alpha=1)
nx.draw_networkx_nodes(reduced_G, pos=sub_pos, nodelist=['4_l', '4_r'], node_color='m', node_size=5, alpha=1)
nx.draw_networkx_nodes(reduced_G, pos=sub_pos, nodelist=['5_l', '5_r'], node_color='y', node_size=5, alpha=1)
plt.show()

# Q15
nx.set_edge_attributes(reduced_G, capacity_dict)
flow_value, flow_dict = nx.maximum_flow(reduced_G, 2607, 1968)  # Stanford and UCSC
print(flow_value)
print(len(list(nx.edge_disjoint_paths(reduced_G, 2607, 1968, flow_func=shortest_augmenting_path))))









