from queue import PriorityQueue
from sortedcontainers import SortedList, SortedSet, SortedDict 

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
    print('edges:', u, v, 'parents:', ulp_u,ulp_v, rank, parent)

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
    print(ulp_u, ulp_v, size)



class Graph():
  def __init__(self, vertices):
    self.adj = {}
    self.V = vertices

  def addVertex(self, vertex):
      if vertex not in self.adj: 
        self.adj[vertex]=[]
      return self.adj

  def addEdge(self,vertex1,vertex2, weight):
    self.adj[vertex1].append([vertex2,weight])
    self.adj[vertex2].append([vertex1,weight])
    return self.adj
  
  def kruskals(self):
    adj = self.adj
    V = len(adj)
    edges = []
    # print(adj)
    for node in adj:
      for neighbor in adj[node]:
        adjNode = neighbor[0]
        wt = neighbor[1]
        edges.append([wt,node, adjNode])

    edges.sort()
    print(edges)
    mstWt = 0

    ds = DisjointSet(V)

    for edge in edges:
      wt, u, v = edge

      if ds.findUParent(u)!=ds.findUParent(v):
        mstWt+=wt
        ds.unionByRank(u,v)

    return mstWt






  

g = Graph(6)

# g.addVertex(0)
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addVertex(4)
g.addVertex(5)
g.addVertex(6)

g.addEdge(1, 4, 1)
g.addEdge(1, 2, 2)
g.addEdge(1, 5, 4)
g.addEdge(4, 5, 9)
g.addEdge(3, 4, 5)
g.addEdge(2, 4, 3)
g.addEdge(2, 3, 3)
g.addEdge(2, 6, 7)
g.addEdge(3, 6, 8)

# g.addEdge(0, 1, 4)
# g.addEdge(1, 2, 2)
# g.addEdge(2, 5, 5)
# g.addEdge(2, 3, 4)
# g.addEdge(1, 4, 1)
# g.addEdge(4, 3, 3)
# g.addEdge(3, 5, 1)


print(g.kruskals())

