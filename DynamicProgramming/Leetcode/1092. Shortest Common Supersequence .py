'''

brute groot
3+3+2
bgruoote

m-lcs + (n-lcs) + lcs
total = m+n-lcs

'''

def shortestCommonSupersequence(word1, word2):
  if word1 == word2: return word1
  m,n = len(word1), len(word2)
  dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

  for i in range(1,m+1):
    for j in range(1,n+1):
      if word1[i-1]==word2[j-1]:
        dp[i][j] = 1+dp[i-1][j-1]
      else:
        dp[i][j] = max(dp[i-1][j],dp[i][j-1])
  
  i,j = m,n
  ans = ""
  while i>0 and j>0:
    if word1[i-1]==word2[j-1]:
      ans += word1[i - 1]
      i-=1
      j-=1
    elif dp[i - 1][j] > dp[i][j - 1]:
      ans += word1[i - 1]
      i-=1
    else:
      ans += word2[j - 1]
      j-=1

  #Adding Remaing Characters - Only one of the below two while loops will run 
  while i>0:
    ans += word1[i - 1]
    i -= 1

  while j > 0:
    ans += word2[j - 1]
    j -= 1

  return ans[::-1]

print(shortestCommonSupersequence("brute", "groot"))

# def shortestCommonSupersequence(word1, word2):
#   if word1 == word2: return ""
#   m,n = len(word1), len(word2)

#   sup = ""
#   def rec(i1, i2):
#     if i1 >= len(word1) or i2 >= len(word2): return ""
#     if word1[i1] == word2[i2]:
#       return word1[i1] + rec(i1+1, i2+1)
    
#     w= word1[i1]+word2[i2]
#     r1 = rec(i1,i2+1)
#     r2 = rec(i1+1,i2)
#     if len(r1)<len(r2):
#       return w+r1
#     else:
#       return w+r2
      
#   res = rec(0, 0)
#   print(res)
#   # return m + n - res


# [['', '', '', '', '', ''], 
#  ['', '', '', '', '', ''], 
#  ['', '', 'r', 'r', 'r', 'r'], 
#  ['', '', 'r', 'r', 'r', 'r'], 
#  ['', '', 'r', 'r', 'r', 'tr'], 
#  ['', '', 'r', 'r', 'r', 'tr']]

[[0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0], 
 [0, 0, 1, 1, 1, 1], 
 [0, 0, 1, 1, 1, 1], 
 [0, 0, 1, 1, 1, 2], 
 [0, 0, 1, 1, 1, 2]]