from queue import PriorityQueue

# TC - > Elog(V)
class Solution:
  def minimumEffortPath(self, heights) -> int:
    rows = len(heights)
    cols = len(heights[0])

    distances = [[float('inf') for _ in range(cols)] for _ in range(rows)]
    distances[0][0] = 0

    pq = PriorityQueue()
    pq.put((0,0,0))

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while not pq.empty():
      dis, r,c = pq.get()
      if r==rows-1 and c==cols-1:
        return dis
      for dr,dc in directions:
        nr, nc = r+dr, c+dc
        if 0<=nr<rows and 0<=nc<cols:
          abs_diff = max(dis, abs(heights[r][c] - heights[nr][nc]))
          if abs_diff < distances[nr][nc]:
            distances[nr][nc] = abs_diff
            pq.put((abs_diff, nr, nc)) 
