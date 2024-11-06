def numDistinct(s: str, t: str):
  m,n = len(s), len(t)

  def rec(i1,i2):
    if i2>=n: return 1
    if i1>=m: return 0
    if s[i1] == t[i2]:
        moveOne = rec(i1+1, i2+1)
        stay = rec(i1+1, i2)
        return moveOne + stay
    else:
       # If the characters don't match, we can only skip the character in s1
        return rec(i1 + 1, i2)
    
  return rec(0,0)
       
s = "babgbag"
t = "bag"
print(numDistinct(s,t))



'''
Time Complexity: O(N*M)
Reason: There are N*M states therefore at max N*M new problems will be solved.

Space Complexity: O(N*M) + O(N+M)
Reason: We are using a recursion stack space(O(N+M)) and a 2D array (O(N*M)).
'''
def numDistinctMemo(s: str, t: str) -> int:
  m,n = len(s), len(t)
  dp = [[-1 for _ in range(n)] for _ in range(m)]

  def rec(i1,i2):
    if i2>=n: return 1
    if i1>=m: return 0
    if dp[i1][i2]!=-1: return dp[i1][i2]
    if s[i1] == t[i2]:
        #move to complete matching current substring
        move = rec(i1+1, i2+1)
        #stay on the current i2 and just move i1 to find more possible matches
        stay = rec(i1+1, i2)

        dp[i1][i2] = move + stay
    else:
      # If the characters don't match, we can only skip the character in s1
        dp[i1][i2] = rec(i1 + 1, i2)
    return dp[i1][i2]
    
  ans = rec(0,0)
  return ans

print(numDistinctMemo(s,t))


def numDistinctTab(s: str, t: str) -> int:
  m,n = len(s), len(t)
  dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]

  for j in range(n+1): dp[0][j] = 0
  for i in range(m+1): dp[i][0] = 1

  for i in range(1,m+1):
     for j in range(1,n+1):
        dp[i][j] = dp[i-1][j]
        if s[i-1] == t[j-1]:
           dp[i][j] += dp[i-1][j-1]
  print(dp)
  return dp[m][n]

print("Tabulation: ",numDistinctTab(s,t))


# [[1, 0, 0, 0], 
#  [1, 1, 0, 0], 
#  [1, 1, 1, 0], 
#  [1, 2, 1, 0], 
#  [1, 2, 1, 1], 
#  [1, 3, 1, 1], 
#  [1, 3, 4, 1], 
#  [1, 3, 4, 5]]