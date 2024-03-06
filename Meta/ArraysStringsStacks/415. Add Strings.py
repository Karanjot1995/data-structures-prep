# https://leetcode.com/problems/add-strings/description/

'''
CLARYFYING QUESTIONS
- What if one of the numbers or both of them are null?
- Will the numbers (if string) contains chars other than nums?
- Will the numbers contain only digits from 0 - 9 or it can have -ve numbers?
- Can the numbers have leading zeroes? other than 0 itself?
'''

'''
APPROACH: Math
1) Iterate over the numbers from behind
2) We would iterate till whatever is the max length between the two numbers
3) Get the digits from both the numbers and convert it to integer and add them and calculate the carry

TC - O(max(n1, n2))
SC - O(max(n1, n2)) as the length of the new string is at most max(n1, n2) + 1
'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n = max(len(num1), len(num2))
        n1 = num1[::-1]
        n2 = num2[::-1]

        carry = 0
        ans = ""
        for i in range(n):
            digit1 = ord(n1[i]) - ord("0") if i < len(num1) else 0
            digit2 = ord(n2[i]) - ord("0") if i < len(num2) else 0

            total = digit1 + digit2 + carry
            ans += str(total % 10)

            carry = total // 10
        
        if carry:
            ans += str(carry)
        
        return ans[::-1]