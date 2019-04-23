# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 17:55:34 2019

@author: King James
"""

import networkx as nx
from Functions.global_properties import *
from independence import *

G = nx.erdos_renyi_graph(10, .3)

print(maximum_independent_set(G))