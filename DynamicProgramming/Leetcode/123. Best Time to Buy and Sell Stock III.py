'''

'''
# TC -> 2^n
def maxProfitRec(prices) -> int:

  def rec(i,buy, cap):
    if i == len(prices): return 0
    if cap == 2: return 0
    if buy:
      take = - prices[i] + rec(i+1,0, cap) #buy on current day
      not_take = 0 + rec(i+1, 1, cap) #not buy on current day
      profit = max(take, not_take)
    else:
      sell = prices[i] + rec(i+1,1, cap+1) #sell on current day
      not_sell = 0 + rec(i+1,0, cap) #not sell on current day
      profit = max(sell, not_sell)
    return profit
  
  ans = rec(0,1,0)
  return ans

prices = [3,3,5,0,0,3,1,4]
print(maxProfitRec(prices))

'''
TC - Nx2x2
SC - Nx2x3 + N(recursion stack space)
'''
def maxProfitMemo(prices) -> int:
  n = len(prices)
  m = 2 # buy is allowed or not so 2 states
  dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]

  def rec(i,buy, cap):
    if i == len(prices): return 0
    if cap == 2: return 0
    if dp[i][buy][cap]!=-1: return dp[i][buy][cap]
    profit = 0
    if buy:
      take = - prices[i] + rec(i+1,0,cap) #buy on current day
      not_take = 0 + rec(i+1, 1, cap) #not buy on current day
      profit = max(take, not_take)
    else:
      sell = prices[i] + rec(i+1,1, cap+1) #sell on current day
      not_sell = 0 + rec(i+1,0, cap) #not sell on current day
      profit = max(sell, not_sell)
    dp[i][buy][cap] = profit
    return dp[i][buy][cap]
  
  ans = rec(0,1,0)
  return ans

prices = [3,3,5,0,0,3,1,4]
print(maxProfitMemo(prices))


'''
Overall, we run an iteration over the sequence of prices.

Over the iteration, we calculate 4 variables which correspond to the costs or the profits of each action respectively, as follows:

t1_cost: the minimal cost of buying the stock in transaction #1. 
The minimal cost to acquire a stock would be the minimal price value that we have seen so far at each step.

t1_profit: the maximal profit of selling the stock in transaction #1. Actually, at the end of the iteration, 
this value would be the answer for the first problem in the series, i.e. Best Time to Buy and Sell Stock.

t2_cost: the minimal cost of buying the stock in transaction #2, while taking into account the profit gained from the previous transaction #1. One can consider this as the cost of reinvestment. 
Similar with t1_cost, we try to find the lowest price so far, which in addition would be partially compensated by the profits gained from the first transaction.

t2_profit: the maximal profit of selling the stock in transaction #2. With the help of t2_cost as we prepared so far, we would find out the maximal profits with at most two transactions at each step.
'''
# without DP
def maxProfit(prices):
  t1_cost, t2_cost = float("inf"), float("inf")
  t1_profit, t2_profit = 0, 0

  for price in prices:
      # the maximum profit if only one transaction is allowed
      t1_cost = min(t1_cost, price)
      t1_profit = max(t1_profit, price - t1_cost)
      # reinvest the gained profit in the second transaction
      t2_cost = min(t2_cost, price - t1_profit)
      t2_profit = max(t2_profit, price - t2_cost)
      print(price, "t1 cost:",t1_cost, ", t1 profit:",t1_profit, ", t2 cost:",t2_cost, ", t2 profit:",t2_profit)
  return t2_profit

# def maxProfitTab(prices) -> int:
#   n = len(prices)
#   m = 2 # buy is allowed or not so 2 states
#   dp = [[-1 for _ in range(m)] for _ in range(n+1)]
#   dp[n][0] = dp[n][1] = 0
#   print(dp)
#   for i in range(n-1,-1,-1):
#     for buy in range(2):
#       profit = 0
#       if buy:
#         take = - prices[i] + dp[i+1][0] #buy on current day
#         not_take = 0 + dp[i+1][1] #not buy on current day
#         profit = max(take, not_take)
#       else:
#         sell = prices[i] + dp[i+1][1] #sell on current day
#         not_sell = 0 + dp[i+1][0] #not sell on current day
#         profit = max(sell, not_sell)
#       dp[i][buy] = profit
#   print(dp)
#   return dp[0][1]

# prices = [7,1,5,3,6,4]
# print(maxProfitTab(prices))