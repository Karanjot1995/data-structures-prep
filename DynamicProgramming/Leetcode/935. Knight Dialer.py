# Time complexity: O(n)
# Space complexity: O(n)


# memoization
def knightDialer(n: int) -> int:
  jumps = [[4, 6],[6, 8],[7, 9],[4, 8],[3, 9, 0],[],[1, 7, 0],[2, 6],[1, 3],[2, 4]]
  dp = [[1 if j==0 else 0 for _ in range(10)] for j in range(n)]
  # @cache
  def dfs(remain, square):
    if dp[remain][square]: return dp[remain][square]
    if remain == 0: return 1
    res = 0
    for next_square in jumps[square]:
      res = (res+dfs(remain-1, next_square))%MOD
    dp[remain][square] = res
    return res

  ans = 0
  MOD = 10 ** 9 + 7
  for square in range(10):
    ans = (ans+dfs(n-1,square))%MOD

  return ans


# tabulation
def knightDialer2(n: int) -> int:
  jumps = [[4, 6],[6, 8],[7, 9],[4, 8],[3, 9, 0],[],[1, 7, 0],[2, 6],[1, 3],[2, 4]]
  dp = [[1 if j==0 else 0 for _ in range(10)] for j in range(n)]
  MOD = 10 ** 9 + 7
  
  for remain in range(1,n):
    for square in range(10):
      res = 0
      for next_square in jumps[square]:
        res = (res + dp[remain-1][next_square])%MOD
      dp[remain][square] = res

  ans = 0
  for square in range(10):
    ans = (ans + dp[n - 1][square]) % MOD
  return ans


n = 2
# Output: 20
# Explanation: All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]
print(knightDialer(n))
print(knightDialer2(n))
  

