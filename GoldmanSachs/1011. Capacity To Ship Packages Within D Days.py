# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

'''
- Min capacity that we can assume is the max weight in the array as if we go less than that then the item will not be able to shipped in any one day
- Max capacity can be total sum of the weights as in one day we can ship all the items
- Now we have the range of capacity [min, max]

APPROACH 1: Brute Force
- For the range of capacity do a for loop and check if it is possible to ship within D days the first answer you get, return that

TC - O((total sum - max + 1) * N) if both are linear then it will be quadratic
SC - O(1)

APPROACH 2: Binary Search
- For the range of capacity apply Binary Search

TC - O(Nlog(total sum - max + 1)), N to calcualte total load and max load => effectively will be O(NLogN)
SC - O(1)
'''

class Solution:
  def shipWithinDays(self, weights, days: int) -> int:
    def isFeasible(capacity):
      daysNeeded = 1
      load = 0

      for wt in weights:
        load+=wt
        if load>capacity:
          daysNeeded+=1
          load = wt

      return daysNeeded<=days

    
    left = max(weights)
    right = sum(weights)

    while left<=right:
      mid = (left+right)//2
      if isFeasible(mid):
        right = mid-1
      else:
        left = mid+1
    
    return left