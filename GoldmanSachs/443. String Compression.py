# Time complexity: O(n)O(n)O(n).

# All cells are initially white. We will repaint each white cell blue, and we may repaint some blue cells green. Thus each cell will be repainted at most twice. Since there are nnn cells, the total number of repaintings is O(n)O(n)O(n).

# Space complexity: O(1)O(1)O(1).

# We store only a few integer variables and the string representation of groupLength which takes up O(1)O(1)O(1) space.
class Solution:
  def compress(self, chars) -> int:
    res = 0
    i = 0
    n = len(chars)
    while i < n:
      cnt = 1
      while i+cnt<n and chars[i+cnt] == chars[i]:
        cnt+=1
      chars[res] = chars[i]
      res+=1
      if cnt>1:
        cnt = str(cnt)
        #if repeated 10 times then 0:0+2 since 10 has 2 chars
        chars[res:res+len(cnt)] = cnt
        res+=len(cnt)
      i+=int(cnt)
    return res
      
