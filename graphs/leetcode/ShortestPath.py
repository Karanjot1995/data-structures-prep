from Templates.graph import Graph

class Graph(Graph):
    
    def shortestPath(self,start):
      adj = self.adj
      n = len(adj)
      q = []
      q.append(start)
      dist = [float('inf')]*n
      dist[start]=0

      while q:
        curr = q.pop(0)
        for neighbor in adj[curr]:
          if dist[curr]+1 < dist[neighbor]:
            dist[neighbor] = dist[curr]+1
            q.append(neighbor)

      ans = [-1]*n
      for i in range(n):
        if dist[i]!=float('inf'):
          ans[i]=dist[i]
      return ans      


g = Graph()

g.addVertex(0)
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addVertex(4)
g.addVertex(5)
g.addVertex(6)
g.addVertex(7)
g.addVertex(8)

g.addEdge(0, 1)
g.addEdge(0, 3)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(3, 4)
g.addEdge(4, 5)
g.addEdge(2, 6)
g.addEdge(5, 6)
g.addEdge(6, 7)
g.addEdge(6, 8)
g.addEdge(7, 8)



print(g.shortestPath(0))