def maxCoins(nums) -> int:  
  n = len(nums)
  nums.insert(0, 1)
  nums.append(1) # 1, 3, 1, 5, 8, 1
  def rec(i,j):
    if i > j: return 0
    max_coins = float("-inf")
    for k in range(i,j+1):
      tot_cost = nums[i-1]*nums[k]*nums[j+1] + (rec(i,k-1) + rec(k+1,j))
      max_coins = max(max_coins, tot_cost)
    return max_coins

  return rec(1,n)

nums = [3,1,5,8]
print(maxCoins(nums))


def maxCoinsMemo(nums) -> int:  
  n = len(nums)
  nums.insert(0, 1)
  nums.append(1) # 1, 3, 1, 5, 8, 1
  dp = [[-1 for _ in range(n+2)] for _ in range(n+2)]

  def rec(i,j):
    if i > j: return 0
    if dp[i][j]!=-1: return dp[i][j]
    max_coins = float("-inf")
    for k in range(i,j+1):
      tot_cost = nums[i-1]*nums[k]*nums[j+1] + (rec(i,k-1) + rec(k+1,j))
      max_coins = max(max_coins, tot_cost)
    dp[i][j] = max_coins
    return dp[i][j]

  return rec(1,n)

nums = [3,1,5,8]
print(maxCoins(nums))




def maxCoinsTab(nums) -> int:  
  n = len(nums)
  nums.insert(0, 1)
  nums.append(1) # 1, 3, 1, 5, 8, 1
  dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

  for i in range(n,0,-1):
    for j in range(1,n+1):
      if i>j: continue
      max_coins = float("-inf")
      for k in range(i,j+1):
        tot_cost = nums[i-1]*nums[k]*nums[j+1] + dp[i][k-1] + dp[k+1][j]
        max_coins = max(max_coins, tot_cost)
      dp[i][j] = max_coins

  return dp[1][n]

nums = [3,1,5,8]
print(maxCoinsTab(nums))