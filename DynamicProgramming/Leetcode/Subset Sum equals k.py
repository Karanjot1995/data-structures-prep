from collections import defaultdict

def subsetSum(nums, k: int) -> int:
  n = len(nums)
  if n == 1 and nums[0]!=k: return 0

  dp = [[-1 for _ in range(k+1)] for _ in range(n)]
  def rec(i,rem):
    if rem==0: return True
    if rem<0: return False
    if i == 0: return nums[0]==k
    if dp[i][rem]!=-1: return dp[i][rem]

    take = False
    #take only if the remaining target is greater or equal to the current number
    if rem>=nums[i]:
      take = rec(i-1,rem-nums[i])
    not_take = rec(i-1,rem)
    dp[i][rem] = take or not_take

    return take or not_take

  res = rec(n-1,k)
  print(dp)
  return res


print(subsetSum([1,2,3,4,0],5))