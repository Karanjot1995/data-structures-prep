def numEnclaves(grid):
  rows, cols = len(grid), len(grid[0])
  vis = set()
  q = []

  #dfs implementation
  def dfs(row,col):
    vis.add((row,col))
    directions = directions = [[1,0], [-1,0], [0,1], [0,-1]]
    for dr, dc in directions:
      r,c = row+dr, col+dc
      if r in range(rows) and c in range(cols) and (r,c) not in vis and grid[r][c]==1:
        dfs(r,c)

  #bfs implementation
  def bfs(r,c):
    q.append([r,c])
    vis.add((r,c))
    while q:
      row,col = q.pop(0)
      directions = directions = [[1,0], [-1,0], [0,1], [0,-1]]
      for dr, dc in directions:
        r,c = row+dr, col+dc
        if r in range(rows) and c in range(cols) and (r,c) not in vis and grid[r][c]==1:
          q.append([r,c])
          vis.add((r,c))

  for r in range(rows):
    for c in range(cols):
      if (r == 0 or r == rows-1 or c == 0 or c == cols-1) and grid[r][c]==1:
        # dfs(r,c)
        bfs(r,c)

  cnt = 0
  for r in range(rows):
    for c in range(cols):
      if grid[r][c] == 1 and (r,c) not in vis:
        cnt+=1
  return cnt


print(numEnclaves([[0,0,0,1],[0,1,1,0],[0,1,1,0],[0,0,0,1],[0,1,1,0]]))
# print(numberOfEnclaves(arr))
# 0 0 0 1
# 0 1 1 0
# 0 1 1 0
# 0 0 0 1
# 0 1 1 0

