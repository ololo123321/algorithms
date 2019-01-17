from itertools import combinations
from collections import defaultdict
from copy import deepcopy
from graphviz import Graph
import random


def create_graph(n_nodes=5, max_edge=2, p=0.5):
    g = defaultdict(list)
    for i, j in combinations(range(n_nodes), 2):
        if random.random() < p:
            d = random.randint(1, max_edge)
            g[i].append((j, d))
    return [g[i] for i in range(n_nodes)]


def plot_graph(g):
    G = Graph()
    for u, children in enumerate(g):
        for v, dist in children:
            G.edge(str(u), str(v), label=str(dist))
    return G


def get_symmetric_graph(g):
    g_new = deepcopy(g)
    for u, children in enumerate(g):
        for v, d in children:
            g_new[v].append((u, d))
    return g_new


def create_graph_edges(n_nodes=5, max_edge=2, p=0.5):
    edges = []
    for u, v in combinations(range(n_nodes), 2):
        if random.random() > p:
            d = random.randint(1, max_edge)
            edges.append((u, v, d))
    return edges


def plot_graph_from_edges(g):
    G = Graph()
    for u, v, d in g:
        G.edge(str(u), str(v), label=str(d))
    return G


def get_edges_duplicates(edges):
    edges_new = edges.copy()
    for u, v, d in edges:
        edges_new.append((v, u, d))
    return edges_new
