#memoization TC-> O(nxmxm)x9, SC-> O(nxmxm) + O(n)
def cherryPickup(grid) -> int:
  m = len(grid)
  n = len(grid[0])
  memo = [[[-1 for _ in range(n)] for _ in range(n)] for _ in range(m)]

  def rec(r,c1,c2):
    if (c1<0 or c1>=n or c2<0 or c2>=n): return -float('inf')
    if r == m-1:
      if c1 == c2: return grid[r][c1]
      else: return grid[r][c1] + grid[r][c2]
    if memo[r][c1][c2]!=-1: return memo[r][c1][c2]

    maxi = 0
    for dc1 in (-1,0,1):
      for dc2 in (-1,0,1):
        if c1 == c2: maxi = max(maxi,grid[r][c1] + rec(r+1,c1+dc1,c2+dc2))
        else: maxi = max(maxi, grid[r][c1] + grid[r][c2] + rec(r+1,c1+dc1,c2+dc2))
    memo[r][c1][c2] = maxi
    return maxi

  ans = rec(0,0,n-1)
  print(memo)
  return ans

grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
print(cherryPickup(grid))


#tabulation
def cherryPickup2(grid) -> int:
  m = len(grid)
  n = len(grid[0])
  dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(m)]
  # print(memo)


  for c1 in range(n):
    for c2 in range(n):
      if c1 == c2: dp[m-1][c1][c2] = grid[m-1][c1]
      else: dp[m-1][c1][c2] = grid[m-1][c1] +  grid[m-1][c2]

  for r in range(m-2,-1,-1):
    for c1 in range(n):
      for c2 in range(n):
        maxi = -float('inf')
        for dc1 in (-1,0,1):
          for dc2 in (-1,0,1):
            val = 0
            if c1 == c2: val = grid[r][c1]
            else: val = grid[r][c1] + grid[r][c2]
            if c1+dc1>=0 and c1+dc1<n and c2+dc2>=0 and c2+dc2<n: val += dp[r+1][c1+dc1][c2+dc2]
            else: val = -float('inf')
            maxi = max(val,maxi)
        dp[r][c1][c2] = maxi

  return dp[0][0][n-1]

print(cherryPickup2(grid))


# Output: 24
# Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
# Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
# Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
# Total of cherries: 12 + 12 = 24.