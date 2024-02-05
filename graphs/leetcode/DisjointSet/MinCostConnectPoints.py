from DisjointSet import DisjointSet


def minCostConnectPoints(points):
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
  print(edges)
  mstWt = 0
  # print(edges)
  ds = DisjointSet(V)
  for edge in edges:
    wt,u,v = edge

    if ds.findUParent(u)!=ds.findUParent(v):
      mstWt+=wt
      ds.unionByRank(u,v)
  return mstWt


points = [[0,0],[2,2],[3,10],[5,2],[7,0]] #op =20
print(minCostConnectPoints(points))
  
      