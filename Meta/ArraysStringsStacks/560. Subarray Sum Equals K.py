from collections import defaultdict, deque
class Solution:

  #TC -> O(N) , SC -> O(N)
  def subarraySumHmap(self, nums, k: int) -> int:
    cnt, preSum = 0,0
    hmap = defaultdict(int)
    hmap[0]=1
    for i in range(len(nums)):
      preSum+=nums[i]
      if preSum-k in hmap: cnt+= hmap[preSum-k]
      hmap[preSum]+=1
    return cnt
  
  # brute force N2
  def subarraySumBrute(self, nums, k: int) -> int:
    cnt = 0
    for i in range(len(nums)):
      sum=0
      for j in range(i,len(nums)):
        sum+=nums[j]
        if sum==k:
          cnt+=1
        
    return cnt
  
  # only positives
  def subarraySum(self, nums, k: int):
    n = len(nums)
    sum = start = 0
    for end in range(n):
      sum+=nums[end]

      while start<end and sum>k:
        sum-=nums[start]
        start+=1

      if sum == k: return True
    # start=end=0
    # while start<n and end<n:
    #   sum+=nums[end]
    #   while start<end:
    #     sum-=nums[start]
    #     start+=1
    #   if sum==k: return True
    #   end+=1

  def subarraySumPrint(self, nums, k: int):
    n = len(nums)
    sum = start = 0
    subsequence = deque([])    
    for end in range(n):
      sum+=nums[end]
      subsequence.append(nums[end])

      while start<end and sum>k:
        sum-=nums[start]
        subsequence.popleft()
        start+=1

      if sum == k: 
        print(subsequence)
        return True

