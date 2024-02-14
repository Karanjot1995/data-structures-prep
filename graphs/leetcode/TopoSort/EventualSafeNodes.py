
############       Eventual Safe Nodes       ############

def eventualSafeNodes(graph):
  q=[]
  in_degree = [0]*len(graph)
  revAdj = {}
  safe_nodes = set()

  for i in range(len(graph)):
    nbr_cnt = 0
    for j in graph[i]:
      nbr_cnt+=1
      revAdj[j].append(i)
      in_degree[i]+=1
    if nbr_cnt==0:
      safe_nodes.add(i)

  q = []
  for node in revAdj:
    if in_degree[node]==0:
      q.append(node)
  
  while q:
    curr = q.pop(0)
    safe_nodes.add(curr)
    for neighbor in revAdj[curr]:
      in_degree[neighbor]-=1
      if in_degree[neighbor]==0:
        q.append(neighbor)

  safe_nodes = list(safe_nodes)
  safe_nodes.sort()
  return safe_nodes


def eventualSafeNodesDFS(graph):
  check = {}
  vis = {}
  
  for node in range(len(graph)):
    check[node]=0
    vis[node] = -1

  def dfs(curr):
    vis[curr] = 1
    for neighbor in graph[curr]:
      if vis[neighbor]==-1:
        if dfs(neighbor) == True: return True
      elif vis[neighbor]==1: return True
    vis[curr]=0
    check[curr]=1
    return False
  
  for node in range(len(graph)):
    if vis[node]==-1:
      dfs(node)

  safeNodes = []
  for node in check:
    if check[node] == 1:
      safeNodes.append(node)

  return safeNodes
        