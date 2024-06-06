# def myPow(x: float, n: int):
#   if n==0: return 1
#   if n<0: return 1/myPow(x,-n)
#   if n % 2 == 1:
#     return x * myPow(x * x, (n - 1) // 2)
#   else:
#     return myPow(x * x, n // 2)
  

# print(myPow(100,10))


import math


def isPower (x, y):
     
    # The only power of 1
    # is 1 itself
    if (x == 1):
        return (y == 1)
         
    # Repeatedly compute
    # power of x
    pow = 1
    while (pow < y):
        pow = pow * x
 
    # Check if power of x
    # becomes y
    return (pow == y)

print(isPower(100,10000))


def is_power(x, y):
    # logarithm function to calculate value
    res1 = math.log(y) / math.log(x)
    print(math.log(y), math.log(x))
    res2 = math.floor(math.log(y) / math.log(x)) # Note: this is float
    print(res1,res2)
 
    # compare to the result1 or result2 both are equal
    return res1 == res2

print(is_power(2,8))

# class Solution:
#     def __init__(self):
#         self.powers = set()
#         i = 1
#         while i <= 2**31:
#             self.powers.add(i)
#             i *= 10
    
#     def isPowerOf10(self, num):
#         # Method 1: Log base 10 must be integer
#         n = math.log10(num)
#         print('Method 1', n == int(n))
        
#         # Method 2: Sum of all digits must be 1
#         add = 0
#         n = num
#         while n:
#             add += n % 10
#             n //= 10
#         print('Method 2', add == 1)
        
#         # Mathod 3: num must have only one occurence 1 and all rest 0s
#         temp = str(num)
#         print('Method 3', temp.count('1') + temp.count('0') == len(temp))
        
#         # Method 4: keep dividing number by 10, reminder must be 0 every time. If we reach to 1, return True
#         n = num
#         if n == 1: print('Method 4', True)
#         elif n % 10 != 0: print('Method 4', False)
#         while n > 1:
#             if n % 10 != 0: 
#                 print('Method 4', False)
#                 break
#             n //= 10
#             if n == 1:
#                 print('Method 4', True)
#                 break
        
#         # Method 5: Convert num to string, left rotate string once, reconvert to int, it must be 1
#         n = str(num)
#         n = n[1:] + n[:1]
#         print('Method 5', int(n) == 1)
        
#         # Method 6: Preprocess and generate all power 10 (< 2**31), num must be present in list
#         print('Method 6', num in self.powers)

# s = Solution()
# s.isPowerOf10(1)
        
                