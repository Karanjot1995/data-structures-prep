class Solution:
  def numDistinctIslands2(self, grid) -> int:
    rows, cols = len(grid), len(grid[0])
    visited = [[0 for _ in range(cols)] for _ in range(rows)]
    islands = set()

    def dfs(row,col, island):
      island.append([row,col])
      visited[row][col] = 1
      directions = [[1,0], [-1,0], [0,1], [0,-1]]

      for dr, dc in directions:
        r,c = row+dr, col+dc
        if r in range(rows) and c in range(cols) and grid[r][c]==1 and visited[r][c]!=1:
          dfs(r,c,island)

    
    def rotations(island):
      shapes = []
      for i, j in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        # Reflection
        shape = sorted([(x * i, y * j) for x, y in island])
        shape = [(x - shape[0][0], y - shape[0][1]) for x, y in shape]
        shapes.append(shape)

        # Rotations
        shape = sorted([(y * i, x * j) for x, y in island])
        shape = [(x - shape[0][0], y - shape[0][1]) for x, y in shape]
        shapes.append(shape)  
      return min(shapes)

    
    for r in range(rows):
      for c in range(cols):
        if grid[r][c] == 1 and visited[r][c]!=1 :
          island = []
          dfs(r,c,island)
          islands.add(tuple(rotations(island)))
    
    return len(islands)
        