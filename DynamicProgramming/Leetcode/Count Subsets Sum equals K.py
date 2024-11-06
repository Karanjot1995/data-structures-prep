def subsetSum(nums, k: int) -> int:
  n = len(nums)
  if n == 1 and nums[0]!=k: return 0

  dp = [[-1 for _ in range(k+1)] for _ in range(n)]
  def rec(i,rem):
    if i == 0:
       if rem == 0 and nums[0] == 0: return 2
       if rem == 0 or rem == nums[0]: return 1
       return 0
    # if rem==0: return 1
    # if rem<0: return 0
    # if i == 0: return nums[0] == rem
    if dp[i][rem]!=-1: return dp[i][rem]
    take = 0
    if rem>=nums[i]: take = rec(i-1,rem-nums[i]) #1
    not_take = rec(i-1,rem) #
    dp[i][rem] = take + not_take

    return take + not_take

  res = rec(n-1,k)
  for d in dp:
    print(d)
  return res



print(subsetSum([0,1,3,2],3))



def subsetSumTabulation(nums, k: int) -> int:
  n = len(nums)
  if n == 1 and nums[0]!=k: return 0

  dp = [[0 for _ in range(k+1)] for _ in range(n)]

  for i in range(n): dp[i][0] = 1

  if nums[0] <= k: dp[0][nums[0]] = 1

  # Fill in the DP table iteratively.
  for i in range(1, n):
      for target in range(0, k + 1):
          notTaken = dp[i - 1][target]  # Not taking the current element.
          taken = 0
          if nums[i] <= target: taken = dp[i - 1][target - nums[i]]
          dp[i][target] = notTaken + taken  # Update the DP table with the result.

  for d in dp: print(d)
  
  return dp[n-1][k]


print(subsetSumTabulation([0,1,3,2],3))


#     0    1    2    3    4    5
# 0  -1              
# 1  -1     
# 2  -1


# 3  -1                   
# 4  -1                        
# 5  -1
# 6  -1
# 7  -1