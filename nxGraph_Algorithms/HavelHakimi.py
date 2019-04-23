import networkx as nx
from Functions.global_properties import *


def Havel_Hakimi_Derivative(D):
    for i in range(1, D[0] +1):
        D[i] -= 1
        
    D.pop(0)
    D.sort(reverse = True)
    return None

def Havel_Hakimi_Process(D):
    while D[0] > 0:
        Havel_Hakimi_Derivative(D)
        
def is_Graphic(D):
    Havel_Hakimi_Process(D)
    return sum(D) == 0

def residue(G):
    D = degree_sequence(G)
    Havel_Hakimi_Process(D)
    return len(D)
