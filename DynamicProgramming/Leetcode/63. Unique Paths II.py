#memoization
def uniquePathsWithObstacles(obstacleGrid) -> int:
  m = len(obstacleGrid)
  n = len(obstacleGrid[0])
  if obstacleGrid[m-1][n-1] == 1: return 0
  memo = [[-1 for _ in range(n+1)] for _ in range(m+1)]

  def rec(row,col):
    if memo[row][col]!=-1: return memo[row][col]
    if row == m-1 and col == n-1: return 1

    if row >= m or col >=n or obstacleGrid[row][col]==1: return 0
    
    right = rec(row,col+1)
    down = rec(row+1,col)
    memo[row][col] = right+down
    return right+down

  return rec(0,0)        

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print("first: ",uniquePathsWithObstacles(obstacleGrid))



#tabulation
def uniquePathsWithObstacles2(obstacleGrid) -> int:
  m = len(obstacleGrid)
  n = len(obstacleGrid[0])
  if obstacleGrid[m-1][n-1] == 1: return 0
  if obstacleGrid[0][0] == 1: return 0

  dp = [[0 for _ in range(n)] for _ in range(m)]
  dp[0][0] = 1

  for r in range(m):
    for c in range(n):
      if r == 0 and c == 0: continue
      else:
        up = left = 0
        if obstacleGrid[r][c] == 0:
          if r>0: up = dp[r-1][c]
          if c>0: left = dp [r][c-1]
        dp[r][c] = up + left
  return dp[m-1][n-1]

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(uniquePathsWithObstacles2(obstacleGrid))

