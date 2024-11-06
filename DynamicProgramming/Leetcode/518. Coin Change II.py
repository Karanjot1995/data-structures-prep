class Solution:
  def change(self, amount: int, coins: List[int]) -> int:
    dp = [[-1 for _ in range(amount+1)] for _ in range(len(coins))]
    def rec(i, rem):
      if i == len(coins)-1:
        return rem%coins[i]==0
      if dp[i][rem]!=-1: return dp[i][rem]  

      take = 0
      if coins[i]<=rem:
        take = rec(i, rem-coins[i])
      not_take = rec(i+1,rem)
      dp[i][rem] = take+not_take
      return take+not_take
    
    return rec(0, amount)
        