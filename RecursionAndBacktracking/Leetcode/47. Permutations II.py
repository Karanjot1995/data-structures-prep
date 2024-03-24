from collections import Counter
# https://leetcode.com/problems/permutations-ii/

# MOST INTIUTIVE
# Nikhil Lohia: https://www.youtube.com/watch?v=YW5F0WqBBWY
# TC - O(n!*n) = n! to generate all permutations, traversing array n times
# SC - O(n) = O(n)

class Solution:
  def permuteUnique(self, nums):
    ans = []
    n = len(nums)
    vis = [0]*n

    def backtrack(seq):
      if len(seq)==n and seq not in ans: 
        ans.append(seq.copy())
        return

      for i in range(n):
        if vis[i]: continue
        seq.append(nums[i])
        vis[i]=1
        backtrack(seq)
        seq.pop()
        vis[i]=0

    backtrack([])

    return ans
  


def permuteUnique(nums):
  ans = []
  counter = Counter(nums)
  def backtrack(comb):
    if len(comb) == len(nums):
      ans.append(list(comb))
      return

    for num in counter:
      if counter[num] > 0:
        # add this number into the current combination
        comb.append(num)
        counter[num] -= 1
        # continue the exploration
        backtrack(comb)
        # revert the choice for the next exploration
        comb.pop()
        counter[num] += 1

  backtrack([], )

  return ans

nums = [1,1,2]
# nums = [1,2,3]
print(permuteUnique(nums))
#Output: [[1,1,2],[1,2,1],[2,1,1]]
#Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

      
