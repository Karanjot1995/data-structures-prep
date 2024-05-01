def pivotIndex(nums) -> int:
  l = 0
  r = sum(nums)
  for i in range(len(nums)):
    if l == r-l-nums[i]: return i
    l+=nums[i]
  return -1

def pivotIndex(nums) -> int:
  for i in range(len(nums)):
    if i>0: l += nums[i-1]
    r -= nums[i]
    if l==r: return i

  return -1
        