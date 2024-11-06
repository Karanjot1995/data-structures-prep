class Graph():
    def __init__(self, vertices) -> None:
      self.adj = {}
      self.V = vertices

    def addVertex(self, vertex):
        if vertex not in self.adj: 
          self.adj[vertex]=[]
        return self.adj

    def addEdge(self,vertex1,vertex2, weight):
      self.adj[vertex1].append([vertex2,weight])
      self.adj[vertex2].append([vertex1,weight])
      return self.adj
