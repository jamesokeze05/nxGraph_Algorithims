import networkx as nx
from Functions.bool_function import is_clique
from Functions.global_properties import V , n
from itertools import combinations

def maximum_clique(G):
    for k in range(n(G), 1, -1):
        for S in combinations(V(G), k):
            if is_clique(G, list(S)) == True:
                return list(S)
            
def clique_numbers(G):
    return len(maximum_clique(G))

G = nx.erdos_renyi_graph(7,.3)
print(maximum_clique(G))
