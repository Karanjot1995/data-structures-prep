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
    

    def dfsCheck(self,curr, vis, pathVis):
      vis[curr] = 1
      pathVis[curr] = 1
      # print('vis: ', vis)
      # print('pathvis: ', pathVis)
      for neighbor in self.adjacencyList[curr]:
        if not vis[neighbor]:
          if self.dfsCheck(neighbor, vis, pathVis) == True: return True
        elif pathVis[neighbor]: return True
      pathVis[curr] = 0
      return False
       
    def isCyclicDirectedGraph(self):
      list = self.adjacencyList
      vis = {}
      pathVis = {}
      for node in list:
        vis[node] = 0
        pathVis[node] = 0
      
      for node in list:
        if not vis[node]:
          if self.dfsCheck(node, vis, pathVis) == True : return True

      return False
        
    def dfsEventual(self,curr, vis, pathVis, check):
      vis[curr] = 1
      # pathVis[curr] = 1
      for neighbor in self.adjacencyList[curr]:
        if vis[neighbor]==-1:
          if self.dfsEventual(neighbor, vis, pathVis, check) == True: return True
        # elif pathVis[neighbor]==1: return True
        elif vis[neighbor]==1: return True
      # pathVis[curr] = 0
      vis[curr]=0
      check[curr] = 1
      return False
       
    def eventualSafeNodes(self):
      list = self.adjacencyList
      check = {}
      vis = {}
      pathVis = {}
      for node in list:
        check[node]=0
        vis[node] = -1
        # pathVis[node] = 0
      
      for node in list:
        if vis[node]==-1:
          self.dfsEventual(node, vis, pathVis, check)

      safeNodes = []
      for node in check:
        if check[node] == 1:
          safeNodes.append(node)

      return safeNodes
    

    def topoSort(self):
      graph = self.adjacencyList
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
      graph = self.adjacencyList
      in_degree = [0]*len(graph)
      # in_degree = {}
      # for i in graph:
      #   in_degree[i]=0

      for i in graph:
        for j in graph[i]:
          in_degree[j]+=1

      q = []
      topo_sort = []
      for node in graph:
        if in_degree[node]==0:
          q.append(node)
      print('indegree:',in_degree)

      while q:
        curr = q.pop(0)
        topo_sort.append(curr)
        for neighbor in graph[curr]:
          in_degree[neighbor]-=1
          if in_degree[neighbor]==0:
            q.append(neighbor)

      return topo_sort
    
    def isCyclicDAG(self):
      graph = self.adjacencyList
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

# graph.addEdge(8,10)
# graph.addEdge(11,9)
# graph.addEdge(11,8)



print(graph.isCyclicDirectedGraph())
print(graph.eventualSafeNodes())
print(graph.topoSort())
print(graph.topoSortKahns())
print(graph.isCyclicDAG())

# graph.addVertex('A')
# graph.addVertex('B')
# graph.addVertex('C')
# graph.addVertex('D')
# graph.addVertex('E')
# graph.addVertex('F')
# graph.addVertex('G')
# graph.addEdge('A','B')
# graph.addEdge('B','D')
# # graph.addEdge('D','E')
# graph.addEdge('D','F')
# graph.addEdge('F','E')
# graph.addEdge('E','C')
# graph.addEdge('C','A')
# graph.addEdge('A','G')


# print(graph.isCyclicDirectedGraph())


  #     A
  #   /  \
  # B     C
  # |     |
  # D     E
  #  \   /
  #    F