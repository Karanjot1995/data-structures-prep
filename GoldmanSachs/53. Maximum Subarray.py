import math

# Time complexity: O(N)O(N)O(N), where NNN is the length of nums.
# We iterate through every element of nums exactly once.
# Space complexity: O(1)O(1)O(1)


def maxSubArray(nums) -> int:
    maxSum = nums[0]
    currentSum = nums[0]

    for num in nums[1:]:
      currentSum = max(num, currentSum + num)
      maxSum = max(maxSum, currentSum)
      # print(currentSum, maxSum)

    return maxSum

def maxSubArrayBrute(nums) -> int:
  max_subarray = -math.inf
  for i in range(len(nums)):
    current_subarray = 0
    for j in range(i, len(nums)):
      current_subarray += nums[j]
      max_subarray = max(max_subarray, current_subarray)

  return max_subarray


nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [5,4,-1,7,8]
print(maxSubArray(nums))
#op = 6
#op = 23 