'''
Time complexity: O(m+n)
Space complexity: O(n)
'''


class Solution:
  # def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
  #   n = len(graph)
  #   revAdj = [[] for i in range(n)]
  #   safeNodes = set()
  #   in_degree = [0]*n
  #   for i in range(n):
  #     nb_cnt = 0
  #     for j in graph[i]:
  #       revAdj[j].append(i)
  #       in_degree[i]+=1
  #       nb_cnt+=1
  #     if nb_cnt==0:
  #       safeNodes.add(i)

  #   q = []
  #   for node in range(n):
  #     if in_degree[node]==0:
  #       q.append(node)

  #   while q:
  #     u = q.pop(0)
  #     safeNodes.add(u)
  #     for v in revAdj[u]:
  #       in_degree[v]-=1
  #       if in_degree[v]==0:
  #         q.append(v)
    
  #   safeNodes = list(safeNodes)
  #   safeNodes.sort()
  #   return safeNodes
      
  def eventualSafeNodes(self, graph):
    n = len(graph)
    vis = [-1]*n
    check = [0]*n
    def detectCycle(u):
      vis[u]=1
      for v in graph[u]:
        if vis[v]==-1:
          if detectCycle(v)==True: return True
        elif vis[v]==1: return True
      vis[u]=0
      check[u]=1
      return False
    
    for node in range(n):
      if vis[node]==-1:
        detectCycle(node)
    safeNodes = []

    for node in range(n):
      if check[node]:
        safeNodes.append(node)


    return safeNodes


