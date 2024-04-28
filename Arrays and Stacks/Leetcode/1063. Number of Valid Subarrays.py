def validSubarrays(nums) -> int:
  ans = 0
  stack = []

  for num in nums:
    while stack and num < stack[-1]:
      stack.pop()
    stack.append(num)
    # print(stack)
    ans+=len(stack)
  return ans


nums = [1,4,2,5,3]
print(validSubarrays(nums))
# Output: 11
# Explanation: There are 11 valid subarrays: [1],[4],[2],[5],[3],[1,4],[2,5],[1,4,2],[2,5,3],[1,4,2,5],[1,4,2,5,3].