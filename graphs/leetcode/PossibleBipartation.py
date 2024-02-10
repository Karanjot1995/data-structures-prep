def possibleBipartition(n, dislikes) -> bool:
  adj = {}
  vis = {}
  for i in range(1,n+1):
    adj[i] = []
    vis[i] = -1

  for u,v in dislikes:
    adj[u].append(v)
    adj[v].append(u)

  def dfs(curr, currCol):
    vis[curr] = currCol
    for nb in adj[curr]:
      if vis[nb]==-1:
        oppCol = 0
        if currCol == 0: oppCol = 1
        if dfs(nb, oppCol) == False: return False
      elif vis[nb]==vis[curr]:
        return False
    return True

  for i in range(1,n+1):
    if vis[i]==-1:
      if dfs(i,0) == False:
        return False
  
  return True

n=8
dislikes = [[1,2],[1,3],[4,5],[4,6],[3,5],[3,7],[5,7]]
print(possibleBipartition(n,dislikes))