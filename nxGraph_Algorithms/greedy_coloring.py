from Functions.global_properties import V
from Functions.local_properties import neighbors
import networkx as nx

def greedy_coloring(G):
    colors = {v: None for v in V(G)}
    colors[V(G)[0]] = 1
    for v in V(G):
        if colors[v] == None:
            N = neighbors(G,v)
            bad_colors = [colors[w] for w in N]
            j = 1
            while colors[v] == None:
                if j not in bad_colors:
                    colors[v] = j
                else:
                    j+= 1
    return colors
