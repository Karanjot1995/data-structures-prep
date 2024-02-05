def findRedundantConnection(edges):
  n = len(edges)
  parent = [i for i in range(n+1)]
  rank = [0]*(n+1)

  def uparent(node):
    if node == parent[node]:
      return node
    parent[node] = uparent(parent[node])
    return parent[node]
  
  def union(u,v):
    ulp_u = uparent(u)
    ulp_v = uparent(v)
    if ulp_u == ulp_v: return False

    if(rank[ulp_u] < rank[ulp_v]):
      parent[ulp_u] = ulp_v
    elif(rank[ulp_u] > rank[ulp_v]):
      parent[ulp_v] = ulp_u
    else:
      parent[ulp_v] = ulp_u
      rank[ulp_u]+=1
    return True

  for u,v in edges:
    if not union(u,v):
      return [u,v]
    
# edges = [[1,2],[1,3],[2,3]]
edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
print(findRedundantConnection(edges))
# Output: [2,3]
# Output: [1,4]