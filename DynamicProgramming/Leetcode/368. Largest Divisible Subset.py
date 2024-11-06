def largestDivisibleSubset(nums):
  nums.sort()
  n = len(nums)
  def rec(i, prev_i):
    if i == len(nums): return 0
    take = float("-inf")
    if prev_i == -1 or nums[prev_i]< nums[i] and (nums[prev_i]%nums[i]==0 or nums[i]%nums[prev_i]==0): 
      take = 1 + rec(i+1, i)

    not_take = 0+rec(i+1, prev_i)
    return max(take, not_take)
  
  return rec(0,-1)

nums = [16,4,7,8,1,9]
print(largestDivisibleSubset(nums))
# 1,4,8,16


def largestDivisibleSubsetTab(nums):
  nums.sort()
  return lis(nums)

def lis(nums):
  print(nums)
  if not nums: return 0
  n = len(nums)
  dp = [1]*n
  hash = [i for i in range(n)]

  for i in range(1,n):
    for prev in range(0,i):
      if nums[i]%nums[prev]==0: 
        if dp[prev]+1 > dp[i]:
          dp[i] = dp[prev]+1
          hash[i] = prev
  
  ans = -1
  lastIndex = -1
  
  for i in range(n):
    if dp[i] > ans:
      ans = dp[i]
      lastIndex = i

  temp = [nums[lastIndex]]
  while hash[lastIndex] != lastIndex: #till not reach the initialization value
    lastIndex = hash[lastIndex]
    temp.append(nums[lastIndex])

  temp.reverse()
  return temp

nums = [16,4,7,8,1,9]
print(largestDivisibleSubsetTab(nums))
