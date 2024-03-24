# striver approach 1
# TC - O(n!*n) = n! to generate all permutations, n for deep copying final perm to ans
# SC - O(n) = O(n) stack space, O(n) for freq array, O(n) for ans array
def permute(nums):
  ans = []
  n = len(nums)
  vis = [0]*n
  def backtrack(seq):
    if len(seq)==n:
      ans.append(seq.copy())
    for i in range(n):
      if not vis[i]: 
        vis[i]=1
        seq.append(nums[i])
        backtrack(seq)
        # go back pop and unmark it
        seq.pop()
        vis[i]=0

  backtrack([])

  return ans

nums = [1,2,3]

print(permute(nums))
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


def permute2(nums):
  ans = []
  n = len(nums)

  def backtrack(seq):
    if len(seq)==n: ans.append(seq.copy())

    for num in nums:
      if num in seq: continue
      seq.append(num)
      backtrack(seq)
      seq.pop()

  backtrack([])
  return ans

nums = [1,2,3]

print('permute2: ',permute2(nums))



#swapping
# striver approach 2 (skip this approach)
# TC - O(n!*n) = n! to generate all permutations, n for deep copying final perm to ans
# SC - O(n) = O(n) stack space, O(n) for ans array
def permute3(nums):
  ans = []
  n = len(nums)

  def backtrack(idx):
    if idx == n: 
      ans.append(nums.copy())
      return
    
    for i in range(idx,n):
      nums[i], nums[idx] = nums[idx], nums[i]
      backtrack(idx+1)
      nums[i], nums[idx] = nums[idx], nums[i] #swap back

  backtrack(0)
  return ans

nums = [1,2,3]

print('permute3: ',permute3(nums))



        