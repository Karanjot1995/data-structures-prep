#Recursive TC - Exponential
#where to use same index approach for TAKE: infinite supply , multiple use

def coinChange(coins, amount):
  def rec(i, rem):
    if i == len(coins)-1:
      if rem%coins[i]==0: return rem//coins[i]
      return float("inf")
    
    take = float("inf")
    if coins[i]<=rem:
      take = 1 + rec(i, rem-coins[i])
    not_take = 0 + rec(i+1,rem)
    return min(take, not_take)
    
  return rec(0, amount)

print(coinChange([1,2,5], 11))



def coinChange(coins, amount) -> int:
  if len(coins)==1 and amount == 0: return 0
  
  dp = [[-1 for _ in range(amount+1)] for _ in range(len(coins))]
  def rec(i, rem):
    if i == len(coins)-1:
      if rem%coins[i]==0: return rem//coins[i]
      return float("inf")
    if dp[i][rem] != -1: return dp[i][rem]
    
    take = float("inf")
    if coins[i]<=rem:
      take = 1 + rec(i, rem-coins[i])
    not_take = 0 + rec(i+1,rem)

    dp[i][rem] = min(take, not_take)
    return min(take, not_take)
    
  ans = rec(0, amount)
  return -1 if ans == float("inf") else ans