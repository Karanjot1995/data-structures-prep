class Solution:
  def threeSum(self, nums):
    if len(nums)==3: return [nums] if nums[0]+nums[1]+nums[2] == 0 else []
    nums.sort()
    res = []
    i = 0
    while i < len(nums):
      lo = i+1
      hi = len(nums)-1
      if i==0 or nums[i-1] != nums[i]:
        while lo<hi:
          s = nums[i]+nums[lo]+nums[hi]
          if s<0: lo+=1
          elif s>0: hi-=1
          else:
            res.append([nums[i],nums[lo],nums[hi]])
            lo+=1
            hi-=1
            while lo < hi and nums[lo] == nums[lo - 1]:
              lo+=1
      i+=1
    return res   