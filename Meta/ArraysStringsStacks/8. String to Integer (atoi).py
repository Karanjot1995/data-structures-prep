class Solution:
  def myAtoi(self, s: str) -> int:
    num = ''
    sign = ''
    prev = ''
    s = s.lstrip()
    
    mini = -pow(2,31)
    maxi = pow(2,31)-1

    for char in s:
      if not prev and char.isdigit():
        num+=char
      elif char == '-' and not num and not sign:
        sign = -1
      elif char == '+' and not num and not sign:
        sign = 1
      elif not char.isdigit():
        prev = char
    
    if not sign: sign = 1
    if num: num = sign*int(num)

    if num and num> maxi : return maxi
    elif num and num < mini: return mini

    return num if num else 0