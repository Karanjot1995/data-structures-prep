class NumArray:

  def __init__(self, nums):
    self.nums = nums
    self.sums = []  
    tot = 0
    for num in nums:
      tot+=num
      self.sums.append(tot)


  #Brute TC -> O(1)  SC -> O(N)
  def sumRange(self, left: int, right: int) -> int:
    sum_left =  self.sums[left-1] if left>0 else 0
    return self.sums[right] - sum_left
  

  #Brute TC -> O(N)  SC -> O(1)
  def sumRange2(self, left: int, right: int) -> int:
    for i in range(left,right+1):
      sum+= self.nums[i]
    return sum

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)