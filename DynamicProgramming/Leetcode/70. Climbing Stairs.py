def climbStairs(n: int) -> int:
  dp = [-1]*(n+1)
  def climb(i):
    if i > n: return 0
    if i == n: return 1

    if dp[i] !=- 1: return dp[i]

    op = climb(i+1)+climb(i+2)
    dp[i] = op
    return op

  return climb(0)
print("recursive: ", climbStairs(5))



def climbStairs2(n: int) -> int:
  dp = [-1]*(n+1)

  def climb(i):
    if i <= 1: return 1

    if dp[i] !=- 1: return dp[i]

    op = climb(i-1)+climb(i-2)
    dp[i] = op
    return op

  return climb(n)

print('rec backwards: ', climbStairs2(5))



def climbStairs3(n: int) -> int:
  if n == 1: return 1
  dp = [-1]*(n+1)
  dp[1] = 1
  dp[2] = 2

  for i in range(3,n+1):
    dp[i] = dp[i-1]+dp[i-2]
  return dp[n]
print(climbStairs3(5))


# tabulation with O(N) space
def climbStairs4(n: int) -> int:
  if n == 1: return 1
  dp = [-1]*(n+1)
  dp[1] = 1
  dp[2] = 2

  for i in range(3,n+1):
    dp[i] = dp[i-1]+dp[i-2]
  return dp[n]

print(climbStairs4(5))


# tabulation with constant space
def climbStairs5(n: int) -> int:
  prev2 = 1
  prev = 2
  for i in range(2,n+1):
    curr = prev+prev2
    prev2 = prev
    prev = curr
  return prev2

print(climbStairs5(5))
