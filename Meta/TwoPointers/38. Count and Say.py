class Solution:
  def countAndSayRecursive(self, n: int) -> str:
    if n == 1: return "1"

    prev = self.countAndSay(n-1)
    res = ''
    j=0
    while j<len(prev):
      cnt=1
      while j+1< len(prev) and prev[j] == prev[j+1]:
        cnt+=1
        j+=1
      res+=str(cnt)+prev[j]
      j+=1
    return res

  def countAndSayIterative(self, n: int) -> str:
    if n == 1: return "1"

    prev = '1'
    for i in range(n-1):
      res = ''
      j=0
      while j<len(prev):
        cnt=1
        while j+1< len(prev) and prev[j] == prev[j+1]:
          cnt+=1
          j+=1
        res+=str(cnt)+prev[j]
        j+=1
      prev = res
    return res


        