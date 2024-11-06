
# most optimal
def buildPalindromeDP(s, n, palindromeDP):
  for end in range(len(s)):
    for start in range(end + 1):
      if s[start] == s[end] and (end - start <= 2 or palindromeDP[start + 1][end - 1]):
        palindromeDP[start][end] = True

def minCut(s: str) -> int:
  n = len(s)
  dp = [0]*(n+1)
  palindromeDP = [[False] * len(s) for _ in range(len(s))]
  buildPalindromeDP(s, len(s), palindromeDP)

  for i in range(n-1,-1,-1):
    min_cost = float("inf")
    for j in range(i,n):
      if palindromeDP[i][j]: 
        cost = 1 + dp[j+1]
        min_cost = min(min_cost, cost)
    dp[i] = min_cost
  
  return dp[0]-1

s = "aaba"
print(minCut(s))


def minCut(s: str) -> int:
  n = len(s)
  def isPalin(i,j):
    while i<j:
      if s[i]!=s[j]: return False
      i+=1
      j-=1
    return True

  def rec(i):
    if i == n: return 0
    min_cost = float("inf")
    for j in range(i,n):
      if isPalin(i,j): 
        cost = 1 + rec(j+1)
        min_cost = min(min_cost, cost)
    return min_cost
      
  return rec(0)-1

s = "aab"
print(minCut(s))


#TC -> N states x N loops inside => NxN
#Sc -> N + N(recursive stack space)
def minCutMemo(s: str) -> int:
  n = len(s)
  dp = [-1]*n
  def isPalin(i,j):
    while i<j:
      if s[i]!=s[j]: return False
      i+=1
      j-=1
    return True

  def rec(i):
    if i == n: return 0
    min_cost = float("inf")
    if dp[i]!=-1: return dp[i]
    for j in range(i,n):
      if isPalin(i,j): 
        cost = 1 + rec(j+1)
        min_cost = min(min_cost, cost)
    dp[i] = min_cost
    return dp[i]
      
  return rec(0)-1

s = "aab"
print(minCutMemo(s))


def minCutTab(s: str) -> int:
  n = len(s)
  dp = [0]*(n+1)
  def isPalin(i,j):
    while i<j:
      if s[i]!=s[j]: return False
      i+=1
      j-=1
    return True

  for i in range(n-1,-1,-1):
    min_cost = float("inf")
    for j in range(i,n):
      if isPalin(i,j): 
        cost = 1 + dp[j+1]
        min_cost = min(min_cost, cost)
    dp[i] = min_cost
  
  return dp[0]-1

s = "aaba"
print(minCutTab(s))



