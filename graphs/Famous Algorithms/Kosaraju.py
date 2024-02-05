def stronglyConnectedComponents(adj,start):
  V = len(adj)
  times = []
  visited = [0]*V

  def dfs(curr):
    visited[curr]=1
    for neighbor in adj[curr]:
      if not visited[neighbor]:
        dfs(neighbor)
    times.append(curr)

  for i in range(V):
    if not visited[i]:
      dfs(i)

  revAdj = [[] for _ in range(V)]

  for i in range(V):
    visited[i] = 0
    for j in adj[i]:
      revAdj[j].append(i)

  components = 0

  def dfs2(curr):
    visited[curr]=1
    for neighbor in revAdj[curr]:
      if not visited[neighbor]:
        dfs2(neighbor)

  while times:
    curr = times.pop()
    if not visited[curr]:
      components+=1
      dfs2(curr)

  return components



adj = [[2, 3], [0], [1], [4], []]
print(stronglyConnectedComponents(adj,0))