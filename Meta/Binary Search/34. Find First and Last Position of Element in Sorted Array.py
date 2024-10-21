class Solution:
  def searchRange(self, nums: List[int], target: int) -> List[int]:
    lower = self.findBound(nums, 0, len(nums)-1, target, True)
    if lower == -1: return [-1,-1]
    upper = self.findBound(nums, 0, len(nums)-1, target, False)
    return [lower,upper]


  def findBound(self,nums, l, r, target, isFirst):
    while l<=r:
      mid = (l+r)//2
      if nums[mid]==target:
        if isFirst:
          if mid == l or nums[mid-1]<target: return mid
          r=mid-1
        else:
          if mid == r or nums[mid+1]>target: return mid
          l = mid+1
      elif nums[mid]<target:
        l = mid+1
      else:
        r = mid-1
    return -1