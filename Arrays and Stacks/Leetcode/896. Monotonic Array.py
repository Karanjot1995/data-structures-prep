class Solution:
  def isMonotonic(self, nums) -> bool:
    if len(nums)==1: return True
    rev = None
    if nums[0]>nums[-1]: rev = True
    for i in range(1,len(nums)):
      if rev and nums[i-1]<nums[i]: return False
      if not rev and nums[i-1]>nums[i]: return False
    return True