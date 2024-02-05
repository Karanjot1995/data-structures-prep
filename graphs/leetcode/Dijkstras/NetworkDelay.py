from queue import PriorityQueue

# You are given a network of n nodes, labeled from 1 to n. You are also given times, 
# a list of travel times as directed edges times[i] = (ui, vi, wi), 
# where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
# We will send a signal from a given node k. Return the minimum time it takes 
# for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.
  
def networkDelayTime(times , n: int, k: int):
  adj=[[] for _ in range(n+1)]
  for u, v, wt in times:
    adj[u].append([v,wt])

  dist = [float('inf')]*(n+1)
  dist[0] = 0
  dist[k] = 0
  vis = set()
  pq = PriorityQueue()
  pq.put((0,k))
  while not pq.empty():
    wt, u = pq.get()
    vis.add(u)
    if len(vis)==n:
      return max(dist)
    for neighbor in adj[u]:
      nb, nb_wt = neighbor
      if nb not in vis and wt + nb_wt < dist[nb]:
        dist[nb] = wt + nb_wt
        pq.put((dist[nb],nb))

  return -1

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
print(networkDelayTime(times,n,k))

#op = 2