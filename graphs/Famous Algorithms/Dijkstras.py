from queue import PriorityQueue
from sortedcontainers import SortedList, SortedSet, SortedDict 


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
  
  def dijkstra(self,start):
    adj = self.adj
    n = len(adj)
    dist = [float('inf')]*n
    dist[start]=0

    pq = PriorityQueue()
    pq.put((0,start))
    # q = [[start,0]]
    while not pq.empty():
      # node = q.pop(0)
      node = pq.get()
      curr = node[1]
      curr_wt = node[0]
      for neighbor in adj[curr]:
        n = neighbor[0]
        n_wt = neighbor[1]
        if curr_wt + n_wt < dist[n]:
          dist[n]= curr_wt + n_wt
          # q.append([neighbor[0],dist[curr]+wt])
          pq.put((dist[n], n))
    return dist
  

  def dijkstraSet(self,start):
    adj = self.adj
    n = len(adj)
    dist = [float('inf')]*n
    dist[start]=0

    s = SortedSet()
    s.add((0,start))
    while s:
      # print(s)
      curr_wt,curr = s[0]
      s.remove((curr_wt,curr))
      for neighbor in adj[curr]:
        n = neighbor[0]
        n_wt = neighbor[1]
        if curr_wt + n_wt < dist[n]:
          dist[n]= curr_wt + n_wt
          s.add((dist[n], n))
    return dist
  
  def minimumEffortPath(self, heights):
    rows, cols = len(heights), len(heights[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    dist = [[float('inf') for _ in range(cols)] for _ in range(rows)]
    dist[0][0] = 0
    pq = PriorityQueue()
    pq.put((0,0,0))

    while not pq.empty():
      dis, r, c = pq.get()
      if r == rows - 1 and c == cols - 1:
        return dis
      for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if nr in range(rows) and nc in range(cols):
          new_dis = max(dis, abs(heights[r][c] - heights[nr][nc]))
          if new_dis < dist[nr][nc]:
            dist[nr][nc] = new_dis
            pq.put((new_dis, nr,nc))

  def shortestPath(self,n,m, edges):
    adj = self.adj
    dist = {}
    parent = {}
    for node in adj:
      dist[node] = float('inf')
      parent[node] = node

    dist[1]=0
    pq = PriorityQueue()
    pq.put((0,1))
    while not pq.empty():
      curr_wt, curr = pq.get()

      for neighbor in adj[curr]:
        nb = neighbor[0]
        n_wt = neighbor[1]
        if curr_wt + n_wt < dist[nb]:
          dist[nb]= curr_wt + n_wt
          parent[nb] = curr
          pq.put((dist[nb], nb))

    path = []
    node = n
    if dist[n] == float('inf'): return [-1]

    while parent[node]!=node:
      path.append(node)
      node = parent[node]

    path.append(1)
    path.reverse()
    return path
    # return dist


  def shortestPathBinaryMatrix(self, grid):
    if grid[0][0] == 1 or grid[-1][-1] ==1:
      return -1
    
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1,-1), (-1,1), (1,-1), (1,1)]

    dist = [[float('inf') for _ in range(cols)] for _ in range(rows)]
    dist[0][0] = 0
    q = [[0,0,0]]

    while q:
      dis, r, c = q.pop(0)
      if r == rows - 1 and c == cols - 1:
        break
      for dr, dc in directions:
        nr, nc = r + dr, c + dc
        new_dis = dis + 1
        if nr in range(rows) and nc in range(cols) and new_dis< dist[nr][nc] and grid[nr][nc] == 0:
          new_dis = dis + 1
          dist[nr][nc] = new_dis
          if nr == rows-1 and nc == cols-1:
            return new_dis+1
          q.append([new_dis, nr,nc])

    return dist[-1][-1]+1 if dist[-1][-1]+1 != float('inf') else -1
  
    

  

g = Graph(6)

# g.addVertex(0)
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addVertex(4)
g.addVertex(5)

# g.addEdge(0, 1, 4)
# g.addEdge(0, 2, 4)
# g.addEdge(1, 2, 2)
# g.addEdge(2, 3, 3)
# g.addEdge(2, 4, 1)
# g.addEdge(2, 5, 6)
# g.addEdge(3, 5, 2)
# g.addEdge(4, 5, 3)

g.addEdge(1, 2, 2)
g.addEdge(2, 5, 5)
g.addEdge(2, 3, 4)
g.addEdge(1, 4, 1)
g.addEdge(4, 3, 3)
g.addEdge(3, 5, 1)


# print(g.dijkstra(0))
# print(g.dijkstraSet(0))
print(g.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))

edges = [[1,2,2],[2,5,5],[2,3,4],[1,4,1],[4,3,3],[3,5,1]]
print(g.shortestPath(5,6,edges))

grid = [[0,0,0],[1,1,0],[1,1,0]]
# grid = [[0,0,0,0,1],[1,0,0,0,0],[0,1,0,1,0],[0,0,0,1,1],[0,0,0,1,0]]
print(g.shortestPathBinaryMatrix(grid))

