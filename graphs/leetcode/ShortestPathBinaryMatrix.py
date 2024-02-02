
def shortestPathBinaryMatrix(grid):
  if grid[0][0] == 1 or grid[-1][-1] ==1:
    return -1
  
  rows, cols = len(grid), len(grid[0])
  directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1,-1), (-1,1), (1,-1), (1,1)]

  dist = [[float('inf') for _ in range(cols)] for _ in range(rows)]
  dist[0][0] = 0
  q = [[0,0,0]]

  while q:
    dis, r, c = q.pop(0)
    if r == rows - 1 and c == cols - 1:
      break
    for dr, dc in directions:
      nr, nc = r + dr, c + dc
      new_dis = dis + 1
      if nr in range(rows) and nc in range(cols) and new_dis< dist[nr][nc] and grid[nr][nc] == 0:
        new_dis = dis + 1
        dist[nr][nc] = new_dis
        if nr == rows-1 and nc == cols-1:
          return new_dis+1
        q.append([new_dis, nr,nc])

  return dist[-1][-1]+1 if dist[-1][-1]+1 != float('inf') else -1

grid = [[0,0,0],[1,1,0],[1,1,0]]
# grid = [[0,0,0,0,1],[1,0,0,0,0],[0,1,0,1,0],[0,0,0,1,1],[0,0,0,1,0]]
print(shortestPathBinaryMatrix(grid))

  
