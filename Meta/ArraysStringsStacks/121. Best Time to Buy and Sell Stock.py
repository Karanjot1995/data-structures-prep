'''
Time complexity: O(n). Only a single pass is needed.
Space complexity: O(1). Only two variables are used.
'''

class Solution:
    def maxProfitOptimal(self, prices: List[int]) -> int:
      min_price = prices[0]
      max_profit = 0

      for price in prices:
        if price < min_price: min_price = price
        if price - min_price > max_profit: max_profit = price - min_price

      return max_profit

'''
Brute force: 
Time complexity: O(n2). Loop runs n(n-1)/2 times.
Space complexity: O(1). Only two variables - maxprofit and profit are used.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit

        return max_profit
