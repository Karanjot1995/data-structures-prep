
#memoization TC->O(nxn) , SC-> dp array O(nxn)
def minimumTotal(triangle) -> int:
  n = len(triangle)
  dp = [[-1 for _ in range(n)] for _ in range(n)]

  def rec(row,col):
    if row == n-1: return triangle[row][col]
    if dp[row][col]!=-1: return dp[row][col]

    left = rec(row+1,col)
    right = rec(row+1, col+1)
    ans = triangle[row][col] + min(left,right)
    dp[row][col] = ans

    return ans

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


# #Tabulation TC->O(nxn) , SC-> dp array O(nxn)
# def minimumTotal2(triangle) -> int:
#   n = len(triangle)
#   dp = [[-1 for _ in range(n)] for _ in range(n)]

#   #last row
#   dp[n-1] = triangle[n-1]

#   memo = [[-1 for _ in range(n)] for _ in range(n)]
#   memo[0][0] = triangle[0][0]
#   for r in range(1,n):
#      for c in range(r+1):
#         up = updiag = float("inf")
#         if c >= 0: up = memo[r-1][c]
#         if c-1 >= 0: updiag = memo[r-1][c-1]
#         print(r,c,up, updiag)
#         memo[r][c] = triangle[r][c] + min(up, updiag)
#   print(memo)
        
#   # for r in range(n-2,-1,-1):
#   #   for c in range(r,-1,-1):
#   #       left = dp[r+1][c]
#   #       right = dp[r+1][c+1]
#   #       dp[r][c] = triangle[r][c]+min(left,right)

#   # return dp[0][0]

# trianglex = [[2],[3,4],[6,5,7],[4,1,8,3]]
# print(minimumTotal2(trianglex))




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

