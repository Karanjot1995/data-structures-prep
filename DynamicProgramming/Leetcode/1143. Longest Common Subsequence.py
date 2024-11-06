#recursive 
def longestCommonSubsequenceRec(s1: str, s2: str) -> int:
  m,n = len(s1), len(s2)

  def rec(i1, i2):
    if i1 >= len(s1) or i2 >= len(s2): return 0
    
    if s1[i1] == s2[i2]:
        return 1 + rec(i1+1, i2+1)
    
    return max(rec(i1, i2 + 1), rec(i1 + 1, i2))
  
  return rec(0, 0)




def longestCommonSubsequence(text1: str, text2: str) -> int:
  m,n = len(text1), len(text2)
  dp = [[-1 for _ in range(n)] for _ in range(m)]

  def rec(s1, s2, ind1, ind2):
    if ind1 >= len(s1) or ind2 >= len(s2): return 0
    # print(ind1, ind2)
    if dp[ind1][ind2] != -1: return dp[ind1][ind2]
    
    if s1[ind1] == s2[ind2]:
        dp[ind1][ind2] = 1 + rec(s1, s2, ind1 + 1, ind2 + 1)
    else:
        dp[ind1][ind2] = 0 + max(rec(s1, s2, ind1, ind2 + 1), rec(s1, s2, ind1 + 1, ind2))
    return dp[ind1][ind2]
  
  return rec(text1, text2, 0, 0)


#with shifting
def longestCommonSubsequenceTabulation(text1: str, text2: str) -> int:
  m,n = len(text1), len(text2)
  dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]

  for i in range(m):dp[i][0] = 0
  for j in range(n):dp[0][j] = 0

  for i in range(1,m+1):
     for j in range(1,n+1):
        if text1[i-1] == text2[j-1]: dp[i][j] = 1 + dp[i-1][j-1]
        else:
           dp[i][j] = max(dp[i-1][j],dp[i][j-1])

  print(dp)
  return dp[m][n]
print(longestCommonSubsequenceTabulation("abde", "abdg"))


#without shifting
def longestCommonSubsequenceTabulation(text1: str, text2: str) -> int:
  m,n = len(text1), len(text2)
  dp = [[-1 for _ in range(n)] for _ in range(m)]

  for i in range(m):
     if i<len(text2) and text1[i] == text2[i]: dp[i][0]=1
     else: dp[i][0] = 0

  for j in range(n):
    if j<len(text1) and text1[j] == text2[j]: dp[0][j]=1
    else: dp[0][j] = 0

  for i in range(1,m):
     for j in range(1,n):
        if text1[i] == text2[j]: dp[i][j] = 1 + dp[i-1][j-1]
        else:
           dp[i][j] = max(dp[i-1][j],dp[i][j-1])

  print(dp)
  return dp[m-1][n-1]

print(longestCommonSubsequenceTabulation("abde", "abdg"))



#############    Printing    ###################

def longestCommonSubsequencePrintTab(text1: str, text2: str) -> int:
  m,n = len(text1), len(text2)
  dp = [["" for _ in range(n+1)] for _ in range(m+1)]

  for i in range(1,m+1):
     for j in range(1,n+1):
        print(text1[i-1], text1[i-1] == text2[j-1])
        if text1[i-1] == text2[j-1]: dp[i][j] = text1[i-1] + dp[i-1][j-1]
        else:
           dp[i][j] = dp[i-1][j] if len(dp[i-1][j]) > len(dp[i][j-1]) else dp[i][j-1]

  return dp[m][n][::-1]

def longestCommonSubsequencePrintMemo(text1: str, text2: str) -> int:

  m,n = len(text1), len(text2)
  dp = [[-1 for _ in range(n)] for _ in range(m)]

  def rec(s1, s2, ind1, ind2):
    if ind1 >= len(s1) or ind2 >= len(s2): return ""
    if dp[ind1][ind2] != -1: return dp[ind1][ind2]
    
    if s1[ind1] == s2[ind2]:
        dp[ind1][ind2] = s1[ind1] + rec(s1, s2, ind1 + 1, ind2 + 1)
    else:
        rec1 = rec(s1, s2, ind1, ind2 + 1)
        rec2 = rec(s1, s2, ind1 + 1, ind2)
        
        dp[ind1][ind2] = "" + rec1 if len(rec1)> len(rec2) else rec2
    return dp[ind1][ind2]
  
  ans = rec(text1, text2, 0, 0)
  return ans

print(longestCommonSubsequencePrintTab("ababa", "cbbcad"))

# [['', '', '', '', '', '', ''], 
#  ['', '', '', '', '', 'a', 'a'], 
#  ['', '', 'b', 'b', 'b', 'b', 'b'], 
#  ['', '', 'b', 'b', 'b', 'ab', 'ab'], 
#  ['', '', 'b', 'bb', 'bb', 'bb', 'bb'], 
#  ['', '', 'b', 'bb', 'bb', 'abb', 'abb']]
