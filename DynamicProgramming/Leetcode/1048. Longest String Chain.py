
def compare(sub, string):
  if len(string)!=len(sub)+1: return False
  i = 0
  for char in string:
      if i < len(sub) and char == sub[i]:
          i += 1
  return i == len(sub)
  # i = j = 0
  # while i<len(string):
  #   if j<len(sub) and string[i] == sub[j]:
  #     i+=1
  #     j+=1
  #   else: i+=1
  # return i==len(string) and j == len(sub)


'''
TC - NxN x L (length of string)
'''
def longestStrChain(words) -> int:
  n = len(words)
  words = sorted(words, key=len)

  def rec(i, prev_i):
    if i == len(words): return 0
    
    take = float("-inf")
    if prev_i == -1 or compare(words[prev_i], words[i]): 
      take = 1 + rec(i+1, i)

    not_take = 0+rec(i+1, prev_i)
    return max(take, not_take)
  
  return rec(0,-1)

words = ["a","b","ba","bca","bda","bdca"]

print(longestStrChain(words))



def longestStrChainMemo(words) -> int:
  n = len(words)
  words = sorted(words, key=len)
  dp = [[-1 for _ in range(n+1)] for _ in range(n)]

  def rec(i, prev_i):
    if i == len(words): return 0
    if dp[i][prev_i+1]!=-1: return dp[i][prev_i+1]
    
    take = float("-inf")
    if prev_i == -1 or compare(words[prev_i], words[i]): 
      take = 1 + rec(i+1, i)

    not_take = 0+rec(i+1, prev_i)
    dp[i][prev_i+1] = max(take, not_take)
    return dp[i][prev_i+1]
  
  return rec(0,-1)

          
words = ["a","b","ba","bca","bda","bdca"]

print(longestStrChainMemo(words))



#space optimized
def longestStrChainMemo(words) -> int:
  if not words: return 0
  n = len(words)
  words = sorted(words, key=len)
  dp = [1]*n

  for i in range(1,n):
    for prev in range(0,i):
      if compare(words[prev],words[i]): 
        dp[i] = max(dp[i], dp[prev]+1)
  return max(dp)


words = ["a","b","ba","bca","bda","bdca"]

print(longestStrChainMemo(words))