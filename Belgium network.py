import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

# nodes dict
nodes = pd.read_excel('D:\数据\重要论文附件\FRLMwCT-main\instance\Belgium\\belgian_municipalities.xlsx',
                      header=None).values

nodes_dict = dict(zip([nodes[i][0] for i in range(len(nodes))],
                      [[] for i in range(len(nodes))]))

for i in range(len(nodes)):
    for j in [3, 2, 4]:
        nodes_dict[nodes[i][0]].append(nodes[i][j])

# arcs dict
arcs = pd.read_excel('D:\数据\重要论文附件\FRLMwCT-main\instance\Belgium\\edges.xlsx',
                     header=None).values
arcs_dict = dict(zip([(arc[0], arc[1]) for arc in arcs] + [(arc[1], arc[0]) for arc in arcs],
                     [arc[2] for arc in arcs] + [arc[2] for arc in arcs]))

# od nodes dict
od_nodes_dict = dict(zip([i for i in nodes_dict if nodes_dict[i][2] > 30000],
                         [[nodes_dict[i][0], nodes_dict[i][1], nodes_dict[i][2]]
                          for i in nodes_dict if nodes_dict[i][2] > 30000]))
od_nodes = list(od_nodes_dict.keys())
print('OD节点数量', len(od_nodes))

# od pairs dict
od_pairs = []
for i in range(len(od_nodes)):
    for j in range(i + 1, len(od_nodes)):
        od_pairs.append((od_nodes[i], od_nodes[j]))
print('OD对数量', len(od_pairs))
od_pairs_dict = dict(zip(od_pairs, [[] for odp in od_pairs]))

# Create the graph
G = nx.DiGraph()
G.add_nodes_from(nodes_dict.keys())
G.add_weighted_edges_from([(arc[0], arc[1], arc[2]) for arc in arcs]
                          + [(arc[1], arc[0], arc[2]) for arc in arcs])

# complete the od pairs dict
for odp in od_pairs:
    od_pairs_dict[odp].append(nodes_dict[odp[0]][2])
    od_pairs_dict[odp].append(nodes_dict[odp[1]][2])
    od_pairs_dict[odp].append(nx.shortest_path_length(G, odp[0], odp[1], weight='weight'))

# Plot
plt.figure(figsize=(20, 20))
for i in range(len(nodes_dict)):
    if i + 1 in od_nodes:
        plt.scatter(nodes_dict[i + 1][0], nodes_dict[i + 1][1], c='r', s=80)
    else:
        plt.scatter(nodes_dict[i + 1][0], nodes_dict[i + 1][1], c='k', s=20)

for arc in arcs_dict:
    plt.plot([nodes_dict[arc[0]][0], nodes_dict[arc[1]][0]],
             [nodes_dict[arc[0]][1], nodes_dict[arc[1]][1]], c='k')

plt.show()
