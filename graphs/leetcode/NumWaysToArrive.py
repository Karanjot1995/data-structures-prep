from Templates.UndirectedWeighted import Graph
from queue import PriorityQueue
from sortedcontainers import SortedList, SortedSet, SortedDict 


class Graph(Graph):

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
  
  def countPaths(self, n, roads):
    adj = {}
    for i in range(n):
      adj[i]=[]

    for i in range(len(roads)):
      adj[roads[i][0]].append([roads[i][1],roads[i][2]])
      adj[roads[i][1]].append([roads[i][0],roads[i][2]])

    ways = [0]*n
    dist = [float('inf')]*n
    ways[0]=1
    dist[0]=0

    pq = PriorityQueue()
    pq.put((0,0))
    mod = 10**9+7
    while not pq.empty():
      curr_wt, curr = pq.get()
      for neighbor in adj[curr]:
        nb = neighbor[0]
        nb_wt = neighbor[1]
        if curr_wt + nb_wt < dist[nb]:
          ways[nb] = ways[curr]
          dist[nb]= curr_wt + nb_wt
          pq.put((dist[nb], nb))
        elif curr_wt + nb_wt == dist[nb]:
          ways[nb] = (ways[nb]+ways[curr])%mod

    return ways[n-1]%mod

g = Graph(6)


roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
print(g.countPaths(7, roads))

