def countDistinctIslands(grid):
  rows, cols = len(grid), len(grid[0])
  visited = [[0 for _ in range(cols)] for _ in range(rows)]
  islands = []

  #take initial row and column in dfs to be subtracted
  def dfs(row,col, island, row0, col0):
    island.append([row-row0,col-col0])
    print(island)
    visited[row][col] = 1
    directions = [[1,0], [-1,0], [0,1], [0,-1]]

    for dr, dc in directions:
      r,c = row+dr, col+dc
      if r in range(rows) and c in range(cols) and grid[r][c]==1 and visited[r][c]!=1:
        dfs(r,c, island, row0, col0)
  
  for r in range(rows):
    for c in range(cols):
      if grid[r][c] == 1 and visited[r][c]!=1 :
        island = []
        dfs(r,c, island, r, c)
        if island not in islands:
          islands.append(island)

  return len(islands)

print(countDistinctIslands([[1,1,0,1,1],[1,0,0,0,0],[0,0,0,1,1],[1,1,0,1,0]]))
# print(numberOfEnclaves(arr))
# 1 1 0 1 1
# 1 0 0 0 0
# 0 0 0 1 1
# 1 1 0 1 0


