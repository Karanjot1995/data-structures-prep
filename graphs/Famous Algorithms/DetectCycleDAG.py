from Templates.directedGraph import Graph

class Graph(Graph):
  def isCyclicDAG(self):
    adj = self.adj
    vis = [-1]*(len(adj)+1)
    
    def dfs(u):
      vis[u]=1
      for v in adj[u]:
        if vis[v]==-1:
          if dfs(v) == True: return True
        elif vis[v]==1:
          return True
      vis[u]=0
      return False
    
    for node in adj:
      if vis[node]==-1:
        if dfs(node)==True:
          print('It has a cycle: ', True)
          return True
    
    print('It has a cycle: ', False)
    return False
      



graph = Graph(10)

graph.addVertex(1)
graph.addVertex(2)
graph.addVertex(3)
graph.addVertex(4)
graph.addVertex(5)
graph.addVertex(6)
graph.addVertex(7)
graph.addVertex(8)
graph.addVertex(9)
graph.addVertex(10)

graph.addEdge(1,2)
graph.addEdge(2,3)
graph.addEdge(3,4)
graph.addEdge(4,5)
graph.addEdge(3,7)
graph.addEdge(7,5)
graph.addEdge(5,6)
graph.addEdge(8,2)
graph.addEdge(8,9)
graph.addEdge(9,10)
graph.addEdge(10,8)
# graph.addEdge(11,9)


print(graph.isCyclicDAG())
