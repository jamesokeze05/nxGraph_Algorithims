from itertools import combinations 
from Functions.bool_function import is_independent
from Functions.global_properties import V,n, E
from Functions.bool_function import is_matching
from math import floor 
import networkx as nx


def matching(G):
    for k in range(floor(n(G)/2), 1, -1):
        for M in combinations(E(G),k):
            if is_matching(G,list(M)) == True:
                return list(M)
            

G = nx.erdos_renyi_graph(7,.3)
nx.draw_networkx(G)
print(matching(G))
