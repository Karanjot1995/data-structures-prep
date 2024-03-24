# TC - O(2^n)

def partition(s: str):
  ans = []

  def isPalindrome(start,end):
    while start<=end:
      if s[start]!=s[end]:return False
      start+=1
      end-=1
    return True

  def backtrack(idx, arr):
    if idx == len(s): 
      ans.append(arr.copy())
      return
    j = idx
    while j<len(s):
      if isPalindrome(idx,j): 
        arr.append(s[idx:j+1])
        backtrack(j+1, arr)
        arr.pop()
      j+=1
    return
  backtrack(0,[])

  # def isPalindrome(substr):
  #   n = len(substr)
  #   for i in range(n):
  #     if substr[i]!=substr[n-i-1]:return False
  #   return True

  # def backtrack(substr, arr):
  #   if not substr: 
  #     ans.append(arr.copy())
  #     return
  #   i=j=0
  #   while j<len(substr):
  #     if isPalindrome(substr[i:j+1]): 
  #       arr.append(substr[i:j+1])
  #       backtrack(substr[j+1:], arr)
  #       arr.pop()
  #     j+=1
  #   return
  # backtrack(s,[])

  return ans
      
print(partition('aabb'))

print(len("|||||*|||*|||*||||*||||**|*|||**|**||**|||*|||*||***||*|*||"))