"""
Author:Ruben Bustamante
Instructor: Diego Aguirre
TA:Gerarado Barraza
Course: CS 2302
Assigment: Lab graphs am
Date of last modification: 12/03/2019
Purpose of program: implement topogical and kruskals
"""

from queue import Queue
from DSF2 import DisjointSetForest
    
class GraphAM:

    def __init__(self, vertices, weighted=False, directed=False):
        self.am = []

        for i in range(vertices):  # Assumption / Design Decision: 0 represents non-existing edge
            self.am.append([0] * vertices)

        self.directed = directed
        self.weighted = weighted
        self.representation = 'AM'

    def is_valid_vertex(self, u):
        return 0 <= u < len(self.am)

    def insert_vertex(self):
        for lst in self.am:
            lst.append(0)

        new_row = [0] * (len(self.am) + 1)  # Assumption / Design Decision: 0 represents non-existing edge
        self.am.append(new_row)

        return len(self.am) - 1  # Return new vertex id
    def num_edges(self):
        count=0
        
        for i in range(len(self.am)):
            for edge in range(len(self.am[i])):
                if self.am[i][edge]!=0:
                    count +=1
        return count

    def insert_edge(self, src, dest, weight=1):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        self.am[src][dest] = weight

        if not self.directed:
            self.am[dest][src] = weight

    def delete_edge(self, src, dest):
        self.insert_edge(src, dest, 0)

    def num_vertices(self):
        return len(self.am)

    def vertices_reachable_from(self, src):
        reachable_vertices = set()

        for i in range(len(self.am)):
            if self.am[src][i] != 0:
                reachable_vertices.add(i)

        return reachable_vertices

    def sort_edges(self):
        e = []
        for i in  range(len(self.am)):
            for edge in range(len(self.am)):
                if self.am[i][edge] !=0:
                    e.append((i,edge, self.am[i][edge]))
        e.sort(key=lambda weight:weight[2], reverse=False)
        return e
    
    def cycle(self):
        dsf = DisjointSetForest(self.num_vertices())
        edges = len(self.am)# number of vertices
        for i in range(len(self.am)):
 
            for e in range(edges):# edges 
                if self.am[i][e] != 0:# check if an edges exist
                    if dsf.find(i) == dsf.find(e):# check if cycle exist
                        return True
                    dsf.union(i,e)
        return False
                
def kruskals_am(graph):
        sorted_edges = graph.sort_edges()#sort the edges in a list

        T = GraphAM(graph.num_vertices(), weighted=True, directed=True)# empty graph
      
        for i in range(graph.num_edges()):
            # inserte the vertices, edges and weight stored in the list
            T.insert_edge(sorted_edges[i][0], sorted_edges[i][1], sorted_edges[i][2])
            # deletes if the edge that cause the cylcle
            if T.cycle():
                T.delete_edge(sorted_edges[i][0], sorted_edges[i][1])
        # the new graph     
        for i in range(len(T.am)):
            for e in range(len(T.am[i])):
                if T.am[i][e]!=0:
                    print(i,e,T.am[i][e])
                    
def compute_indegree(graph,v):
    indeg = 0
    for i in range(graph.num_vertices()):
        if graph.am[i][v]>0: # checks if a edge exist 
            indeg +=1 # adds 1 for index for that vertex
    return indeg

def topological_sort_am(graph):
    
    q = Queue()
    in_degree= {}
    sort_result=[]
    for i in range(graph.num_vertices()):
        in_degree[i] = compute_indegree(graph,i)
        if in_degree[i]==0:
            q.put(i)

    
    while not q.empty():
        u = q.get()
        sort_result.append(u)
        for j in graph.vertices_reachable_from(u):
            in_degree[j] -=1
            if in_degree[j] == 0:
                q.put(j)

    if len(sort_result) != graph.num_vertices(): # eheck if a cycle exist
        return None

    return sort_result


