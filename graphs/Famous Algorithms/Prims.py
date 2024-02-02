from queue import PriorityQueue
from sortedcontainers import SortedList, SortedSet, SortedDict 


class Graph():
  def prims(self, edges, n):
    adj = {i:[] for i in range(n)}
    for u,v,d in edges:
      adj[u].append([v,d])
      adj[v].append([u,d])

    vis= [0]*n
    mst = []
    sum = 0
    pq = PriorityQueue()
    pq.put((0,0,-1))

    while not pq.empty():
      wt, node, parent = pq.get()

      if vis[node]: continue
      vis[node]=1
      sum+=wt

      if parent != -1:
        mst.append([parent,node])

      for neighbor in adj[node]:
        nb = neighbor[0]
        nb_wt = neighbor[1]
        if not vis[nb]:
          pq.put((nb_wt, nb, node))

    print(sum)
    return mst
  

  

g = Graph()
edges = [[0,1,2], [0,2,1], [1,2,1], [2,4,2], [2,3,2], [3,4,1]]
print(g.prims(edges, 5))

