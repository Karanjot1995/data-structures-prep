from math import e, log

#TC -> O(N)
def mySqrt(x: int) -> int:
  if x<2: return x
  left = int(e**(0.5 * log(x)))
  right = left+1
  # print(left)
  return left if right*right>x else right

print(mySqrt(1024))

#TC -> O(logN)
def mySqrt(self, x: int) -> int:
  if x<2: return x

  l,r = 2, x//2
  while l<=r:
    mid = l + (r-l)//2
    print(mid, l+r>>1)
    num = mid*mid
    if num>x: r = mid-1
    elif num<x: l = mid+1
    else: return mid
  
  return r