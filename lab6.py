# -*- coding: utf-8 -*-
"""
Author:Ruben Bustamante
Instructor: Diego Aguirre
TA:Gerarado Barraza
Course: CS 2302
Assigment: lab 7-unit test
Date of last modification: 12/03/2019
Purpose of program:graph test
"""
from graph_al import GraphAL,topological_sort,kruskals
from graph_am  import GraphAM, topological_sort_am,kruskals_am

def main():
    g = GraphAL(6, weighted=True,directed=True)
    g.insert_edge(0, 1,4)
    g.insert_edge(1, 2,5)
    g.insert_edge(2, 3,10)
    g.insert_edge(2, 4,5)
    g.insert_edge(3, 4,20)
    g.insert_edge(3, 5, 2)
    print('topological AL')
    print(topological_sort(g))
    

    g2 = GraphAM(6, weighted=True,directed=True)
    g2.insert_edge(0, 1,4)
    g2.insert_edge(1, 2,5)
    g2.insert_edge(2, 3,10)
    g2.insert_edge(3, 4,20)
    print('topological AM')
    print(topological_sort_am(g2))
    print('Graph AM kruskals AL')
    g3 = GraphAL(6, weighted=True,directed=True)
    g3.insert_edge(0, 1,40)
    g3.insert_edge(0,2,6 )
    g3.insert_edge(1, 2,5)
    g3.insert_edge(1,3,7)
    g3.insert_edge(2, 3,10)
    g3.insert_edge(3, 4,20)
    g3.insert_edge(4,0, 5)
    g3.insert_edge(4,2,1)
    kruskals(g3)
    print('Graph AM kruskals AM')
    g4 = GraphAM(6, weighted=True,directed=True)
    g4.insert_edge(0, 1,40)
    g4.insert_edge(0,2,6 )
    g4.insert_edge(1, 2,5)
    g4.insert_edge(1,3,7)
    g4.insert_edge(2, 3,10)
    g4.insert_edge(3, 4,20)
    g4.insert_edge(4,0, 5)
    g4.insert_edge(4,2,1)
    kruskals_am(g4)
  
main()  