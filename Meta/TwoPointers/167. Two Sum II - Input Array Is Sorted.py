class Solution:
  def twoSum(self, numbers, target: int):
    i = 0
    j = len(numbers)-1
    while i<j:
      sum = numbers[i]+numbers[j]
      if sum == target: return [i+1, j+1]
      elif sum>target: j-=1
      else: i+=1

    return [-1,-1]