from scipy.interpolate import interp1d
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
    
def kruskals_am(graph):
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
        


def compute_indegree(graph,v):
    indeg = 0
    for i in range(graph.num_vertices()):
        if graph.am[i][v]>0:
            indeg +=1
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

    if len(sort_result) != graph.num_vertices() :
        return None

    return sort_result

   

