from Templates.DisjointSet import DisjointSet

def numProvincesDisjoint(mat):
  V = len(mat)
  ds = DisjointSet(V)
  for u in range(V):
    for v in range(V):
      if mat[u][v]==1:
        ds.unionByRank(u,v)
  
  return len(set(ds.parent[i] for i in range(V)))
  # OR
  cnt = 0
  for i in range(V):
    #if it is the parent of itself then its the ultimate parent/boss of the component
    # so increase the count by 1
    if ds.parent[i] == i: cnt+=1

  return cnt

