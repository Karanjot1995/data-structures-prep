from collections import defaultdict
from Templates.directedGraph import Graph

class Graph(Graph):

    def topoSort(self):
      graph = self.adj
      vis = {}
      s=[]

      for node in graph:
        vis[node] = 0

      def dfs(curr,graph):
        vis[curr] = 1
        for neighbor in graph[curr]:
          if not vis[neighbor]:
            dfs(neighbor, graph)
        s.append(curr)

      for node in graph:
        if not vis[node]:
          dfs(node,graph)
      s.reverse()
      return s
    

    def topoSortKahns(self):
      graph = self.adj
      in_degree = [0]*len(graph)

      for i in graph:
        for j in graph[i]:
          in_degree[j]+=1

      q = []
      topo_sort = []
      for node in graph:
        if in_degree[node]==0:
          q.append(node)

      while q:
        curr = q.pop(0)
        topo_sort.append(curr)
        for neighbor in graph[curr]:
          in_degree[neighbor]-=1
          if in_degree[neighbor]==0:
            q.append(neighbor)

      return topo_sort
    

    def isCyclicDAG(self):
      graph = self.adj
      in_degree = [0]*len(graph)

      for i in graph:
        for j in graph[i]:
          in_degree[j]+=1

      q = []
      cnt = 0
      for node in graph:
        if in_degree[node]==0:
          q.append(node)

      while q:
        curr = q.pop(0)
        cnt+=1
        
        for neighbor in graph[curr]:
          in_degree[neighbor]-=1
          if in_degree[neighbor]==0:
            q.append(neighbor)
    
      return False if cnt==len(graph) else True

          


graph = Graph(6)

graph.addVertex(0)
graph.addVertex(1)
graph.addVertex(2)
graph.addVertex(3)
graph.addVertex(4)
graph.addVertex(5)
# graph.addVertex(6)
# graph.addVertex(7)
# graph.addVertex(8)
# graph.addVertex(9)
# graph.addVertex(10)
# graph.addVertex(11)

graph.addEdge(5, 2)
graph.addEdge(5, 0)
graph.addEdge(4, 0)
graph.addEdge(4, 1)
graph.addEdge(2, 3)
graph.addEdge(3, 1)
# graph.addEdge(0,1)
# graph.addEdge(1,2)
# graph.addEdge(2,3)
# graph.addEdge(3,4)
# graph.addEdge(3,5)
# graph.addEdge(4,6)
# graph.addEdge(5,6)
# graph.addEdge(6,7)
# graph.addEdge(8,1)
# graph.addEdge(8,9)
# graph.addEdge(9,10)
# graph.addEdge(10,8)
# graph.addEdge(11,9)

print(graph.topoSort())
print(graph.topoSortKahns())
print(graph.isCyclicDAG())

