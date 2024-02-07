from queue import PriorityQueue
def swimInWater(grid):
  rows, cols = len(grid), len(grid[0])
  directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

  dist = [[float('inf') for _ in range(cols)] for _ in range(rows)]
  dist[0][0] = grid[0][0]

  pq = PriorityQueue()
  pq.put((grid[0][0],0,0))

  while not pq.empty():
    dis, r, c = pq.get()
    if r == rows - 1 and c == cols - 1:
      return dis
    for dr, dc in directions:
      nr, nc = r + dr, c + dc
      if nr in range(rows) and nc in range(cols):
        new_dis = max(dis, grid[nr][nc])
        if new_dis < dist[nr][nc]:
          dist[nr][nc] = new_dis
          pq.put((new_dis, nr,nc))
    print(dis, dist)

grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
print(swimInWater(grid))