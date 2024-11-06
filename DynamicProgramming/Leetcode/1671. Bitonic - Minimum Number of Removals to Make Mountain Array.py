def minimumMountainRemovals(nums):
  if not nums: return 0
  n = len(nums)
  dp1 = [1]*n

  nums2 = nums[::-1]
  dp2 = [1]*n

  for i in range(1,n):
    for prev in range(0,i):
      if nums[i]>nums[prev]: dp1[i] = max(dp1[i], dp1[prev]+1)
      if nums2[i]>nums2[prev]: dp2[i] = max(dp2[i], dp2[prev]+1)
  dp2.reverse()

  min_removals = float("inf")
  for i in range(n):
    if dp1[i] > 1 and dp2[i] > 1:
      min_removals = min(min_removals, n - (dp1[i]+dp2[i]-1))
  return min_removals

nums = [2,1,1,5,6,2,3,1]
#rev = [1, 3, 2, 6, 5, 1, 1, 2]

print(minimumMountainRemovals(nums))


def maxBitonic(nums):
  if not nums: return 0
  n = len(nums)
  dp1 = [1]*n

  nums2 = nums[::-1]
  dp2 = [1]*n

  for i in range(1,n):
    for prev in range(0,i):
      if nums[i]>nums[prev]: dp1[i] = max(dp1[i], dp1[prev]+1)
      if nums2[i]>nums2[prev]: dp2[i] = max(dp2[i], dp2[prev]+1)
  dp2.reverse()
  
  maxi = 0
  for i in range(n):
    maxi = max(maxi, dp1[i]+dp2[i]-1)
  return maxi