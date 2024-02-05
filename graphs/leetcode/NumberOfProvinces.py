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


def findCircleNumBFS(mat):
  def bfs(i,adj,visited):
      queue = []
      queue.append(i)
      visited[i] = True
      
      while queue:
          i = queue.pop(0)
          for j in range(n):
              if adj[i][j] == 1 and not visited[j]:
                  visited[j] = True
                  queue.append(j)
  n = len(mat)
  provinces = 0
  visited = [False]*n
  for i in range(n):
      if not visited[i]:
          provinces += 1
          bfs(i,mat,visited)
  return provinces


def findCircleNum(mat):
  n = len(mat)
  vis = [0]*n
  provinces = 0

  def dfs(i):
    vis[i]=1
    for j in range(n):
      if mat[i][j]==1 and not vis[j]:
        dfs(j)

  for i in range(n):
    if not vis[i]:
      provinces+=1
      dfs(i)
  return provinces


isConnected = [[1,1,0],[1,1,0],[0,0,1]]

print(findCircleNum(isConnected))
print(numProvincesDisjoint(isConnected))




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

       
