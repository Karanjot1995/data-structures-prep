# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/

'''
CLARIFTING QUESTIONS

- empty string?
- null string
- will string only contain parantheses or other characters
'''

class Solution:
    '''
    APPROACH 1: STACK
    - Simlar to checking if the string is valid parantheses or not (LC 20)
    - We will keep track of invalid parentheses in a stack
    - Length of stack will be the min parantheses needed to be added
    
    TC - O(N)
    SC - O(N)
    '''
    def minAddToMakeValid1(self, s: str) -> int:
        stack = []
        for char in s:
            if char == "(":
                stack.append(char)
            else:
                # char is ")"
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(char)
        
        return len(stack)
    
    '''
    APPROACH 2: NO STACK
    - instead of using stack we can use 2 variables to keep track of opening and closing
    - we just balance the parantheses as we see opening and closing
    - in the end we would return addition of opening and closing
    
    TC - O(N)
    SC - O(1)
    '''
    def minAddToMakeValid(self, s: str) -> int:
        opening = closing = 0

        for char in s:
            if char == "(":
                opening += 1
            else:
                if opening: opening -= 1
                else:
                    closing += 1
        
        return opening + closing