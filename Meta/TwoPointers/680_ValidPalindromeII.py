# https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    '''
    * APPROACH 1: Brute Force
    * Remove each char and check if the string becomes a palindrome or not (after removing the char)
    * 
    * TC - O(N^2) | SC - O(1)
    '''
    
    '''
    * APPROACH 2: Optimal
    * 1) Take two pointers at 0, n - 1
    * 2) As soon as we find characters that are not equal i.e. s[left] != s[right] delete the left char and check if it 
    * is palindrome or delete the right char and check if the string now becomes palindrome or not and return from here
    *
    * TC - O(N) | SC - O(1)
    '''
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(string, i, j):
            while i <= j:
                if string[i] != string[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        i, j = 0, len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                return isPalindrome(s, i + 1, j) or isPalindrome(s, i, j - 1)
            
            i += 1
            j -= 1
        return True
    
'''
FOLLOW UP: How will you extend this to work for n changes (LC 1216: Valid Palindrome III)

ANSWER: Have a sub-function that compares left and right and calls recursively with a counter.


Solution 1: https://leetcode.com/problems/valid-palindrome-ii/solutions/632647/python-readable-and-intuitive-solution-generalizable-to-n-deletes/
Check Palindrome after k deletes (Generic Approach)
Approach: Recursion with a counter to check allowed deletes. For K deletes and check palindromes, change allowed_deletes = k.


def validPalindrome(self, s: str) -> bool:

    allowed_deletes = 1
    
    def check_palindrome(string, left, right, deletes):
        if left >= right: return True 
        
        if string[left] == string[right]:
            return check_palindrome(string, left + 1, right - 1, deletes)
        
        elif string[left] != string[right] and deletes < allowed_deletes:
            return check_palindrome(string, left + 1, right, deletes + 1) or \
                    check_palindrome(string, left, right - 1, deletes + 1)
         
        return False 

    return check_palindrome(s, 0, len(s)-1, 0)

Solution 2: ----(not verified code; source: LC editorial discuss)---

class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def helper(l, r, mismatches): 
            while l <= r: 
                if s[l] != s[r]: # mismatch 
                    return mismatches > 0 and (helper(l, r-1, mismatches - 1) or helper(l+1, r, mismatches - 1))
                l += 1
                r -= 1
            return True 

        return helper(0, len(s) - 1, 1)

Solution 3: https://leetcode.com/problems/valid-palindrome-ii/solutions/107717/c-java-clean-code-2-liner-generic-for-you-may-delete-at-most-n-character/
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Start the validation with the given string, from the beginning and end,
        # and allow at most 1 character deletion.
        return self.valid(s, 0, len(s) - 1, 1)

    def valid(self, s, i, j, d):
        # If the left index is greater than or equal to the right index, it's a palindrome.
        if i >= j:
            return True
        
        # If characters at the current positions match, continue validating the inner part of the string.
        if s[i] == s[j]:
            return self.valid(s, i + 1, j - 1, d)
        else:
            # If characters don't match, you can delete at most 1 character.
            # Check both possibilities: deleting a character from the left or the right.
            return d > 0 and (self.valid(s, i + 1, j, d - 1) or self.valid(s, i, j - 1, d - 1))

'''




def validPalindrome(self, s: str) -> bool:
  i = 0
  j = len(s)-1
  self.cnt = 0

  def isValid(s,i,j):
    while i<j:
      if s[i]!=s[j]:
        self.cnt+=1
        if self.cnt>1: return False
        #move one from left or right and check again
        return isValid(s,i+1,j) or isValid(s,i,j-1)
      else:
        i+=1
        j-=1
    return True

  return isValid(s,i,j)

s = "aba"   #op = True
# s = "abca"   #op = True just delete one
# s = "cabbcc"  # False as we will have to delete more than one
print(validPalindrome(s))