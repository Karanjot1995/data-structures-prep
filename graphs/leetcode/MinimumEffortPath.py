from queue import PriorityQueue

def minimumEffortPath(heights):
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

print(minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))
