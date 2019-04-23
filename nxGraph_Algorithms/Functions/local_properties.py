import networkx as nx
from Functions.global_properties import *
def neighbors(G, v):
    return list(nx.neighbors(G, v))

def vertex_degree(G,v):
    return len(neighbors(G, v))

def eccentricity(G, v):
    return len(distance_list(G, v))-1 

def degree_sequence(G):
    D=[vertex_degree(G, v) for v in V(G)]
    D.sort(reverse = True)
    return D