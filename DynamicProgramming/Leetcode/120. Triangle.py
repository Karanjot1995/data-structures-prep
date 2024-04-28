
#memoization TC->O(nxn) , SC-> dp array O(nxn)
def minimumTotal(triangle) -> int:
  n = len(triangle)
  # dp = {}
  dp = [[-1 for _ in range(n)] for _ in range(n)]
  def rec(r,c):
    # if (r,c) in dp: return dp[(r,c)]
    if dp[r][c]!=-1: return dp[r][c]
    if r == n-1: return triangle[r][c]

    left = triangle[r][c]+rec(r+1,c)
    right = triangle[r][c]+rec(r+1,c+1)
    dp[r][c] = min(left,right)
    # dp[(r,c)] = min(left,right)
    return min(left,right)

  return rec(0,0)

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(minimumTotal(triangle))
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).



#Tabulation TC->O(nxn) , SC-> dp array O(nxn)
def minimumTotal2(triangle) -> int:
  n = len(triangle)
  dp = [[-1 for _ in range(n)] for _ in range(n)]

  #last row
  dp[n-1] = triangle[n-1]

  for r in range(n-2,-1,-1):
    for c in range(r,-1,-1):
        left = dp[r+1][c]
        right = dp[r+1][c+1]
        dp[r][c] = triangle[r][c]+min(left,right)

  return dp[0][0]

print(minimumTotal2(triangle))




#Tabulation TC->O(nxn) , SC-> dp array O(n)
def minimumTotal3(triangle) -> int:
  n = len(triangle)
  front = triangle[n-1]

  for r in range(n-2,-1,-1):
    curr = [0]*(r+1)
    for c in range(r,-1,-1):
        left = triangle[r][c]+front[c]
        right = triangle[r][c]+front[c+1]
        curr[c] = min(left,right)
    front = curr

  return front[0]


triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(minimumTotal3(triangle))

