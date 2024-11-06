#space optimized O(N)
def findNumberOfLIS(nums) -> int:
  if not nums: return 0
  n = len(nums)
  dp = [1]*n
  count = [1]*n

  maxi = 1
  for i in range(1,n):
    for prev in range(0,i):
      if nums[i]>nums[prev] and dp[prev]+1 > dp[i]:
        dp[i] = dp[prev]+1
        count[i] = count[prev]
      elif nums[i]>nums[prev] and dp[prev]+1 == dp[i]:
        count[i] += count[prev]
      maxi = max(maxi, dp[i])

  cnt = 0
  for i in range(n):
    if dp[i]==maxi: cnt += count[i]

  return cnt

nums = [1,3,5,4,7]
print(findNumberOfLIS(nums))