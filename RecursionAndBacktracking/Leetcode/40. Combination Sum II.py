class Solution:

  # Time Complexity: O(k * 2^n)
  # Space Complexity: O(k * x)

  #Subtraction: calculating based on remaining difference from target
  def combinationSum2(self, candidates, target: int):
    ans = []
    candidates.sort()
    def dfs(idx,curr, seq):
      if curr == 0:
        ans.append(seq[:])
        return
      for i in range(idx, len(candidates)):
        if i>idx and candidates[i] == candidates[i-1]:
          continue
        if candidates[i]>curr: break
        # seq.append(candidates[i])
        dfs(i+1, curr - candidates[i], seq+[candidates[i]])
        # seq.pop()
    dfs(0, target, [])

    return ans
  

  #Addition: calculating by adding till we reach target
  def combinationSum2(self, candidates, target: int):
    ans = []
    candidates.sort()

    def dfs(idx, curr, seq):
      if curr > target: return
      if curr == target:
        ans.append(seq)
        return
      for i in range(idx, len(candidates)):
        if i > idx and candidates[i] == candidates[i-1]:
          continue
        dfs(i+1, curr + candidates[i], seq+[candidates[i]])
        
    dfs(0, 0, [])

    print(ans)

    return ans



  #brute force
  def combinationSum2(self, candidates, target: int):
    ans = []
    candidates.sort()

    def rec(i, seq, sum):
      if sum == target:
        ans.append(seq.copy())
        return
      if i >= len(candidates) or sum > target:
        return

      seq.append(candidates[i])
      rec(i+1, seq, sum+candidates[i])
      seq.pop()
      while i+1<len(candidates) and candidates[i]==candidates[i+1]: 
        i+=1
      rec(i+1, seq, sum)
    rec(0,[],0)

    return ans