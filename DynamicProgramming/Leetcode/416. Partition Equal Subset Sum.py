class Solution:
  def subsetSum(self, nums, k):
    n = len(nums)
    if n == 1 and nums[0]!=k: return False

    dp = [[-1 for _ in range(k+1)] for _ in range(n)]

    def rec(i,rem):
      if rem==0: return True
      if rem<0: return False
      if i == 0: return nums[0]==k
      if dp[i][rem]!=-1: return dp[i][rem]

      take = False
      if rem>=nums[i]: take = rec(i-1,rem-nums[i])
      not_take = rec(i-1,rem)
      dp[i][rem] = take or not_take

      return take or not_take

    res = rec(n-1,k)
    return res

  def canPartition(self, nums: List[int]) -> bool:
    if len(nums)==1: return False
    total = sum(nums)
    if total%2 == 1: return False
    return self.subsetSum(nums,int(total/2))
  
