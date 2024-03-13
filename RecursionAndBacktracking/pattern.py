def subsets(nums):
  ans = []
  def rec(i,seq):
    if i>= len(nums):
      print(seq)
      ans.append(seq[:])
      return
    seq.append(nums[i])
    # pick the element to the subsequence
    rec(i+1, seq)
    seq.pop()
    # do not pick the element to the subsequence
    rec(i+1, seq)
  
  seq = []
  rec(0,seq)
  return ans

nums = [3,1,2]
print(subsets(nums))