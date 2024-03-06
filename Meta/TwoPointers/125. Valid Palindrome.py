# https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome1(self, s: str) -> bool:
        if not s: return True

        S = ""

        for char in s:
            if char != " " and char.isalnum():
                S += char.lower()
        
        return S == S[::-1]
    
    # TC - O(N) | SC - O(1)
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            # ignore non-alphanumeric characters
            while i < j and not s[i].isalnum():
                i += 1
            
            # ignore non-alphanumeric characters
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True