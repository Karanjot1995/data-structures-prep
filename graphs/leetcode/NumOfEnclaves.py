def numberOfEnclavesDFS(grid):
  rows, cols = len(grid), len(grid[0])
  visited = [[0 for _ in range(cols)] for _ in range(rows)]

  def dfs(row,col):
    visited[row][col] = 1
    directions = [[1,0], [-1,0], [0,1], [0,-1]]

    for dr, dc in directions:
      r,c = row+dr, col+dc
      if r in range(rows) and c in range(cols) and grid[r][c]==1 and visited[r][c]!=1:
        dfs(r,c)
  
  for r in range(rows):
    for c in range(cols):
      if (r == 0 or c == 0 or r == rows-1 or c == cols-1) and grid[r][c] == 1:
        dfs(r,c)


  # print(visited)
  lands = 0
  for r in range(rows):
    for c in range(cols): 
      if grid[r][c] == 1 and visited[r][c]!=1:
        lands+=1

  return lands



#bfs implementation
def numberOfEnclavesBFS(grid):
  rows, cols = len(grid), len(grid[0])
  visited = [[0 for _ in range(cols)] for _ in range(rows)]
  q = []

  for r in range(rows):
    for c in range(cols):
      if (r == 0 or c == 0 or r == rows-1 or c == cols-1) and grid[r][c] == 1:
        q.append([r,c])
        visited[r][c]=1

  while q:
    row,col = q.pop(0)
    directions = [[1,0], [-1,0], [0,1], [0,-1]]

    for dr, dc in directions:
      r,c = row+dr, col+dc
      if r in range(rows) and c in range(cols) and grid[r][c]==1 and visited[r][c]!=1:
        q.append([r,c])
        visited[r][c]=1

  lands = 0
  for r in range(rows):
    for c in range(cols): 
      if grid[r][c] == 1 and visited[r][c]!=1:
        lands+=1

  return lands


print(numberOfEnclavesBFS([[0,0,0,1],[0,1,1,0],[0,1,1,0],[0,0,0,1],[0,1,1,0]]))
# print(numberOfEnclaves(arr))
# 0 0 0 1
# 0 1 1 0
# 0 1 1 0
# 0 0 0 1
# 0 1 1 0

