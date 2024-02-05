def articulationPoint(n, adj):
  t_ins = [0]*n
  vis = [0]*n
  low = [0]*n
  mark = [0]*n
  timer = 1

  def dfs(u, parent, timer):
    vis[u] = 1
    t_ins[u] = low[u] = timer
    timer += 1
    child = 0

    for v in adj[u]:
      if v == parent: continue
      if not vis[v]:
        dfs(v, u, timer)
        low[u] = min(low[u], low[v])
        #if lowest time of nb is smaller or equal to the insertion time of node then it can reach the node else
        #if lowest time of neighbor is greater than time insertion of node then it cant reach back to it => bridge
        if low[v] >= t_ins[u] and parent!=-1:
          mark[u] = 1
        child+=1
      else:
        low[u] = min(low[u], t_ins[v])
    if child > 1 and parent == -1:
      mark[u] = 1

  for i in range(n):
    if not vis[i]:
      dfs(0,-1, timer)

  ans = []
  for i in range(n):
    if mark[i] ==1:
      ans.append(i)
  return ans if len(ans) else [-1]


adj = [[1], [0, 4], [4, 3], [4, 2], [1, 2, 3]]
print(articulationPoint(5,adj))