from bisect import bisect_left


nums = [10,9,2,5,3,7,101,18]

def lengthOfLIS(nums):
  n = len(nums)
  def rec(i, prev_i):
    if i == len(nums): return 0
    take = float("-inf")
    if prev_i == -1 or nums[prev_i]< nums[i]: 
      take = 1 + rec(i+1, i)

    not_take = 0+rec(i+1, prev_i)
    return max(take, not_take)
  
  return rec(0,-1)

nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))


'''
TC - NxN
SC - NxN + N(recursion stack space)
'''
def lengthOfLISMemo(nums):
  n = len(nums)
  dp = [[-1 for _ in range(n+1)] for _ in range(n)]

  def rec(i, prev_i):
    if i == len(nums): return 0
    if dp[i][prev_i+1]!=-1: return dp[i][prev_i+1]
    take = float("-inf")
    if prev_i == -1 or nums[prev_i]< nums[i]: 
      take = 1 + rec(i+1, i)

    not_take = 0+rec(i+1, prev_i)
    dp[i][prev_i+1] = max(take, not_take)
    return dp[i][prev_i+1]
  
  return rec(0,-1)

nums = [10,9,2,5,3,7,101,18]
print(lengthOfLISMemo(nums))


def lengthOfLTSTab(nums):
  n = len(nums)
  dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

  for i in range(n-1,-1,-1):
    for prev_i in range(i-1,-2,-1):
      not_take = dp[i+1][prev_i+1]

      take = float("-inf")
      if prev_i == -1 or nums[prev_i]< nums[i]: 
        take = 1 + dp[i+1][i+1]

      dp[i][prev_i+1] = max(take, not_take)

  return dp[0][0]

# print(lengthOfLTSTab(nums))


#space optimized O(N)
def lengthOfLISTab(nums) -> int:
  if not nums: return 0
  n = len(nums)
  dp = [1]*n

  for i in range(1,n):
    for prev in range(0,i):
      if nums[i]>nums[prev]: dp[i] = max(dp[i], dp[prev]+1)
  return max(dp)

nums = [10,9,2,5,3,7,101,18]
print(lengthOfLISTab(nums))


#binary search
def lengthOfLIS(nums) -> int:
  n = len(nums)
  sub = [nums[0]]
  for i in range(1,n):
    num = nums[i]
    if num>sub[-1]: sub.append(num)
    else:
      i = bisect_left(sub, num)
      sub[i] = num
  return len(sub)
  # sub = []
  # for num in nums:
  #   i = bisect_left(sub, num)
  #   # If num is greater than all elements in sub
  #   if i == len(sub): sub.append(num)
  #   # Otherwise, replace the first element in sub greater than or equal to num
  #   else: sub[i] = num
  # return len(sub)

#space optimized O(N)
def printLIS(nums) -> int:
  if not nums: return 0
  n = len(nums)
  dp = [1]*n
  hash = [i for i in range(n)]

  for i in range(1,n):
    for prev in range(0,i):
      if nums[i]>nums[prev]: 
        if dp[prev]+1 > dp[i]:
          dp[i] = dp[prev]+1
          hash[i] = prev
  
  maxi = max(dp)
  ans = -1
  lastIndex = -1
  
  for i in range(n):
    if dp[i] > ans:
      ans = dp[i]
      lastIndex = i

  temp = []
  while hash[lastIndex] != lastIndex: #till not reach the initialization value
    lastIndex = hash[lastIndex]
    temp.append(nums[lastIndex])

  temp.reverse()

  return temp

nums = [10,9,2,5,3,7,101,18]
print(printLIS(nums))