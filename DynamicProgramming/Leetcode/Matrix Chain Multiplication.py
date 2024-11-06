'''
Rules:
Start with entire block/ array (f(i,j))
Try all partitions: Run a loop to try all partitions
Return the best possible 2 partitions

              ABCD
    (AB)(CD)    A(BCD)    (ABC)D

'''

nums = [10,20,30,40,50]

# start with: 10, 20    30,40,50
#                 i            j

#TC - exponential
def matrixMultiplication(nums):
  n = len(nums)
  def rec(i,j):
    if i == j: return 0
    mini = float("inf")

    for k in range(i,j):
      # (10 x 20 )x 50 + steps between 20-50
      steps = (nums[i-1] * nums[k] * nums[j]) + (rec(i,k) + rec(k+1,j))
      mini = min(mini, steps)
    return mini


  return rec(1,n-1)

print(matrixMultiplication(nums))



#TC - NxNx N(internal loop)
#SC - NxN + N(stack space)
def matrixMultiplicationMemo(nums):
  n = len(nums)
  dp = [[-1 for _ in range(n)] for _ in range(n)]
  def rec(i,j):
    if i == j: return 0
    mini = float("inf")
    if dp[i][j]!=-1: return dp[i][j]
    for k in range(i,j):
      # (10 x 20 )x 50 + steps between 20-50
      steps = (nums[i-1] * nums[k] * nums[j]) + (rec(i,k) + rec(k+1,j))
      mini = min(mini, steps)
    dp[i][j] = mini
    return dp[i][j]


  ans = rec(1,n-1)
  print(dp)
  return ans


print(matrixMultiplicationMemo(nums))



#TC - NxNx N(internal loop)
#SC - NxN
def matrixMultiplicationTab(nums):
  n = len(nums)
  dp = [[-1 for _ in range(n)] for _ in range(n)]
  for i in range(n): dp[i][i] = 0

  for i in range(n-1,0,-1):
    for j in range(i+1,n):
      mini = float("inf")
      for k in range(i,j):
        # (10 x 20 )x 50 + steps between 20-50
        steps = (nums[i-1] * nums[k] * nums[j]) + dp[i][k] + dp[k+1][j]
        mini = min(mini, steps)
      dp[i][j] = mini

  return dp[1][n-1]

nums = [10,20,30,40,50]

print(matrixMultiplicationTab(nums))

#  0 0 0
#  0 0 0
#  0 0 0