


def isMatch(s: str, p: str):  
  m,n = len(s), len(p)
  dp = [[-1 for _ in range(n)] for _ in range(m)]

  #i1 is j and i2 is i for strivers video
  def rec(i1, i2):
    if i1==m and i2==n: return True
    if i2==n and i1<m: return False
    if i1 == m and i2<n:
      for i in range(i2,n):
        if p[i]!="*": return False
      return True
    if dp[i1][i2]!=-1: return dp[i1][i2]

    if s[i1] == p[i2] or p[i2]=="?":
      dp[i1][i2] = rec(i1+1, i2+1)
    elif p[i2]=="*": 
      move_s = rec(i1+1, i2)
      move_p = rec(i1, i2+1)
      dp[i1][i2] = move_s or move_p
    else: dp[i1][i2] = False
    return dp[i1][i2]
  ans = rec(0,0)

  print(dp)
  return ans


# s = "baxy"
# p = "b?xy"
# s = "aa"
# p = "a"
s = "adceb"
p = "*a*b"
# s = "acdcb"
# p = "a*c*b"
print(isMatch(s,p))


def isAllStars(S1, i):
    for j in range(1, i + 1):
        if S1[j - 1] != '*':
            return False
    return True

def isMatchTab(s: str, p: str):  
  m = len(s)
  n = len(p)

  dp = [[False for _ in range(m+1)] for _ in range(n + 1)]
  dp[0][0] = True

  for j in range(1, m+1):
    dp[0][j] = False

  for i in range(1, n + 1):
    dp[i][0] = isAllStars(p, i)

  for i in range(1, n + 1):
    for j in range(1, m+1):
      if p[i - 1] == s[j - 1] or p[i - 1] == '?':
        dp[i][j] = dp[i - 1][j - 1]
      elif p[i - 1] == '*':
        dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
      else:
        dp[i][j] = False

  return dp[n][m]


print(isMatchTab(s,p))

[[True, False, False, False, False], 
 [False, False, False, False, False], 
 [False, False, False, False, False], 
 [False, False, False, False, False], 
 [False, False, False, False, False], 
 [False, False, False, False, False]]

  # for i in range(1,n+1):
  #   flag = True
  #   for k in range(i+1):
  #     if p[k-1]!="*": flag = False
  #     break
  #   dp[i][0] = flag
# [[True, False, False, False, False, False], 
#  [False, -1, -1, -1, -1, -1], 
#  [True, -1, -1, -1, -1, -1], 
#  [False, -1, -1, -1, -1, -1], 
#  [False, -1, -1, -1, -1, -1], 
#  [False, -1, -1, -1, -1, -1]]

  
  


