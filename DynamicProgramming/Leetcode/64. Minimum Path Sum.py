
#memoization TC->O(nxm) , SC-> path length O((n-1)+(m-1)) + dp array O(nxm)
def minPathSum(grid):
  m = len(grid)
  n = len(grid[0])
  memo = [[-1 for _ in range(n+1)] for _ in range(m+1)]
  
  def rec(row,col):
    if memo[row][col]!=-1: return memo[row][col]
    if row == m-1 and col == n-1: return grid[row][col]
    if row >=m or col >=n: return float('inf')
    
    right = rec(row,col+1)
    down = rec(row+1,col)

    memo[row][col] = grid[row][col]+min(right,down)
    return grid[row][col]+min(right,down)
  
  return rec(0,0)


grid = [[1,3,1],[1,5,1],[4,2,1]]
print(minPathSum(grid))
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.





#memoization
def minPathSum(grid):
  m = len(grid)
  n = len(grid[0])
  memo = [[-1 for _ in range(n+1)] for _ in range(m+1)]
  
  def rec(row,col):
    if memo[row][col]!=-1: return memo[row][col]
    if row == 0 and col == 0: return grid[row][col]
    if row < 0 or col < 0: return float('inf')
    
    right = rec(row,col-1)
    down = rec(row-1,col)

    memo[row][col] = grid[row][col]+min(right,down)

    return grid[row][col]+min(right,down)
  
  return rec(m-1,n-1)


grid = [[1,3,1],[1,5,1],[4,2,1]]
print(minPathSum(grid))




#Tabulation TC->O(nxm) , SC-> dp array O(nxm)
def minPathSum2(grid) -> int:
  m = len(grid)
  n = len(grid[0])
  dp = [[-1 for _ in range(n)] for _ in range(m)]
  dp[0][0]=grid[0][0]

  for r in range(m):
    for c in range(n):
      if r == 0 and c == 0: dp[0][0] = grid[0][0]
      else:
        up = left = float('inf')
        if r>0: up = dp[r-1][c]
        if c>0: left = dp[r][c-1]
        dp[r][c] = grid[r][c]+ min(up,left)

  return dp[m-1][n-1]

print(minPathSum2(grid))


#Tabulation TC->O(nxm) , SC-> dp array O(n)
def minPathSum3(grid) -> int:
  m = len(grid)
  n = len(grid[0])
  prev_row = [0 for _ in range(n)]

  for r in range(0,m):
    curr = [0 for _ in range(n)]
    for c in range(0,n):
      if r == 0 and c == 0: curr[c] = grid[0][0]
      else:
        up = left = float('inf')
        if r>0: up = prev_row[c]
        if c>0: left =  curr[c-1]
        curr[c] = grid[r][c] + min(up,left)
    prev_row = curr

  return prev_row[n-1]

print(minPathSum3(grid))
