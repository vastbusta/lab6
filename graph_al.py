
from queue import Queue
from DSF2 import DisjointSetForest
import math

class Edge:
    def __init__(self, dest, weight=1):
        self.dest = dest
        self.weight = weight


class GraphAL:
    # Constructor
    def __init__(self, vertices, weighted=False, directed=False):
        self.al = [[] for i in range(vertices)]
        self.weighted = weighted
        self.directed = directed
        self.representation = 'AL'

    def is_valid_vertex(self, u):
        return 0 <= u < len(self.al)

    def insert_vertex(self):
        self.al.append([])

        return len(self.al) - 1  # Return id of new vertex

    def insert_edge(self, source, dest, weight=1):
        if not self.is_valid_vertex(source) or not self.is_valid_vertex(dest):
            print('Error, vertex number out of range')
        elif weight != 1 and not self.weighted:
            print('Error, inserting weighted edge to unweighted graph')
        else:
            self.al[source].append(Edge(dest, weight))
            if not self.directed:
                self.al[dest].append(Edge(source, weight))

    def delete_edge(self, source, dest):
        if source >= len(self.al) or dest >= len(self.al) or source < 0 or dest < 0:
            print('Error, vertex number out of range')
        else:
            deleted = self._delete_edge(source, dest)
            if not self.directed:
                deleted = self._delete_edge(dest, source)
            if not deleted:
                print('Error, edge to delete not found')

    def _delete_edge(self, source, dest):
        i = 0
        for edge in self.al[source]:
            if edge.dest == dest:
                self.al[source].pop(i)
                return True
            i += 1
        return False

    def num_vertices(self):
        return len(self.al)

    def vertices_reachable_from(self, src):
        reachable_vertices = set()

        for edge in self.al[src]:
            reachable_vertices.add(edge.dest)

        return reachable_vertices
   
            
    def num_edges(self):
        count=0
        
        for i in range(len(self.al)):
            for edge in self.al[i]:
                if edge.dest!=0:
                    count +=1
        return count
    
    def sort_edges(self):
        e = []
        for i in  range(len(self.al)):
            for edge in self.al[i]:
                if edge.weight !=0:
                    e.append((i,edge.dest,edge.weight))
        e.sort(key=lambda weight:weight[2], reverse=False)
        return e
   
                
def kruskals(graph):
    sort = graph.sort_edges()
  
    T={}
    
    forest = DisjointSetForest(len(sort))
    for edge in sort:#sorted eges
        for i in range(len(sort)):
            if i == 0:#if index is zerot
                 
                T[edge[i]] = edge[i+1]# the first edeges
         
                forest.union(edge[i], edge[i+1])
                i += 1

    return T               
        

        
        
def compute_indegree(graph):# finds indegrees of each vertex
    
    if graph.al is None:
        return None
    
    in_deg = [0]*len(graph.al)# creates list that is lenght of num of veritices filled in by zeros
   
    for i in range(len(graph.al)):
        for edge in graph.al[i]:
            in_deg[edge.dest]+=1 # counts the indegrees and stores them in list by index
            
    return in_deg  # returns the count of the indegreses

def topological_sort(graph):
    
    sort_result = []
    q = Queue()
    in_degree=compute_indegree(graph)#stores all the indegrees
 
    for i in range(len(in_degree)):

        if in_degree[i]==0:# if any in_degrees are zero store them in queue
            q.put(i)
            
    while not q.empty():
        u =q.get() #dequeue first element stores it in u
       
        sort_result.append(u)
        
        for j in graph.vertices_reachable_from(u):# checks all vertices adjancy to u
           
            in_degree[j] -=1 # minus one from each in degree
            if in_degree[j] ==0:#stores any of them that is zero
                q.put(j)
                
    if len(sort_result)!=graph.num_vertices():# if a cycle exist return none
        return None
    
    return sort_result # return the stored veritices 

