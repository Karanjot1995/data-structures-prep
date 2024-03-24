
# Brute Force
# TC -> O(N*2^n)
# SC -> O(N*2^n)

def subsetsPowerSet(nums):
  output = [[]]
  
  for num in nums:
    output += [curr + [num] for curr in output]
    # print(output)

  return output

nums = [3,1,2]
print(subsetsPowerSet(nums))



#-----------------------------------------------#



# TC -> O(2^n) : exponential
# SC -> O(N)

# N Queen
def subsets(nums):
  res = []
  def dfs(idx, path):
    res.append(path)
    for i in range(idx, len(nums)):
      dfs(i+1, path+[nums[i]])

  dfs(0, [])
  return res

def subsets(nums):
  ans = []
  def backtrack(i,seq):
    if i>= len(nums):
      ans.append(seq[:])
      return
    seq.append(nums[i])
    # pick the element to the subsequence
    backtrack(i+1, seq)
    seq.pop()
    # do not pick the element to the subsequence
    backtrack(i+1, seq)
  
  backtrack(0,[])

  return ans

nums = [3,1,2]
print(subsets(nums))




#-----------------------------------------------#





def subsetSumK(nums,k):
  cnt = [0]   
  ans = [] 
  def rec(i,seq,sum):
    if i>= len(nums):
      if sum == k: 
        ans.append(seq[:])
        cnt[0]+=1
      return
    sum+=nums[i]
    seq.append(nums[i])
    rec(i+1, seq, sum) #pick
    seq.pop()
    sum-=nums[i]
    rec(i+1, seq, sum) #not pick
  rec(0,[],0)
  return ans
  # return cnt[0]


print(subsetSumK([1,2,1],2))

def subsetFirstSumK(nums,k):

  def rec(i,seq,sum):
    if i>= len(nums):
      if sum == k: 
        print('first sum: ', seq)
        return True
      else: return False

    sum+=nums[i]
    seq.append(nums[i])

    if (rec(i+1,seq, sum)==True): return True #pick

    seq.pop()
    sum-=nums[i]

    if (rec(i+1,seq, sum)==True): return True #not pick

    return False
  
  return rec(0,[],0)

print(subsetFirstSumK([1,2,1],2))


def subsetSumKCount(nums,k):
  def rec(i,sum):
    if sum>k: return 0 # only if the array contains positives
    if i>= len(nums):
      if sum == k: return 1
      else: return 0
    
    sum+=nums[i]
    l = rec(i+1, sum) #pick
    sum-=nums[i]
    r = rec(i+1, sum) #not pick
    return l+r
  
  return 'count is: ', rec(0,0)
  # return cnt[0]


print(subsetSumKCount([1,2,1],2))


