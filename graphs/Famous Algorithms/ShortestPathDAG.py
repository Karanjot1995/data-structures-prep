from Templates.DirectedWeighted import Graph

class Graph(Graph):
    
    def topo(self):
      graph = self.adj
      vis = {}
      s=[]
      #node[0] is the node and node[1] is the weight
      for node in graph:
        vis[node] = 0

      def dfs(curr,graph):
        vis[curr] = 1
        for neighbor in graph[curr]:
          if not vis[neighbor[0]]:
            dfs(neighbor[0], graph)
        s.append(curr)

      for node in graph:
        if not vis[node]:
          dfs(node,graph)
          
      return s
    
    def shortestPathDAG(self):
      adj = self.adj
      s = self.topo()
      print(s)
      dist = [float('inf')]*len(s)
      dist[-1]=0
      while s:
        u = s.pop()
        for neighbor in adj[u]:
          v = neighbor[0]
          wt = neighbor[1]
          if dist[u]+wt<dist[v]:
            dist[v]=dist[u]+wt
      return dist
        




g = Graph(6)

g.addVertex(0)
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addVertex(4)
g.addVertex(5)
g.addVertex(6)

g.addEdge(0, 1, 2)
g.addEdge(1, 3, 1)
g.addEdge(2, 3, 3)
g.addEdge(4, 0, 3)
g.addEdge(4, 2, 1)
g.addEdge(5, 4, 1)
g.addEdge(6, 4, 2)
g.addEdge(6, 5, 3)


print(g.shortestPathDAG())