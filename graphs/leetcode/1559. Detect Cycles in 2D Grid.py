class Solution:
  def containsCycle(self, grid) -> bool:
    if not grid: return False
    rows, cols = len(grid), len(grid[0])
    vis = [[0 for _ in range(cols)] for _ in range(rows)]

    def dfs(row,col, p_row, p_col):

      vis[row][col] = 1
      directions = [[1,0], [-1,0], [0,1], [0,-1]]

      for dr,dc in directions:
        r,c = row+dr, col+dc
        if 0<=r<rows and 0<=c<cols:
          if not vis[r][c] and grid[r][c]==grid[row][col]:
            if dfs(r,c, row, col): return True
          # if neighbor is already visited but it is not the currents parent then there is cycle
          elif grid[r][c]==grid[row][col] and (r,c) != (p_row,p_col): 
            return True

      return False

    for r in range(rows):
      for c in range(cols):
        if not vis[r][c]:
          if dfs(r,c, r, c): return True

    return False