# Intuition
# Here, we can use binary search to look for the tightest upper bound. Given a value x, the condition for x to be a valid upper bound is that

# there is enough number between 1 to x that are not divisible by divisor1;
# there is enough number between 1 to x that are not divisible by divisor2;
# in the overlapping area, if some numbers are allocated to cover uniqueCnt1 they cannot be used to cover uniqueCnt2.


# Time complexity:O(log(uniqueCnt1 + uniqueCnt2))
from math import lcm

def minimizeSet(divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
  lo,hi = 0, 1<<32-1
  # x = 2**32 - 1
  # print(lo, hi)
  mult = lcm(divisor1, divisor2)
  while lo < hi: 
    mid = lo + hi >> 1
    if uniqueCnt1 <= mid - mid//divisor1 and uniqueCnt2 <= mid - mid//divisor2 and uniqueCnt1+uniqueCnt2 <= mid - mid//mult: hi = mid
    else: lo = mid+1
  return lo 



def minimizeSet(divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
  l, r = uniqueCnt1 + uniqueCnt2, 2 * int(1e9)
  def check(m):
      lcm = lcm(divisor1 * divisor2)
      #check the number we can use
      cnt = m - (m // divisor1 + m // divisor2 - m // lcm)
      u1 = max(0, uniqueCnt1 - (m // divisor2 - m // lcm))
      u2 = max(0, uniqueCnt2 - (m // divisor1 - m // lcm))
      return cnt >= u1 + u2

  while l < r:
      m = (l + r) // 2
      if check(m):
          r = m
      else:
          l = m + 1
  return l