from collections import defaultdict

class Graph:
    def __init__(self) -> None:
      self.adj = {}

    def addVertex(self, vertex):
        if vertex not in self.adj: 
          self.adj[vertex]=[]
        return self.adj
    

    def addEdge(self,vertex1,vertex2):
      self.adj[vertex1].append(vertex2)
      self.adj[vertex2].append(vertex1)
      return self.adj