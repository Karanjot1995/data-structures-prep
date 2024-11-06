# Time Complexity: O(N*M)
# Reason: There are two nested loops
# Space Complexity: O(N*M)
# Reason: We are using an external array of size ‘N*M)’. Stack Space is eliminated.

def longestCommonSubstring(s1,s2):
  m,n = len(s1), len(s2)
  dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

  ans = 0
  for i in range(1,m+1):
     for j in range(1,n+1):
        if s1[i-1] == s2[j-1]: 
          dp[i][j] = 1 + dp[i-1][j-1]
          ans = max(ans,dp[i][j])
        else:
           dp[i][j] = 0
  return ans
    


print("Tabulation: ",longestCommonSubstring("wasdijkll", "wsdjkll"))


#recursive 
# def longestCommonSubsequenceRec(s1: str, s2: str) -> int:

#   def rec(i1, i2, count):
#     if i1 >= len(s1) or i2 >= len(s2): return count
#     if s1[i1] == s2[i2]: count = rec(i1+1,i2+1,count+1)
#     else: count= max(count, max(rec(i1+1,i2,0),rec(i1,i2+1,0)))
#     return count
#   return rec(0, 0, 0)

# print(longestCommonSubsequenceRec("wasdijkll", "wsdjkl"))


# def longestCommonSubsequence(s1: str, s2: str) -> int:
#   m,n = len(s1), len(s2)
#   dp = [[-1 for _ in range(n)] for _ in range(m)]
#   def rec(i1, i2, count):
#     if i1 >= len(s1) or i2 >= len(s2): return count
#     if dp[i1][i2]!=-1: return dp[i1][i2]

#     if s1[i1] == s2[i2]: count = rec(i1+1,i2+1,count+1)
#     count= max(count, max(rec(i1+1,i2,0),rec(i1,i2+1,0)))
#     dp[i1][i2] = count
#     return count

#   ans = rec(0, 0, 0)

#   return ans

# print("Memo: ",longestCommonSubsequence("wasdijkll", "wsdjkl"))




