class Graph():
  def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int):
    costs = {}
    adj = {}
    for i in range(n):
      adj[i]=[]

    for i in range(len(flights)):
      adj[flights[i][0]].append([flights[i][1],flights[i][2]])

    for node in adj:
      costs[node] = float('inf')

    costs[src]=0
    q = [[0,src,0]]
    while q:
      print(q)
      # print(costs)
      stops, curr, cost = q.pop(0)
      if stops>k:
        break
      for neighbor in adj[curr]:
        nb, nb_cost = neighbor
        if cost+nb_cost < costs[nb] and stops<=k:
          costs[nb]= cost + nb_cost
          q.append([stops+1, nb, costs[nb]])

    print(costs)
    return -1 if costs[dst] == float('inf') else costs[dst]

    



g = Graph()

flights = [[0,1,100],[1,2,100],[2,0,200],[1,3,600],[2,3,200]]
print(g.findCheapestPrice(4,flights,0,3,1))