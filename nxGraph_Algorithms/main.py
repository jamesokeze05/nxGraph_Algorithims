# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 17:55:34 2019

@author: King James
"""

import networkx as nx
from Functions.global_properties import *
from independence import *

G = nx.read_edgelist('Test_Graphs/G1.txt')

print(maximum_independent_set(G))
