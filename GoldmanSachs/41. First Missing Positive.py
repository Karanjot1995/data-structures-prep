class Solution:
  def firstMissingPositive(self, nums) -> int:
    nums_length = len(nums)
    # initialize the cursor
    i = 0

    # phase 1: sort the numbers with cyclic sort
    # move the cursor through the list
    while i < nums_length:
      # has minus 1 because the numbers start from 1 not 0
      val_at_i = nums[i] - 1

      # does the value belong in the range of the list?
      # if it doesn't, we get an out of bounds error
      # when we try to access nums[val_at_i] later
      belongs_in_range = 0 <= val_at_i < nums_length

      if belongs_in_range and nums[i] != nums[val_at_i]:
        nums[i], nums[val_at_i] = nums[val_at_i], nums[i]
      else:
        i += 1
    print(nums)

    # phase 2: find the first missing positive integer
    for x in range(nums_length):
      # has plus 1 because the numbers start from 1 not 0
      if x + 1 != nums[x]:
        return x + 1

    # if all numbers are in the correct spot,
    # the first missing positive integer is the
    # length of the list + 1
    return nums_length + 1
  

  # def firstMissingPositive(self, nums):
  #   n = len(nums)
  #   seen = [False]*(n+1)

  #   for num in nums:
  #     if 0 < num <= n:
  #       seen[num]=True

  #   for i in range(1, n+1):
  #     if not seen[i]: return i

  #   return n+1



# Example 2:

# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.
# Example 3:

# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.