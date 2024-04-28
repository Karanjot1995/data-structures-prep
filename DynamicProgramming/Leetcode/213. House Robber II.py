#circular connection of houses, if first is robbed last cant be robbed
class Solution:
  def rec(self,nums):
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

  def rob(self, nums) -> int:
    if len(nums)== 1: return nums[0]
    n = len(nums)
    max1 = self.rec(nums[1:])
    max2 = self.rec(nums[:n-1])
    return max(max1, max2)
