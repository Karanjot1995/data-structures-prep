class Solution:
  def longestValidSubstring(self, word: str, forbidden) -> int:
    f=set(forbidden)
    res=left=0
    for i in range (len(word)):
      for j in range (max(left,i-9),i+1):
        if word[j:i+1] in f:
          left=j+1
      res=max(res,i-left+1)
    return res
    

# Input: word = "cbaaaabc", forbidden = ["aaa","cb"]
# Output: 4
# Explanation: There are 11 valid substrings in word: "c", "b", "a", "ba", "aa", "bc", "baa", "aab", "ab", "abc" and "aabc". The length of the longest valid substring is 4. 
# It can be shown that all other substrings contain either "aaa" or "cb" as a substring. 