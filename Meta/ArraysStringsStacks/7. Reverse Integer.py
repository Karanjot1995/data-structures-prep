'''
Time Complexity: O(log(x)). There are roughly log10(x) digits in x.
Space Complexity: O(1).
'''


class Solution:
  # def reverse(self, x: int) -> int:
  #   sign = [1,-1][x<0]
  #   rev,x = 0, abs(x)
  #   while x:
  #     x, dig = divmod(x,10)
  #     rev = rev*10+dig
  #     if rev > 2**31-1: return 0
  #   return sign*rev

  def reverse(self, x: int) -> int:
    sign = -1 if x<0 else 1
    x = abs(x)
    rev = 0
    while x:
      dig = x%10
      x //= 10
      rev = rev*10+dig
      if rev > 2**31-1: return 0
      # if (rev > (2**31-1)//10) or (rev == (2**31-1)//10 and dig == 7): return 0
    
    return sign*rev
        