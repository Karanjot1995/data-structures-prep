def validPalindrome(self, s: str) -> bool:
  i = 0
  j = len(s)-1
  self.cnt = 0

  def isValid(s,i,j):
    while i<j:
      if s[i]!=s[j]:
        self.cnt+=1
        if self.cnt>1: return False
        #move one from left or right and check again
        return isValid(s,i+1,j) or isValid(s,i,j-1)
      else:
        i+=1
        j-=1
    return True

  return isValid(s,i,j)

s = "aba"   #op = True
# s = "abca"   #op = True just delete one
# s = "cabbcc"  # False as we will have to delete more than one
print(validPalindrome(s))