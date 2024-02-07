##########         Course Schedule      ############


#Topological Sort (Cycle detection) 

class Solution:
#Course schedule 1
#detect cycle
    def canFinish(self, numCourses: int, prerequisites):
      graph=[[] for _ in range(numCourses)]
      vis=[-1]*numCourses
      for i,j in prerequisites:
        graph[j].append(i)

      def dfsCheck(curr):
        vis[curr] = 1
        for neighbor in graph[curr]:
          if vis[neighbor]==-1:
            if dfsCheck(neighbor) == True: return True
          elif vis[neighbor]==1: return True
        vis[curr] = 0
        return False
      
      for node in range(numCourses):
        if vis[node]==-1:
          if dfsCheck(node) == True: return False

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
      for node in range(numCourses):
        if in_degree[node]==0:
          q.append(node)

      while q:
        curr = q.pop(0)
        topo_sort.append(curr)
        for neighbor in graph[curr]:
          in_degree[neighbor]-=1
          if in_degree[neighbor]==0:
            q.append(neighbor)
    
      return topo_sort if len(topo_sort)==len(in_degree) else []
    

      
