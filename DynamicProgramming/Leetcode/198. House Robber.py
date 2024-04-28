# Time Complexity: O(N) since we process at most N recursive calls, 
# Space Complexity: O(N)which is occupied by the cache and also by the recursion stack.


#memoization from right to left
def rob(nums) -> int:
  n = len(nums)
  dp = [-1]*(n+1)
  def rec(i):
    if dp[i]!=-1: return dp[i]
    if i == 0: return nums[i]
    if i < 0: return 0

    pick = nums[i] + rec(i-2)
    notPick = rec(i-1)
    op = max(pick, notPick)
    dp[i] = op
    return op
  
  return rec(n-1)

nums = [2,7,9,3,1]
print(rob(nums))
#op = 12 (2+9+1)


#memoization from left to right
def rob2(nums) -> int:
  n = len(nums)
  dp = [-1]*(n+1)

  def rec(i):
    if dp[i]!=-1: return dp[i]
    if i >= n: return 0
    if i == n-1: return nums[i]

    pick = nums[i] + rec(i+2)
    notPick = rec(i+1)
    op = max(pick, notPick)
    dp[i] = op
    return op
  
  return rec(0)

nums = [2,7,9,3,1]
print(rob2(nums))
#op = 12 (2+9+1)



#Tabulation
def rob3(nums) -> int:
  n = len(nums)
  dp = [-1]*(n+1)
  dp[0] = nums[0]

  for i in range(1,n):
    pick = nums[i]
    if i>1: pick = nums[i] + dp[i-2]
    notPick = dp[i-1]
    op = max(pick, notPick)
    dp[i] = op
  print(dp)
  return dp[n-1]


nums = [2,7,9,3,1]
print('Tabulation:', rob3(nums))
#op = 12 (2+9+1)



#Tabulation Space Optimized
def rob4(nums) -> int:
  n = len(nums)
  prev = nums[0]
  prev2 = nums[0]

  for i in range(1,n):
    pick = nums[i]
    if i>1: pick = nums[i] + prev2
    notPick = prev
    op = max(pick, notPick)
    prev2 = prev
    prev = op

  return prev


nums = [2,7,9,3,1]
print('Tabulation space optimized:', rob4(nums))
#op = 12 (2+9+1)