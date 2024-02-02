from queue import PriorityQueue

class Graph():
  def minimumMultiplications(self, arr, start, end):
    if start == end: return 0
    mod = 100000
    q = [[start,0]]
    dist=[float('inf')]*mod

    while q:
      curr, steps = q.pop(0)
      if curr == end:
        return steps
      for node in arr:
        mult = (curr*node)%mod
        if steps+1 < dist[mult]:
          dist[mult]=steps+1
          if mult == end: return steps+1
          q.append([mult,steps+1])
    return -1

g = Graph()

print(g.minimumMultiplications([2,5,7], 3, 30))