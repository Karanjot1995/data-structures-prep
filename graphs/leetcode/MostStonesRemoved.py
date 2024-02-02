class DisjointSet():
  def __init__(self,n):
    self.rank = [0]*(n+1)
    self.parent = [i for i in range(n+1)]
    self.size = [1]*(n+1)
  
  def findUParent(self,node):
    if node == self.parent[node]:
      return node
    self.parent[node] = self.findUParent(self.parent[node])
    return self.parent[node]

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


def removeStones(stones):
  n=len(stones) # total no of stones
  #max no of rows and cols
  maxRow,maxCol = 0,0
  for i,j in stones:
    maxRow = max(maxRow,i)
    maxCol = max(maxCol,j)

  ds = DisjointSet(maxRow+maxCol+2)
  stoneNodes = {}
  for i,j in stones:
    row = i
    col = j+maxRow+1
    print(row,col)
    ds.unionBySize(row,col)
    stoneNodes[row] = 1
    stoneNodes[col] = 1

  print(stoneNodes)
  print(ds.parent)
  cnt = 0
  for node in stoneNodes:
    if ds.findUParent(node) == node:
      cnt+=1

  return n - cnt


# stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
stones = [[0,0],[0,2],[1,3],[3,0],[3,2],[4,3]]
print(removeStones(stones))

# 1 0 1 0
# 0 0 0 1
# 0 0 0 0
# 1 0 1 0
# 0 0 0 1
