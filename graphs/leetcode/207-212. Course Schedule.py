##########         Course Schedule      ############


#Topological Sort (Cycle detection) 
from collections import deque


class Solution:

  def hasCycle(self, node, vis, adj):
    vis[node] = 1
    for nb in adj[node]:
      if vis[nb]==-1:
        if self.hasCycle(nb, vis, adj): return True
      elif vis[nb]==1:
        return True
    vis[node]=0
    return False

  
  def canFinish(self, numCourses: int, prerequisites) -> bool:
    adj = [[] for _ in range(numCourses)]
    vis = [-1]*numCourses
    for pre in prerequisites:
      adj[pre[1]].append(pre[0])

    for i in range(numCourses):
      if vis[i]==-1:
        if self.hasCycle(i,vis,adj)==True: return False

    return True
    
  def canFinishBFS(self, numCourses: int, prerequisites) -> bool:
    adj = [[] for _ in range(numCourses)]
    indegree = [0]*numCourses
    vis = [-1]*numCourses
    nodesVisited = 0
    for pre in prerequisites:
      adj[pre[1]].append(pre[0])
      indegree[pre[0]]+=1

    q = deque()

    for i in range(numCourses):
      if indegree[i]==0:
        q.append(i)

    while q:
      node = q.popleft()
      nodesVisited+=1
      for nb in adj[node]:
        indegree[nb]-=1
        if indegree[nb]==0:
          q.append(nb)

    return nodesVisited == numCourses
    
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
  

    
