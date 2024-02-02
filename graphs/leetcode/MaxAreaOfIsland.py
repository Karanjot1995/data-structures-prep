def maxAreaOfIsland(grid):
  rows, cols = len(grid), len(grid[0])
  visited = [[0 for _ in range(cols)] for _ in range(rows)]
  maxArea = 0
  q = []

  def bfs(row,col):
    q.append([row,col])
    visited[row][col]=1
    area=1

    while q:
      row,col = q.pop(0)
      directions = [[1,0], [-1,0], [0,1], [0,-1]]

      for dr, dc in directions:
        r,c = row+dr, col+dc
        if r in range(rows) and c in range(cols) and grid[r][c]==1 and visited[r][c]!=1:
          q.append([r,c])
          visited[r][c]=1
          area+=1
    return area
  
  maxArea = 0
  for r in range(rows):
    for c in range(cols):
      if grid[r][c] == 1 and visited[r][c]!=1 :
        maxArea = max(maxArea, bfs(r,c))
     
  return maxArea

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(maxAreaOfIsland(grid))

# [0,0,1,0,0,0,0,1,0,0,0,0,0]
# [0,0,0,0,0,0,0,1,1,1,0,0,0]
# [0,1,1,0,1,0,0,0,0,0,0,0,0]
# [0,1,0,0,1,1,0,0,1,0,1,0,0]
# [0,1,0,0,1,1,0,0,1,1,1,0,0]
# [0,0,0,0,0,0,0,0,0,0,1,0,0]
# [0,0,0,0,0,0,0,1,1,1,0,0,0]
# [0,0,0,0,0,0,0,1,1,0,0,0,0]

