'''
VARIATION: https://leetcode.com/discuss/interview-question/4571159/Meta-or-Phone-Screen-or-E4

Given a number of personal time off days (PTO), maximize the length of the longest vacation you can take with given PTO days

Example

Input:
[W, H, H, W, W, H, W] PTO = 2
'''
class Solution:
  def longestOnes(self, nums, k: int) -> int:
    left=0
    window = 0
    for right in range(len(nums)):
      if nums[right]==0:
        k-=1
      if k<0:
        if nums[left]==0:
          k+=1
        left+=1
      print(k, left,right)
      # window = max(window, right-left+1)

    return right-left+1
      
      

        

        