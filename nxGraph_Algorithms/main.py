import networkx as nx
from Functions.global_properties import *
from independence import *

G = nx.read_edgelist('Test_Graphs/G1.txt')

print(maximum_independent_set(G))
