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


import networkx as nx

def neighbors(G, v):
    return list(nx.neighbors(G, v)) 

def degree(G, v):
    return len(neighbors(G, v))

def V(G):
    return list(nx.nodes(G))

    
def E(G):
    return list(nx.edges(G))


    

g = nx.read_edgelist('sampleG.txt', nodetype=str,
  data=(('weight',int),), create_using=nx.Graph())

t = nx.Graph()
t.add_node('a')


      

def incident_edges(g,t):
    l = nx.Graph()
    for e in E(g):
        if  e[0] in V(t):
            l.add_node(e)
        elif e[1] in V(t):
            l.add_node(e)
    return l.nodes()

#print("this prints out all the edges attached to starting node", incident_edges(g,t))
#print()

#Function determines if edge is in MST and ignores all
#incident edges that are already in MST 
#def in_graph(g,t):
#    d = incident_edges(g,t)#gets incident edges to current vertex 
#    f = list(d) # adds them to a variable f as list
#    a = len(d)
#    for i in range(a):
#        current_edge = f[i]
#       if current_edge in E(t):
 #           return True 
 #       else:
 #           return False
 
#u = min_incident_node(g,t)


#def add_edge(g,t, u, v):
#     if ___ in E(g):
#         t.add_edge(u,v)
#         g.remove_edge(u,v)     

def min_incident_edges(g,t):
    return min(incident_edges(g,t))


print(min_incident_edges(g,t))

#removes the edge from priority q and adds it to MST t
def remove_add_edge(g,t):
    a = min_incident_edges(g,t)
    f = list(a)
    j = f[0]
    d = f[1]
    if f[j][d] in E(g) and f[j][d] not in E(t):
        t.add_edge(j,d)
        g.remove_edges(j,d)

d = t.edges()

def cost(g,e):
    return g[e[0]e[1]]['weight']

#print('this prints the min weighted edge to vertex', min_incident_edges(g,t))
#print()


#gets the verteces of the minimum incident edge of current vertex and 
#adds the vertex currently not in MST t to the MST t
def min_incident_node(g,t):
    d = min_incident_edges(g,t)#gets the minimum weighted edge 
    f = list(d)# assigns d to a list of d
    a = len(d)
    current_vertex = t.node()
    for i in range(a):
        vertex = f[i]
        if vertex not in V(t):
            t.add_node(vertex)
            current_vertex = vertex
            return current_vertex
        
#print('get the current vertex:',min_incident_node(g,t))
#print(t.edges())


import networkx as nx
import matplotlib.pyplot as plt 

g = nx.read_edgelist('weightedgraph.txt', nodetype=str,
  data=(('weight',int),), create_using=nx.Graph())


print(g.edges(data=True))

def prims(g,starting_vertex):
    t = nx.Graph() #empty graph t to store vertices removed from proirity queue g
    t.add_node(starting_vertex)#stores vertex in MST t
    g.remove_node(starting_vertex)#removed vertex from priority Queue g 
    while is_spanning(g,t) == False:#while all the verteces in priority queue g are not in MST graph t
     #   if in_graph(g,t) == False:# if the edge does not exist in MST graph t
            t.add_node(min_incident_edge(g,t))
    #return t, tree_cost(t)
