
def minInsertionsRec(s: str) -> int:
  s1 = s
  s2 = s[::-1]
  def rec(i1, i2):
    if i1 >= len(s1) or i2 >= len(s2): return 0
  
    if s1[i1] == s2[i2]:
        return 1 + rec(i1 + 1, i2 + 1)
    return max(rec(i1,i2+1), rec(i1+1,i2))
  
  return len(s) - rec(0, 0)


def minInsertions(s: str) -> int:
  s1 = s
  s2 = s[::-1]
  n = len(s)
  dp = [[-1 for _ in range(n)] for _ in range(n)]

  def rec(i1, i2):
    if i1 >= len(s1) or i2 >= len(s2): return 0
    if dp[i1][i2]!=-1: return dp[i1][i2]

    if s1[i1] == s2[i2]: dp[i1][i2] = 1 + rec(i1 + 1, i2 + 1)
    else: dp[i1][i2] = max(rec(i1,i2+1), rec(i1+1,i2))

    return dp[i1][i2]
  
  return n - rec(0, 0)



#Tabulation with shifting
def minInsertionsTab(s) -> int:
  s1 = s
  s2 = s[::-1]
  n = len(s)
  dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]

  for i in range(n):
    dp[i][0] = 0
    dp[0][i] = 0

  for i in range(1,n+1):
     for j in range(1,n+1):
        if s1[i-1] == s2[j-1]: 
          dp[i][j] = 1 + dp[i-1][j-1]
        else: 
          dp[i][j] = max(dp[i-1][j],dp[i][j-1])

  return n - dp[n][n]
print(minInsertionsTab("mbadm"))

# Input: s = "mbadm"
# Output: 2
# Explanation: String can be "mbdadbm" or "mdbabdm"



