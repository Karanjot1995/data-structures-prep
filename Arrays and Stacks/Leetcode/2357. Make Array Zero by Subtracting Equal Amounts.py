import heapq
class Solution:
  def minimumOperations(self, nums) -> int:
    nums = set(nums)
    if list(nums)[0] == 0: return len(nums) - 1
    return len(nums)
    