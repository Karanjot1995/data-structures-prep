'''

'''
# TC -> 2^n
def maxProfitRec(prices) -> int:

  def rec(i,buy):
    if i == len(prices): return 0
    if buy:
      take = - prices[i] + rec(i+1,0) #buy on current day
      not_take = 0 + rec(i+1, 1) #not buy on current day
      profit = max(take, not_take)
    else:
      sell = prices[i] + rec(i+1,1) #sell on current day
      not_sell = 0 + rec(i+1,0) #not sell on current day
      profit = max(sell, not_sell)
    return profit
  
  ans = rec(0,1)
  return ans

prices = [7,1,5,3,6,4]
print(maxProfitRec(prices))


def maxProfitMemo(prices) -> int:
  n = len(prices)
  m = 2 # buy is allowed or not so 2 states
  dp = [[-1 for _ in range(m)] for _ in range(n)]

  def rec(i,buy):
    if i == len(prices): return 0
    if dp[i][buy]!=-1: return dp[i][buy]
    profit = 0
    if buy:
      take = - prices[i] + rec(i+1,0) #buy on current day
      not_take = 0 + rec(i+1, 1) #not buy on current day
      profit = max(take, not_take)
    else:
      sell = prices[i] + rec(i+1,1) #sell on current day
      not_sell = 0 + rec(i+1,0) #not sell on current day
      profit = max(sell, not_sell)
    dp[i][buy] = profit
    return dp[i][buy]
  
  ans = rec(0,1)
  print(dp)
  return ans

prices = [7,1,5,3,6,4]
print(maxProfitMemo(prices))
[[-1, 7], 
 [8, 7], 
 [8, 3], 
 [6, 3], 
 [6, 0], 
 [4, 0]]



def maxProfitTab(prices) -> int:
  n = len(prices)
  m = 2 # buy is allowed or not so 2 states
  dp = [[-1 for _ in range(m)] for _ in range(n+1)]
  dp[n][0] = dp[n][1] = 0
  print(dp)
  for i in range(n-1,-1,-1):
    for buy in range(2):
      profit = 0
      if buy:
        take = - prices[i] + dp[i+1][0] #buy on current day
        not_take = 0 + dp[i+1][1] #not buy on current day
        profit = max(take, not_take)
      else:
        sell = prices[i] + dp[i+1][1] #sell on current day
        not_sell = 0 + dp[i+1][0] #not sell on current day
        profit = max(sell, not_sell)
      dp[i][buy] = profit
  print(dp)
  return dp[0][1]

prices = [7,1,5,3,6,4]
print(maxProfitTab(prices))