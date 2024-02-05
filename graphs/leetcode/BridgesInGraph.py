def criticalConnections(n, connections):
  adj = [[] for _ in range(n)]

  for u,v in connections:
    adj[u].append(v)
    adj[v].append(u)

  t_ins = [0]*n
  vis = [0]*n
  low = [0]*n
  timer = 1
  bridges = []


  def dfs(u, parent, timer):
    vis[u] = 1
    print(timer, u, parent)
    t_ins[u] = low[u] = timer
    timer += 1

    for v in adj[u]:
      if v == parent: continue
      if not vis[v]:
        dfs(v, u, timer)
        #if lowest time of neighbor is greater than time insertion of node then it cant reach back to it
        if low[v] > t_ins[u]:
          bridges.append([u,v])
      low[u] = min(low[u], low[v])

  dfs(0,-1, timer)
  return bridges


connections = [[0,1],[1,2],[2,0],[1,3]]
print(criticalConnections(4,connections))