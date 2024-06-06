from collections import defaultdict


class Solution:
  def containsNearbyDuplicate(self, nums, k: int) -> bool:
    dups = defaultdict(int)

    for i,num in enumerate(nums):
      if num in dups: 
        if abs(dups[num]-i)<=k: return True
      dups[num] = i

    return False