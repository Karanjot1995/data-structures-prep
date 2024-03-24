# solution https://leetcode.com/problems/integer-break/solutions/4135963/faster-lesser-4-methods-simple-math-dynamic-programming-greedy-approach-memoization/


def integerBreak1(self, n: int) -> int:
  if n<=3: return n-1
  dp = [-1] * (n + 1)

  def solve(num):
    if dp[num]!=-1: return dp[num]
    if num == 1: return 1

    res = -float('inf')
    for i in range(1, num):
      res = max(res, i * solve(num-i), i * (num-i))
    dp[num] = res

    return res

  return solve(n)


def integerBreak2(self, n: int) -> int:
  if n<=3: return n-1
  ans = 1
  while n>4:
    ans*=3
    n-=3
  return ans*n

def integerBreak3(self, n: int) -> int:
  if n <=3: return n-1
  q = n//3
  r = n%3

  if r == 0: return 3**q
  elif r == 1: return (3**(q-1))*4
  else: return (3**q)*2


print(integerBreak1(10))
print(integerBreak2(10))
print(integerBreak3(10))