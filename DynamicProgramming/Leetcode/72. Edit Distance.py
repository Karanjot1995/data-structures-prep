
word1 = "horse"
word2 = "ros"

def minDistance(word1: str, word2: str):
  m = len(word1)
  n = len(word2)

  def rec(i1,i2):
    if i1 == m: return n-i2 #remaining chars in word2
    if i2 == n: return m-i1
    if word1[i1] == word2[i2]:
      return 0 + rec(i1+1, i2+1)
    else:
      # insert at i so i still remains the same but the i2 moves
      ins = 1 + rec(i1,i2+1)
      de = 1 + rec(i1+1,i2)
      rep = 1 + rec(i1+1,i2+1)

      return min(ins, de, rep)
    
  return rec(0,0)
    
print(minDistance(word1, word2))




def minDistanceMemo(word1: str, word2: str) -> int:
  m = len(word1)
  n = len(word2)
  dp = [[-1 for _ in range(n)] for _ in range(m)]

  def rec(i1,i2):
    if i1 == m: return n-i2 #remaining chars in word2
    if i2 == n: return m-i1
    if dp[i1][i2] != -1: return dp[i1][i2]

    if word1[i1] == word2[i2]:
      dp[i1][i2] = 0 + rec(i1+1, i2+1)
    else:
      # insert at i so i still remains the same but the i2 moves
      ins = rec(i1,i2+1)
      de = rec(i1+1,i2)
      rep = rec(i1+1,i2+1)

      dp[i1][i2] = 1 + min(ins, de, rep)
    return dp[i1][i2]
    
  ans = rec(0,0)
  print(dp)
  return ans
word1 = "horse"
word2 = "ros"
print(minDistanceMemo(word1, word2))
[[3, 3, 4], 
 [3, 2, 3], 
 [2, 2, 2], 
 [-1, 2, 1], 
 [-1, 2, 1]]


def minDistanceTab(word1: str, word2: str) -> int:
  m = len(word1)
  n = len(word2)
  dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]

  for i in range(m+1): dp[i][0] = dp[i][0] = i
  for j in range(n+1): dp[0][j] = dp[0][j] = j

  for i in range(1,m+1):
    for j in range(1, n+1):
      if word1[i-1] == word2[j-1]:
         dp[i][j] = 0 + dp[i-1][j-1]
      else:
        dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])

  
  print(dp)
  return dp[m][n]

  # def rec(i1,i2):
  #   if i1 == m: return n-i2 #remaining chars in word2
  #   if i2 == n: return m-i1
  #   if dp[i1][i2] != -1: return dp[i1][i2]

  #   if word1[i1] == word2[i2]:
  #     dp[i1][i2] = 0 + rec(i1+1, i2+1)
  #   else:
  #     # insert at i so i still remains the same but the i2 moves
  #     ins = 1 + rec(i1,i2+1)
  #     de = 1 + rec(i1+1,i2)
  #     rep = 1 + rec(i1+1,i2+1)

  #     dp[i1][i2] = min(ins, de, rep)
  #   return dp[i1][i2]
    
  # return rec(0,0)
      
print(minDistanceTab(word1, word2))
[[0, 1, 2, 3], 
 [1, -1, -1, -1], 
 [2, -1, -1, -1], 
 [3, -1, -1, -1], 
 [4, -1, -1, -1], 
 [5, -1, -1, -1]]

[[0, 1, 2, 3], 
 [1, 1, 2, 3], 
 [2, 2, 1, 2], 
 [3, 2, 2, 2], 
 [4, 3, 3, 2], 
 [5, 4, 4, 3]]
