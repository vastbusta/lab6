# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 10:07:56 2019

@author: vasto
"""

from graph_al import GraphAL,topological_sort,kruskals
from graph_am  import GraphAM, topological_sort_am,kruskals_am

def main():
    g = GraphAL(6, weighted=True,directed=True)
    g.insert_edge(0, 1,4)
    g.insert_edge(1, 2,5)
    g.insert_edge(2, 3,10)
    g.insert_edge(3, 4,20)
  
    print(topological_sort(g))
    

    g2 = GraphAM(6, weighted=True,directed=True)
    g2.insert_edge(0, 1,4)
    g2.insert_edge(1, 2,5)
    g2.insert_edge(2, 3,10)
    g2.insert_edge(3, 4,20)
    print(topological_sort_am(g2))
    
    g3 = GraphAL(6, weighted=True,directed=True)
    g3.insert_edge(0, 1,40)
    g3.insert_edge(0,2,6 )
    g3.insert_edge(1, 2,5)
    g3.insert_edge(1,3,7)
    g3.insert_edge(2, 3,10)
    g3.insert_edge(3, 4,20)
    g3.insert_edge(4,0, 5)
    g3.insert_edge(4,2,1)
    print(kruskals(g3))
    
    g4 = GraphAL(6, weighted=True,directed=True)
    g4.insert_edge(0, 1,40)
    g4.insert_edge(0,2,6 )
    g4.insert_edge(1, 2,5)
    g4.insert_edge(1,3,7)
    g4.insert_edge(2, 3,10)
    g4.insert_edge(3, 4,20)
    g4.insert_edge(4,0, 5)
    g4.insert_edge(4,2,1)
    print(kruskals_am(g4))
  
main()  