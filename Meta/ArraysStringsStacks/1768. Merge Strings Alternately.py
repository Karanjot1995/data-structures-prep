class Solution:
    '''
    APPROACH 1: TWO POINTER

    TC - O(m + n)
    SC - O(1)
    '''
    def mergeAlternately1(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        i = j = 0
        ans = []

        while i < m or j < n:
            if i < m:
                ans += word1[i]
                i += 1
            if j < n:
                ans += word2[j]
                j += 1

        return "".join(ans)
    
    '''
    APPROACH 2: ONE POINTER

    TC - O(m + n)
    SC - O(1)
    '''
    def mergeAlternately(self, word1, word2):
        n = max(len(word1), len(word2))
        ans = []

        for i in range(n):
            if i < len(word1):
                ans += word1[i]
            if i < len(word2):
                ans += word2[i]

        return "".join(ans)