import networkx as nx
from Functions.global_properties import *
from Functions.local_properties import *

def is_clique(G, s):
    for i in range(len(s)):
        N=neighbors(G, s[i])
        for j in range(i +1, len(s)):
            if s[i + 1] not in N:
                return False
    return True