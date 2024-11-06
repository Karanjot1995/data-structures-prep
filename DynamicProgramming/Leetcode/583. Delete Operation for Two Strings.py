# del = m - len(lcs)
# insert = n - len(lcs)
# total = m+n-2(lcs)


'''
Time complexity : O(2 max(m,n)). Size of recursion tree will be 2 (m+n). 
Here, m and n refer to the lengths of s1 and s2 respectively.
Space complexity : O(max(m,n)). The depth of the recursion tree will go upto max(m,n).
'''
def minDistanceRec(word1, word2):
  def rec(i1, i2):
    if i1 >= len(word1) or i2 >= len(word2): return 0
    if word1[i1] == word2[i2]:
        return 1 + rec(i1 + 1, i2 + 1)
    return max(rec(i1,i2+1), rec(i1+1,i2))
  
  res = rec(0, 0)
  return len(word1)+len(word2) - 2*res


word1 = "abcd"
word2 = "anc"
print(minDistanceRec(word1, word2))

'''
Time complexity : O(m∗n). memo array of size mxn needs to be filled once. 
Here, m and n refer to the length of the strings s1 and s2 respectively.

Space complexity : O(m∗n). memo array of size mxn is used. 
Also, The depth of the recursion tree will go upto max(m,n).
'''
def minDistanceMemo(word1, word2):
  if word1 == word2: return 0
  m,n = len(word1), len(word2)
  dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]

  def rec(i1, i2):
    if i1 >= len(word1) or i2 >= len(word2): return 0
    if dp[i1][i2]!=-1: return dp[i1][i2]
    if word1[i1] == word2[i2]:
      dp[i1][i2] = 1 + rec(i1 + 1, i2 + 1)
    else: 
      dp[i1][i2] = max(rec(i1,i2+1), rec(i1+1,i2))
    return dp[i1][i2]
  
  res = rec(0, 0)
  return m + n - 2*res


print(minDistanceMemo(word1, word2))


#Space complexity : O(m∗n). dp array of size mxn is used.
#Tabulation with shifting
def minDistanceTab(word1, word2):
  if word1 == word2: return 0
  m,n = len(word1), len(word2)
  dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

  for i in range(1,m+1):
    for j in range(1,n+1):
        if word1[i-1] == word2[j-1]: 
          dp[i][j] = 1 + dp[i-1][j-1]
        else: 
          dp[i][j] = max(dp[i-1][j],dp[i][j-1])

  return m+n - 2*dp[m][n]

print(minDistanceTab(word1, word2))