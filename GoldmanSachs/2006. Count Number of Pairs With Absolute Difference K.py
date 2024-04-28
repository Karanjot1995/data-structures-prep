from collections import defaultdict

class Solution:
  def countKDifference(self, nums, k: int) -> int:
    hmap = defaultdict(int)
    cnt = 0
    for num in nums:
      cnt += hmap[num-k] + hmap[num+k]
      hmap[num]+=1

    return cnt
    # cnt = 0
    # n = len(nums)
    # for i in range(n):
    #   for j in range(i+1,n):
    #     if abs(nums[i]-nums[j])==k:cnt+=1

    # return cnt