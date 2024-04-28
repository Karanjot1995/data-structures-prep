def computeSnowpack(height):
  if not height or len(height) == 0 or len(height) == 1:
      return 0
      
  n = len(height)
  ans = max_left = max_right = 0
  left, right = 0, n - 1

  while left <= right:
    if height[left] <= height[right]:
      if height[left] >= max_left:
        max_left = height[left]
      else:
        ans += max_left - height[left]
      left += 1
    else:
      if height[right] >= max_right:
        max_right = height[right]
      else:
        ans += max_right - height[right]
      right -= 1
  
  return ans

print(computeSnowpack([0, 1, 3, 0, 1, 2, 0, 4, 2, 0, 3, 0])) # 13
print(computeSnowpack([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])) # 10