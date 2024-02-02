from queue import PriorityQueue
from heapq import heapify, heappush, heappop

def findTheCity(n , edges, distanceThreshold):

  matrix = [[0 if i == j else float('inf') for i in range(n)] for j in range(n)]
  for e in edges:
    matrix[e[0]][e[1]] = e[2]
    matrix[e[1]][e[0]] = e[2]
  for k in range(n):
    for i in range(n):
      for j in range(n):
        if matrix[i][k] == float('inf') or matrix[k][j] == float('inf'):
          continue
        matrix[i][j] = min(matrix[i][j], (matrix[i][k]+matrix[k][j]))
  
  cntCity = n
  cityNo = -1
  for i in range(n):
    cnt=0
    for j in range(n):
      if matrix[i][j]<=distanceThreshold:
        cnt+=1
    if cnt<=cntCity:
      cntCity = cnt
      cityNo = i

  return cityNo


def findTheCityDijkstra(n, edges, distanceThreshold):
  adj = {i:[] for i in range(n)}
  for u,v,d in edges:
    adj[u].append([v,d])
    adj[v].append([u,d])

  cities=[0]*n
  def dijkstra(start,n):
    c = -1
    dist = [float('inf')]*n
    dist[start]=0
    visited=[0]*n

    pq = PriorityQueue()
    pq.put((0,start))

    while not pq.empty():
      curr_wt, curr = pq.get()      
      if curr_wt>distanceThreshold:
        break
      if visited[curr]:
        continue
      visited[curr]=1
      c +=1
      for neighbor in adj[curr]:
        nb = neighbor[0]
        nb_wt = neighbor[1]
        if visited[nb]==0 and curr_wt + nb_wt < dist[nb]:
          dist[nb]= curr_wt + nb_wt
          pq.put((dist[nb], nb))
    cities[start]= c
  
  for i in range(n):
      dijkstra(i,n)
      
  cntCity = n
  cityNo = -1
  for i in range(n):
    if cities[i]<=cntCity:
      cntCity = cities[i]
      cityNo = i
  return cityNo


n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4
# print(findTheCity(n, edges, distanceThreshold))
print(findTheCityDijkstra(n, edges, distanceThreshold))




def findTheCity(n: int, edges, distanceThreshold: int):
  adj={i:dict() for i in range(n)}
  for u,v,d in edges:
      adj[u][v]=d
      adj[v][u]=d
  cities=[0]*n
  for k in range(n):
      c=-1
      dist=[float('inf')]*n
      dist[k]=0
      visited=[0]*n
      pq=[(0,k)]
      heapify(pq)
      while pq:
          d,node=heappop(pq)
          if d>distanceThreshold:
              break
          if visited[node]:
              continue
          visited[node]=1
          c+=1
          for v in adj[node]:
              if visited[v]==0 and d+adj[node][v]<dist[v]:
                  dist[v]=d+adj[node][v]
                  heappush(pq,(dist[v],v))
      cities[k]=c
  maxNode=0
  minDist=cities[0]
  for i in range(n):
      if cities[i]<=minDist and maxNode<i:
          maxNode=i
          minDist=cities[i]
  return maxNode

print(findTheCity(n, edges, distanceThreshold))
