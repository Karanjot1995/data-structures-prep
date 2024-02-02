class Graph():

  def bellmanFord(self,edges,V,S):
    limit = 10**8
    dist = [limit]*V
    dist[S]=0
    print(edges)

    for _ in range(V):
      for node in edges:
        u,v,wt = node
        if dist[u] != limit and dist[u]+wt<dist[v]:
          dist[v] = dist[u]+wt

    for node in edges:
      u,v,wt = node
      if dist[u] != limit and dist[u]+wt<dist[v]:
          return [-1]

    return dist

g = Graph()


# arr,V, S = [[3,2,6],[5,3,1],[0,1,5],[1,5,-3],[1,2,-2],[3,4,-2],[2,4,3]], 5, 0
arr ,V, S=  [[0,1,5],[1,0,3],[1,2,-1],[2,0,1]], 3 ,2
print(g.bellmanFord(arr,V,S))

