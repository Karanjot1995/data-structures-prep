def maxArea(height) -> int:
  l,r = 0, len(height)-1
  max_area = 0
  while l<r:
    width = r-l
    area = min(height[l],height[r])*width
    max_area = max(max_area,area)
    if height[l]<=height[r]:
      l+=1
    else: r-=1
  return max_area


height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
#Output: 49

