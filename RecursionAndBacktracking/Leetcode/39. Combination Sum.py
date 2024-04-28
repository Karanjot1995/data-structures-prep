# Time Complexity: O(N^(T/M+1))
# Space Complexity: O(N^(T/M))

def combinationSum(candidates, target: int):
  ans = []
  def rec(i,seq, remain):
    if remain <0: return
    if i == len(candidates):
      if remain == 0: ans.append(seq[:])
      return

    # pick the element till it is smaller than target
    if candidates[i]<=remain:
      seq.append(candidates[i])
      rec(i, seq, remain-candidates[i]) #pick
      seq.pop()
    
    rec(i+1, seq, remain) #not pick

  rec(0, [], target)
  return ans

candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates, target))
# Output: [[2,2,3],[7]]
