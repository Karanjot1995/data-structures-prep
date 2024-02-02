class Graph:
    def __init__(self) -> None:
      self.adjacencyList = {}

    def addVertex(self, vertex):
        if vertex not in self.adjacencyList: 
          self.adjacencyList[vertex]=[]
        # print(self.adjacencyList)
        return self.adjacencyList
    

    def addEdge(self,vertex1,vertex2):
      self.adjacencyList[vertex1].append(vertex2)
      self.adjacencyList[vertex2].append(vertex1)
      # print(self.adjacencyList)
      return self.adjacencyList
    
    def bfs(self,start):
      queue = []
      res = []
      visited = {}

      queue.append(start)
      visited[start] = True

      while len(queue)>0:
        currentVertex = queue.pop(0)
        res.append(currentVertex)

        for neighbor in self.adjacencyList[currentVertex]:
          if neighbor not in visited:
            visited[neighbor] = True
            queue.append(neighbor)
      print(self.adjacencyList)
      return res
    
    def dfsGraph(self,start):
        visited={}
        res = []

        def dfs(node):
        # curr = self.adjacencyList[start]
          visited[node] = True
          res.append(node)
          for neighbor in self.adjacencyList[node]:
            if neighbor not in visited:
              dfs(neighbor)
            
        dfs(start)
        return res
    
    def detectCycleBFS(self,start):
      q = []
      visited={}

      q.append([start,-1])
      visited[start] = True
      while q:
        node = q.pop(0)
        curr = node[0]
        parent = node[1]
        for neighbor in self.adjacencyList[curr]:
          if neighbor not in visited:
            visited[neighbor] = True
            q.append([neighbor,curr])
          #means the neighbor is already visited but its actually not the parent since its in the next node
          # only parent which is usually the first neighbor is already visited
          elif parent != neighbor:
             return True
             
      return False
       
    def detectCycleDFS(self,start):
      visited={}

      visited[start] = True

      def dfs(node,parent):
        visited[node] = True
        for neighbor in self.adjacencyList[node]:
          if neighbor not in visited:
            if dfs(neighbor,node) == True:
              return True
          elif parent != neighbor:
              return True
        return False
        
      return dfs(start,-1)
    

    def checkBipartiteBFS(self,colors, start):
      q = []
      q.append(start)
      colors[start] = 0

      while q:
        curr= q.pop(0)
        for neighbor in self.adjacencyList[curr]:
          if colors[neighbor]==-1:
            colors[neighbor] = 1 if colors[curr] == 0 else 0
            q.append(neighbor)
          elif colors[curr] == colors[neighbor]:
            return False
          
      return True
    

    def checkBipartiteDFS(self, colors, curr, currCol):
      colors[curr] = currCol

      for neighbor in self.adjacencyList[curr]:
        if colors[neighbor]==-1:
          colors[neighbor] = 1 if currCol == 0 else 0
          self.checkBipartiteDFS(colors, neighbor, colors[neighbor])
        elif currCol == colors[neighbor]:
          return False
      return True
    
    def isBipartite(self,start):
      colors={}
      for node in self.adjacencyList:
        colors[node] = -1

      return self.checkBipartiteDFS(colors, start, 0)
    


    def dfsCheck(self,curr, vis, pathVis):
      vis[curr] = 1
      pathVis[curr] = 1
      for neighbor in self.adjacencyList[curr]:
        if curr not in vis:
          if self.dfsCheck(neighbor, vis, pathVis) == True: return True
        elif pathVis[neighbor]: return True
      pathVis[curr] = 0
      return False
       
    def isCyclicDirectedGraph(self):
      list = [node for node in self.adjacencyList]
      vis = {}
      pathVis = {}
      for node in list:
        vis[node] = 0
        pathVis[node] = 0
      
      for node in list:
        if node not in vis:
          if self.dfsCheck(node, vis, pathVis) == True : return True

      return False
        

      


    

graph = Graph()

graph.addVertex('A')
graph.addVertex('B')
graph.addVertex('C')
graph.addVertex('D')
graph.addVertex('E')
graph.addVertex('F')

graph.addEdge('A','B')
graph.addEdge('A','C')
graph.addEdge('B','D')
graph.addEdge('C','E')
# graph.addEdge('D','E')
graph.addEdge('D','F')
graph.addEdge('E','F')

print(graph.bfs("A"))
print(graph.dfsGraph("A"))
print(graph.detectCycleBFS("A"))
print(graph.detectCycleDFS("A"))
print(graph.isBipartite("A"))
print(graph.isCyclicDirectedGraph())


  #     A
  #   /  \
  # B     C
  # |     |
  # D     E
  #  \   /
  #    F