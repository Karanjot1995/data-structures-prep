#Recursive TC - 2^n

def knapsack(W, val, wt):
  def rec(i, rem):
    # if rem<0: return 0
    if i == len(wt)-1:
      if wt[i]<=rem: return val[i]
      return 0
    take = float("-inf")
    if wt[i]<=rem:
      take = val[i] + rec(i+1, rem-wt[i])
    not_take = 0+rec(i+1,rem)
    return max(take, not_take)
    
  return rec(0, W)


#Recursive TC - 2^n

def knapsack(W, val, wt):
  dp = [[-1 for _ in range(W+1)] for _ in range(len(wt))]

  def rec(i, rem):
    # if rem<0: return 0
    if i == len(wt)-1:
      if wt[i]<=rem: return val[i]
      return 0
    if dp[i][rem] != -1: return dp[i][rem]
    take = float("-inf")
    if wt[i]<=rem:
      take = val[i] + rec(i+1, rem-wt[i])
    not_take = 0+rec(i+1,rem)
    dp[i][rem] = max(take, not_take)
    return max(take, not_take)
    
  return rec(0, W)



    # dp = [[-1 for _ in range(k+1)] for _ in range(n)]
    # def rec(i,rem):
    #     if i == 0:
    #         if rem == 0 and nums[0] == 0: return 2
    #         if rem == 0 or rem == nums[0]: return 1
    #         return 0

    #     if dp[i][rem]!=-1: return dp[i][rem]
    #     take = 0
    #     if rem>=nums[i]: take = rec(i-1,rem-nums[i])
    #     not_take = rec(i-1,rem)
    #     dp[i][rem] = (take + not_take)%MOD

    #     return dp[i][rem]

    # res = rec(n-1,k)
    # return res


W = 4
val = [1,2,2,3]
wt = [4,5,3,1]

print(knapsack(W, val, wt))

