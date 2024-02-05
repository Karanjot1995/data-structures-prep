
class DisjointSet():
  def __init__(self,n):
    self.rank = [0]*(n)
    self.parent = [i for i in range(n)]
    self.size = [1]*(n)
  
  def findUParent(self,node):
    if node == self.parent[node]:
      return node
    parent = self.parent[node] 
    return self.findUParent(parent)

  def unionByRank(self, u, v):
    rank = self.rank
    parent = self.parent

    ulp_u = self.findUParent(u)
    ulp_v = self.findUParent(v)
    
    if ulp_u == ulp_v: return 

    if(rank[ulp_u] < rank[ulp_v]):
      parent[ulp_u] = ulp_v
    elif(rank[ulp_u] > rank[ulp_v]):
      parent[ulp_v] = ulp_u
    else:
      parent[ulp_v] = ulp_u
      rank[ulp_u]+=1

  def unionBySize(self, u, v):
    size = self.size
    parent = self.parent
    ulp_u = self.findUParent(u)
    ulp_v = self.findUParent(v)
    if ulp_u == ulp_v: return 

    if(size[ulp_u] < size[ulp_v]):
      parent[ulp_u] = ulp_v
      size[ulp_v] += size[ulp_u]
    else:
      parent[ulp_v] = ulp_u
      size[ulp_u] += size[ulp_v]