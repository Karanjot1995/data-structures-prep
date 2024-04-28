# brute force gived TLE
def uniquePaths(m: int, n: int):
  cnt = [0]
  def rec(row,col):
    if row == m-1 and col == n-1:
      cnt[0]+=1
    directions = [[1,0], [0,1]]
    for dr, dc in directions:
      r,c = row+dr, col+dc
      if r in range(m) and c in range(n):
        rec(r,c)

  rec(0,0)

  return cnt

print(uniquePaths(3,3))


#memoization TC->O(nxm) , SC-> path length O((n-1)+(m-1)) + dp array O(nxm)
def uniquePaths2(m: int, n: int):
  # memo = {}
  memo = [[-1 for _ in range(n+1)] for _ in range(m+1)]
  def rec(row,col):
    # if (row,col) in memo: return memo[(row,col)]
    if memo[row][col]!=-1: return memo[row][col]
    if row == m-1 and col == n-1:
      return 1
    if row >=m or col >=n: return 0
    
    right = rec(row,col+1)
    down = rec(row+1,col)
    memo[row][col] = right+down
    # memo[(row,col)]= right+down
    return right+down

  return rec(0,0)

print(uniquePaths2(3,3))



#Tabulation TC->O(nxm) , SC-> dp array O(nxm)
def uniquePaths3(m: int, n: int):
  dp = [[0 for _ in range(n)] for _ in range(m)]
  dp[0][0] = 1

  for r in range(0,m):
    for c in range(0,n):
      if r == 0 and c == 0: dp[0][0] = 1
      else:
        up = left = 0
        if r>0: up = dp[r-1][c]
        if c>0: left = dp[r][c-1]
        dp[r][c] =  up + left

  print(dp)
  return dp[m-1][n-1]

print(uniquePaths3(3,3))




#Tabulation space optimized TC->O(nxm) , SC-> O(1)
def uniquePaths4(m: int, n: int):
  # prev2 = [0 for _ in range(n)]
  prev_row = [0 for _ in range(n)]

  for r in range(0,m):
    curr = [0 for _ in range(n)]
    for c in range(0,n):
      if r == 0 and c == 0: curr[c] = 1
      else:
        curr[c] = prev_row[c] + curr[c-1]
    prev_row = curr

  return prev_row[n-1]

print(uniquePaths4(3,3))