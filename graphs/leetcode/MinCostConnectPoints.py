from queue import PriorityQueue
import heapq

def minCostConnectPoints(points):
  n = len(points)
  min_cost = 0
  visited = [0] * n
  pq = PriorityQueue()
  #cost,vertex
  pq.put((0,0))
  while not pq.empty():
    cost, u = pq.get()
    if visited[u]:
      continue
    visited[u]=1
    min_cost+=cost

    for v in range(n):
      if not visited[v]:
        new_cost = abs(points[u][0]-points[v][0])+abs(points[u][1]-points[v][1])
        #pq puts lowest cost at top so we will have lowest dist to another vertex
        #higher dist will be added at the bottom of the PQ
        pq.put((new_cost,v))

  return min_cost

points = [[0,0],[2,2],[3,10],[5,2],[7,0]] #op =20
# points = [[3,12],[-2,5],[-4,1]]  #op = 18
print(minCostConnectPoints(points))



def minCostConnectPoints(self, points):
  n = len(points)
  min_cost = 0
  visited = [0] * n
  pq = [(0, 0)]  # Priority queue to store edges (cost, vertex/index)
  while pq:
    cost, u = heapq.heappop(pq)
    if visited[u]:
      continue
    visited[u]=1
    min_cost += cost

    for v in range(n):
      if not visited[v]:
        new_cost = abs(points[u][0]-points[v][0])+abs(points[u][1]-points[v][1])
        #pq puts lowest cost at top so we will have lowest dist to another vertex
        heapq.heappush(pq, (new_cost, v))

  return min_cost



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
    # return self.findUParent(self.parent[node])

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
    # print('edges:', u, v, 'parents:', ulp_u,ulp_v, rank, parent)

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
    # print(ulp_u, ulp_v, size)

class Solution:
  def minCostConnectPoints(self, points):
    V = len(points)

    edges = []
    for i in range(V):
      u = points[i]
      for j in range(V):
        v = points[j]
        if u != v :
          dist = abs(u[0]-v[0])+abs(u[1]-v[1])
          edges.append([dist,i,j])

    edges.sort()
    mstWt = 0
    # print(edges)
    ds = DisjointSet(V)
    for edge in edges:
      wt,u,v = edge

      if ds.findUParent(u)!=ds.findUParent(v):
        mstWt+=wt
        ds.unionByRank(u,v)
    return mstWt
  
      