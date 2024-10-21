# https://leetcode.com/problems/valid-number/description/

class Solution:
    '''
    APPROACH: Handle all the edge cases
    
    A number can be:
    - Decimal
        - can have a sign (-)/(+)
        - 1 or more digit followed by a dot
        - 1 or more digit before the dot
        - if having an "e" has to come after dot
    - Integer
        - can have a sign (-)/(+)
        - 1 or more digits
    - Having exponents
        - a number should be before "e"
        - a number should be followed by an "e/E" (-ve or +ve num)
        - can only be 1 "e/E"
    
    Valid numbers: "2", "0089", "-0.1", "+3.14", "-.9", "2e10", "+6e-1", "53.5e93"
    Invalid numbers: "abc", "1a", "1e", "e3", "99e.25", "--3"
    
    TC - O(N)
    SC - O(1)
    '''
    def isNumber(self, s: str) -> bool:
        seenDigit = seenDecimal = seenExponent = False

        for i,c in enumerate(s):
            if c.isdigit(): seenDigit = True
            elif c in ['-','+']:
                if i>0 and s[i-1] not in ['e','E']: return False
            elif c in ['e', 'E']:
                if seenExponent or not seenDigit: return False
                seenExponent = True
                seenDigit = False
            elif c == '.':
                if seenExponent or seenDecimal: return False
                seenDecimal = True
            else:
                return False
        return seenDigit

'''
META ALTERNATIVE: There is no "e"
'''

'''
    APPROACH: Handle all the edge cases
    
    A number can be:
    - Decimal
        - can have a sign (-)/(+) and should be at the starting
        - 1 or more digit followed by a dot
        - 1 or more digit before the dot
    - Integer
        - can have a sign (-)/(+) and should be at the starting
        - 1 or more digits
        - no alphabets
    
    Can I consider these valid? (SPECIAL CASES)
    - 0.5 can also be written as .5
    - for -.5 and 5.
    
    QUESTIONS
    - null string
    - empty string
    - leading zeroes should I consider ok? "001"
    
    TC - O(N)
    SC - O(1)
'''
def isNumber(s):
    if not s or len(s) == 0: return False
    
    seen_sign = seen_decimal = seen_digit = False
    
    if s[0] == "-":
        seen_sign = True
        s = s[1:]
    
    if len(s) == 0:
        return False
    
    # "-0" is not valid
    if seen_sign and s[0] == "0":
        return False
    
    # HANDLE LEADING ZEROES IF NOT ALLOWED
    if len(s) > 1 and s[0] == "0":
        return False
    
    for i, c in enumerate(s):
        if s[i].isdigit():
            seen_digit = True
        if c == ".":
            if seen_decimal:
                return False
            
            # handle for string "."
            if not seen_digit and i == len(s) - 1:
                return False
            
            seen_decimal = True
            
            # if special cases are invalid i.e. (decimal point should ALWAYS have a digit to the left and right)
            # if i > 0 and i < len(s) - 1:
            #     if not s[i - 1].isdigit() or not s[i + 1].isdigit():
            #         return False
            # else:
            #     return False
        elif not s[i].isdigit():
            # if we encounter an alphabet other than "e", "E"
            return False
    
    return True

# GOOD CASES
# print(isNumber("100,000")) # FALSE
print(isNumber("-0.0")) # FALSE
print(isNumber("1. 3")) # FALSE
print(isNumber("1.2 ")) # FALSE
print(isNumber("-0")) # FALSE
print(isNumber("-001")) # FALSE
print(isNumber("0")) # True
print(isNumber("01")) # False
print(isNumber(".")) # False

print(isNumber("001")) # False
print(isNumber("13")) # True
print(isNumber("3.0")) # True
print(isNumber("-7.4")) # True
print(isNumber("-13.5")) # True
print(isNumber("abc")) # False
print(isNumber("123a")) # False
print(isNumber("-.")) # False
print(isNumber("-..---")) # False
print(isNumber("1.0.0.1")) # False
print(isNumber(".3")) # True
print(isNumber("3.")) # True
print(isNumber("-.3")) # True
print(isNumber("--0975..-0975..")) # False