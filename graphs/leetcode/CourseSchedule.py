##########         Course Schedule      ############

class Solution:
#Course schedule 1
    def dfsCheck(self,graph, curr, vis):
      vis[curr] = 1
      for neighbor in graph[curr]:
        if vis[neighbor]==-1:
          if self.dfsCheck(graph, neighbor, vis) == True: return True
        elif vis[neighbor]==1: return True
      vis[curr] = 0
      return False

    def canFinish(self, numCourses: int, prerequisites):
      graph=[[] for _ in range(numCourses)]
      vis=[-1]*numCourses
      for i,j in prerequisites:
        graph[j].append(i)
      
      for node in range(numCourses):
        if vis[node]==-1:
          if self.dfsCheck(graph, node, vis) == True: return False

      return True
    
#Course schedule 2
    def findOrder(self, numCourses: int, prerequisites):
      graph=[[] for _ in range(numCourses)]
      vis=[-1]*numCourses
      s = []
      for i,j in prerequisites:
        graph[j].append(i)

      print(graph)
      def dfs(curr):
        vis[curr] = 1
        for neighbor in graph[curr]:
          if vis[neighbor]==-1:
            if dfs(neighbor) == True: return True
          elif vis[neighbor]==1: return True
        vis[curr] = 0
        s.append(curr)
        return False

      for node in range(numCourses):
        if vis[node]==-1:
          if dfs(node) == True: return []

      s.reverse()
      return s

    ######     OR     ######

    def findOrder(self, numCourses: int, prerequisites):
      graph=[[] for _ in range(numCourses)]
      in_degree = [0]*len(graph)

      for i,j in prerequisites:
        graph[j].append(i)
        in_degree[i]+=1 

      q = []
      topo_sort = []
      for i in range(len(in_degree)):
        if in_degree[i]==0:
          q.append(i)

      while q:
        curr = q.pop(0)
        topo_sort.append(curr)
        for neighbor in graph[curr]:
          in_degree[neighbor]-=1
          if in_degree[neighbor]==0:
            q.append(neighbor)
    
      return topo_sort if len(topo_sort)==len(in_degree) else []
    

      
