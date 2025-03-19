import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


def plot(network):
    nodes = [n.split() for n in open('D:\数据\重要论文附件\FRLMwCT-main\instance\\' + network + '\\NODES.txt', 'r')]
    arcs = [[round(float(v)) for v in a.split()] for a in
            open('D:\数据\重要论文附件\FRLMwCT-main\instance\\' + network + '\\ARCS.txt', 'r')]
    nodes_dict = dict(zip([eval(nodes[i][0]) for i in range(len(nodes))],
                          [[] for i in range(len(nodes))]))
    for i in range(len(nodes)):
        nodes_dict[i + 1].append(eval(nodes[i][2]))
        nodes_dict[i + 1].append(eval(nodes[i][3]))
        nodes_dict[i + 1].append(eval(nodes[i][1]))

    arcs_keys = []





    for i in range(len(arcs)):
        arcs_keys.append((arcs[i][2], arcs[i][3]))

    arcs_dict = dict(zip(arcs_keys, [[arcs[i][1]] for i in range(len(arcs_keys))]))

    for arc in arcs_keys:
        arcs_dict[arc].append(
            np.sqrt((nodes_dict[arc[0]][0] - nodes_dict[arc[1]][0]) ** 2 + (nodes_dict[arc[0]][1] - nodes_dict[arc[1]][1]) ** 2))
    print(arcs_dict)
    plt.figure(figsize=(20, 20))

    od_nodes = []

    for i in range(len(nodes)):
        if nodes_dict[i + 1][2] > 0:
            od_nodes.append(i + 1)
            plt.scatter(nodes_dict[i + 1][0], nodes_dict[i + 1][1], c='r', s=120, label=str(i))
        else:
            plt.scatter(nodes_dict[i + 1][0], nodes_dict[i + 1][1], c='b', s=30)
        # plt.annotate(str(i + 1), (nodes_dict[i + 1][0], nodes_dict[i + 1][1]), c='k', size=20)
    for arc in arcs_dict:
        plt.plot([nodes_dict[arc[0]][0], nodes_dict[arc[1]][0]],
                 [nodes_dict[arc[0]][1], nodes_dict[arc[1]][1]], c='k')
    print('OD节点数量', len(od_nodes))
    plt.show()


plot('TEXAS')
