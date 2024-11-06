class Graph:
    def __init__(self, vertices) -> None:
      self.adjacencyList = {}
      self.V = vertices

    def addVertex(self, vertex):
        if vertex not in self.adjacencyList: 
          self.adjacencyList[vertex]=[]
        return self.adjacencyList
    

    def addEdge(self,vertex1,vertex2):
      self.adjacencyList[vertex1].append(vertex2)
      return self.adjacencyList




g = Graph(6)

g.addVertex(0)
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addVertex(4)
g.addVertex(5)
# graph.addVertex(6)
# graph.addVertex(7)
# graph.addVertex(8)
# graph.addVertex(9)
# graph.addVertex(10)
# graph.addVertex(11)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)