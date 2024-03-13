'''
Intuition
Given a list of integers, the task is to find all possible subsets. However, there are duplicate integers in the list, so we have to handle them to avoid duplicate subsets.

Approach
First, we sort the list. This ensures that duplicates are adjacent to each other.
We use a backtracking approach. We start with an empty list and at every step, we choose to either include or exclude the current element.
If the current element is the same as the previous element and the previous element was excluded, then we skip the current element to avoid duplicate subsets.
Complexity

Time complexity: O(2^n), where n is the length of the nums list. In the worst case, we would have 2^n subsets.
Space complexity: O(n*2^n), primarily for the recursive call stack.
'''

# N-Queen
def subsetsWithDup(nums):
  ans = []
  nums.sort()
  def backtrack(idx, seq):
    ans.append(seq[:])
    for i in range(idx, len(nums)):
      if i>idx and nums[i]==nums[i-1]: continue
      seq.append(nums[i])
      backtrack(i+1, seq)
      seq.pop()
  
  backtrack(0,[])
  return ans

nums = [1,2,2]
print(subsetsWithDup(nums))


#brute force
def subsetsWithDup(nums):
  ans = []
  nums.sort()

  def rec(i,seq):
    if i==len(nums): 
      ans.append(seq[:])
      return

    seq.append(nums[i])
    rec(i+1, seq)
    seq.pop()
    while i+1<len(nums) and nums[i]==nums[i+1]: i+=1
    rec(i+1, seq)

  rec(0,[])

  return ans
        
print(subsetsWithDup(nums))
