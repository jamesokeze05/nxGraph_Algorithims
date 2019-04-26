import networkx as nx
from Functions.local_properties import *
from Functions.global_properties import *


def is_independent(G, S):
    for v in S:
        N = neighbors(G, v)
        if list(set(N) & set(S)) != []:
            return False
    return True


def is_clique(G, s):
    for i in range(len(s)):
        N = neighbors(G, s[i])
        for j in range(i + 1, len(s)):
            if s[i + 1] not in N:
                return False
    return True

def is_dominating(G, S):
    S_complement = list(set(V(G)) - set(S))
    for v in S_complement:
        N = neighbors(G, V)
        if list(set(N) & set (S)) == []:
            return False
    return True

def is_matching (G,M):
    for edge1 in M:
        v, w = edge1
        for edge2 in M:
            if edge2!=edge1:
                if v in edge1 or w in edge1:
                    return False
    return True
