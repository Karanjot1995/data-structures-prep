class Solution:
  def minSubArrayLen(self, target: int, nums) -> int:
    left = 0
    right = 0
    currWindowSum = 0
    min_len = float('inf')

    for right in range(len(nums)):
      currWindowSum+=nums[right]
      while currWindowSum>=target:
        min_len = min(min_len, right-left+1)
        currWindowSum-=nums[left]
        left+=1
    
    return min_len if min_len != float('inf') else 0
  

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.