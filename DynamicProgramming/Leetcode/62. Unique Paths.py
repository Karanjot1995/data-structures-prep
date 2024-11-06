# brute force gave TLE (TC->2^(mxn))
def uniquePaths(m: int, n: int):
  def rec(row,col):
    if row > m-1 or col >n-1: return 0
    if row == m-1 and col == n-1:
      return 1
    dir = [[0,1], [1,0]]
    ans = 0
    for dr,dc in dir:
      r,c = row+dr, col+dc
      if 0<=r<m and 0<=c<n:
        ans += rec(r,c)
    return ans
  
  return rec(0,0)

print(uniquePaths(4,4))


# brute force gave TLE (TC->2^(mxn))
def uniquePathsx(m: int, n: int):
  dp = [[-1 for _ in range(m)] for _ in range(n)]
  def rec(row,col):
    if row >= m or col >= n: return 0
    if row == m-1 and col == n-1: return 1
    if dp[row][col] != -1: return dp[row][col]

    ans = 0
    right = rec(row,col+1)
    down = rec(row+1,col)
    ans = right+down
    # dir = [[0,1], [1,0]]
    # for dr,dc in dir:
    #   r,c = row+dr, col+dc
    #   if 0<=r<m and 0<=c<n:
    #     ans += rec(r,c)
    dp[row][col] = ans
    return ans
  
  return rec(0,0)

print('my way: ',uniquePathsx(4,4))












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

  for r in range(m):
    for c in range(n):
      if r == 0 and c == 0: continue
      else:
        up = left = 0
        if r>0: up = dp[r-1][c]
        if c>0: left = dp[r][c-1]
        dp[r][c] =  up + left

  print("tabulation: ",dp)
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