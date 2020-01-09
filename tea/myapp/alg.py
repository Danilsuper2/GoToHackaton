import networkx as nx
import pandas as pd


def match():
    file = pd.read_csv('myapp/csv.csv', sep=",")
    s = [list(file.loc[i]) for i in range(len(file["Fios"]))]  # TODO: ИСПРАВИТЬ ДЛЯ ФУНКЦИИ LEN()
    d = {s[i][0]: s[i][1:] for i in range(len(s))}
    pandas = d
    users = list(pandas.keys())

    p = len(pandas[users[0]])
    n = len(users)

    def weight(a, b):
        node1, node2 = pandas[users[a]], pandas[users[b]]
        w = 0
        for i in range(p, 0, -1):
            if node1[i - 1] != node2[i - 1]:
                w += 2 ** (i - 1)
        return w

    def weight_edges():
        edges = []
        for node1 in range(n):
            for node2 in range(node1, n):
                if node1 != node2:
                    edges.append((users[node1], users[node2], weight(node1, node2)))
        return edges

    g = nx.Graph()
    g.add_nodes_from(users)
    g.add_weighted_edges_from(weight_edges())

    return list(nx.max_weight_matching(g))
