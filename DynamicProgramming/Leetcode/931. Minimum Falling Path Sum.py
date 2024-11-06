#Memoization TC->O(nxn) , SC-> dp array O(nxn) + O(n)


class Solution:
  def minFallingPathSum(self, matrix: List[List[int]]) -> int:
    n = len(matrix)
    dp = [[float("inf") for _ in range(n)] for _ in range(n)]

    def rec(row,col):
      if row>=n or col<0 or col>=n: return float("inf")
      if row == n-1: return matrix[row][col]
      if dp[row][col]!=float("inf"): return dp[row][col]

      down_left = matrix[row][col] + rec(row+1,col-1)
      down = matrix[row][col] + rec(row+1,col)
      down_right = matrix[row][col] + rec(row+1, col+1)

      dp[row][col] = min(down_left, down, down_right)
      return dp[row][col]

    mini = float("inf")
    for i in range(n):
      curr = rec(0,i)
      mini = min(mini, curr)
    
    return mini



def minFallingPathSum(matrix):
  n = len(matrix)
  memo = [[-float('inf') for _ in range(n+1)] for _ in range(n+1)]
  def rec(row,col):
    if memo[row][col]!=-float('inf'): return memo[row][col]
    if row < 0 or col < 0 or col>=n: return float('inf')
    if row == 0: return matrix[row][col]

    first = matrix[row][col]+rec(row-1,col-1)
    second = matrix[row][col]+rec(row-1,col)
    third = matrix[row][col]+rec(row-1,col+1)
    # print(first,second,third)

    memo[row][col] = min(first,second,third)
    return memo[row][col]

  mini = float('inf')
  for c in range(n):
    mini = min(mini, rec(n-1,c))

  return mini



#Tabulation TC->O(nxn) , SC-> dp array O(nxn)
def minFallingPathSum2(matrix):
  n = len(matrix)
  dp = [[-float('inf') for _ in range(n)] for _ in range(n)]

  dp[0] = matrix[0]
  for row in range(1,n):
    for col in range(n):
      first = third = float('inf')
      if col > 0: first = matrix[row][col]+ dp [row-1][col-1]
      second = matrix[row][col] + dp[row-1][col]
      if col+1 < n: third = matrix[row][col] + dp[row-1][col+1]
      dp[row][col] = min(first,second,third)

  mini = float('inf')
  for c in range(n):
    mini = min(mini, dp[n-1][c])
  return mini



#Tabulation TC->O(nxn) , SC-> dp array O(n)
def minFallingPathSum3(matrix):
  n = len(matrix)
  prev_row = matrix[0]

  for r in range(1,n):
    curr = [0]*n
    for c in range(n):
      first = third = float('inf')
      if c > 0: first = matrix[r][c] + prev_row[c-1]
      second = matrix[r][c] + prev_row[c]
      if c+1 < n: third = matrix[r][c] + prev_row[c+1]
      curr[c] = min(first,second,third)
    prev_row = curr

  return min(prev_row)



# def minFallingPathSum(self, matrix: List[List[int]]) -> int:
#   n = len(matrix)
#   memo = [[-float('inf') for _ in range(n+1)] for _ in range(n+1)]

#   def rec(row,col):
#     if memo[row][col]!=-float('inf'): return memo[row][col]
#     if col >= n: return float('inf')
#     if row == n-1: return matrix[row][col]

#     first = matrix[row][col]+rec(row+1,col-1)
#     second = matrix[row][col]+rec(row+1,col)
#     third = matrix[row][col]+rec(row+1,col+1)

#     memo[row][col] = min(first,second,third)
#     return memo[row][col]

#   mini = float('inf')
#   for c in range(n):
#     mini = min(mini, rec(0,c))
#   return mini

        