from collections import Counter
from math import ceil

def minOperations(nums) -> int:
  hmap = Counter(nums)
  cnt=0
  for val in hmap.values():
    if val == 1: return -1
    cnt+= ceil(val/3)

  return cnt

nums = [2,3,3,2,2,4,2,3,4]

print(minOperations(nums))

# Output: 4
# Explanation: We can apply the following operations to make the array empty:
# - Apply the first operation on the elements at indices 0 and 3. The resulting array is nums = [3,3,2,4,2,3,4].
# - Apply the first operation on the elements at indices 2 and 4. The resulting array is nums = [3,3,4,3,4].
# - Apply the second operation on the elements at indices 0, 1, and 3. The resulting array is nums = [4,4].
# - Apply the first operation on the elements at indices 0 and 1. The resulting array is nums = [].
# It can be shown that we cannot make the array empty in less than 4 operations.