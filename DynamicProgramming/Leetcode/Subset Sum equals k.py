from collections import defaultdict

# recursive
def subsetSumRec(nums, k: int) -> int:
  n = len(nums)
  if n == 1 and nums[0]!=k: return 0

  def rec(i,rem):
    if rem == 0: return True
    if rem<0: return False
    if i == 0: return nums[0] == k

    take = False
    if rem>= nums[i]: take = rec(i-1, rem-nums[i])
    not_take = rec(i-1, rem)

    return take or not_take
  
  res = rec(n-1,k)
  return res

print(subsetSumRec([1,2,3,4,0],5))

def subsetSum(nums, k: int) -> int:
  n = len(nums)
  if n == 1 and nums[0]!=k: return 0

  dp = [[-1 for _ in range(k+1)] for _ in range(n)]
  def rec(i,rem):
    if rem==0: return True
    if rem<0: return False
    if i == 0: return nums[0]==k #if we moved to the first index and it is equal to the rem/target 
    if dp[i][rem]!=-1: return dp[i][rem]

    take = False
    #take only if the remaining target is greater or equal to the current number
    if rem>=nums[i]: take = rec(i-1,rem-nums[i])
    not_take = rec(i-1,rem)
    dp[i][rem] = take or not_take #whichever returns true or if both return false

    return take or not_take

  res = rec(n-1,k)
  print(dp)
  return res



print(subsetSum([1,2,3,4,0],5))



def subsetSumToK(n, k, arr):
    # Initialize a 2D DP table with False values.
    dp = [[False for j in range(k + 1)] for i in range(n)]
    
    # Set the first column to True since a sum of 0 is always possible with an empty subset.
    for i in range(n):
        dp[i][0] = True
    
    # Check if the first element of the array can be used to make the target sum.
    if arr[0] <= k:
        dp[0][arr[0]] = True
    
    
    # Fill in the DP table iteratively.
    for ind in range(1, n):
        for target in range(1, k + 1):
            notTaken = dp[ind - 1][target]  # Not taking the current element.
            taken = False
            # Check if taking the current element is possible without exceeding the target.
            if arr[ind] <= target:
                taken = dp[ind - 1][target - arr[ind]]
            dp[ind][target] = notTaken or taken  # Update the DP table with the result.
    
    # The final result is stored in the bottom-right cell of the DP table.
    return dp[n - 1][k]

arr = [1, 2, 3, 4]
k = 4
n = len(arr)
print(subsetSumToK(n,k,arr))
