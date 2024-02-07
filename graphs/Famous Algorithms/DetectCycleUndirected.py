from Templates.graph import Graph

class Graph(Graph):
  def isCyclicBFS(self):
    start = 0
    adj = self.adj
    vis = [0]*len(adj)

    vis[start] = 1
    q = [[start,-1]]

    print(adj)
    while q:
      u,parent = q.pop(0)

      for v in adj[u]:
        if not vis[v]:
          q.append([v,u])
          vis[v]=1
        elif v != parent:
          return True
    return False
  

  def isCyclicDFS(self):
    start = 0
    adj = self.adj
    vis = [0]*len(adj)

    vis[start] = 1
    q = [[start,-1]]

    def dfs(u,parent):
      vis[u]= 1
      for v in adj[u]:
        if not vis[v]:
          if dfs(v,u) == True: return True
        elif v != parent:
          return True
      return False

  
    return dfs(start,-1)
    # def dfs(curr):
    #   vis[curr]
      



graph = Graph()

graph.addVertex(0)
graph.addVertex(1)
graph.addVertex(2)
graph.addVertex(3)
graph.addVertex(4)
graph.addVertex(5)
graph.addEdge(0,1)
graph.addEdge(0,2)
graph.addEdge(1,3)
graph.addEdge(2,4)
graph.addEdge(3,5)
graph.addEdge(4,5)



print(graph.isCyclicBFS())
print(graph.isCyclicDFS())