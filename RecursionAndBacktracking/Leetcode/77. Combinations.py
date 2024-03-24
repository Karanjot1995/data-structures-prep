def combine(n: int, k: int):
  ans = []
  def backtrack(idx, seq):
    if len(seq)==k: 
      ans.append(seq.copy())
      return
      
    # if i>=n: return
    # seq.append(idx+1)
    # rec(idx+1, seq)
    # seq.pop()
    # rec(idx+1, seq)

    for i in range(idx,n):
      seq.append(i+1)
      backtrack(i+1, seq)
      seq.pop()


  backtrack(0,[])

  return ans
        
n = 4
k = 2
print(combine(n,k))
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]