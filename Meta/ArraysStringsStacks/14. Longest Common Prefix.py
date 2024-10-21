# https://leetcode.com/problems/longest-common-prefix/

'''
- Take one string and heck all its char in every other string simultaneously
- Handle edge cases when on string is shorten than other so it is possible to go out of bounds

TC - O(N) where N is the avg size
SC - O(M) where M is the len of longest common prefix
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      for i in range(len(strs[0])):
        c = strs[0][i]
        for s in strs:
          if i == len(s) or s[i]!=c: return strs[0][0:i]

      return strs[0]
    
      # ans = ""
      
      # for i in range(len(strs[0])):
      #     for s in strs:
      #         if i == len(s) or s[i] != strs[0][i]:
      #             return ans
      #     ans += strs[0][i]
      # return ans

'''
SORTING
- Sort the strings and compare the first and last word

TC - O(NlogN)
SC - O(1)

Following is in sorted -- so prefix comes first -- "CLU"
CLUB
CLUE
CLUMSY
CLUSTER
CLUTCH
'''
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        # Sort the array
        strs.sort()
        
        # Get the first and last strings
        first = strs[0]
        last = strs[-1]
        
        result = []
        
        # Start comparing
        for i in range(len(first)):
            if i < len(last) and first[i] == last[i]:
                result.append(first[i])
            else:
                break
        
        return ''.join(result)