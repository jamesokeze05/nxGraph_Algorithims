from itertools import combinations 
from Functions.bool_function import is_matching
from Functions.global_properties import n, E
from math import floor 
import networkx as nx

def maximum_matching(G):
    for k in range(floor(n(G)/2), 1, -1):
        for M in combinations(E(G),k):
            if is_matching(G,list(M)) == True:
                return list(M)

def matching_number(G):
    return len(maximum_matching(G))
        
