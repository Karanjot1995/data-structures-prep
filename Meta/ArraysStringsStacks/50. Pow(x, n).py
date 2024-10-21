# https://leetcode.com/problems/powx-n/

# Video - https://www.youtube.com/watch?v=g9YQyYi4IQQ&ab_channel=NeetCode

'''
CLARIFYING QUESTIONS
- can 'n' be -ve ?
- what if 'n' is None ?
- what if 'x' is None ?
'''
class Solution:
    '''
    APPROACH 1 - Brute Force - Recursive

    TC - O(N) where N is the power "n"
    SC - O(N) for recursive stack frames; where N is the power "n"
    '''
    def myPowRecursive(self, x: float, n: int) -> float:
        if x == 0: return 0
        if n == 0: return 1

        if n < 0: return 1 / self.myPowRecursive(x, -n)

        return x * self.myPowRecursive(x, n - 1)
    
    '''
    APPROACH 2 - Brute Force - Iterative

    TC - O(N) where N is the power "n"
    SC - O(1)
    '''
    def myPowIterative(self, x: float, n: int) -> float:
        if x == 0: return 0
        if n == 0: return 1

        ans, power = 1, abs(n)
        while power > 0:
            ans *= x
            power -= 1
        
        return ans if n > 0 else 1 / ans
    
    def myPowOptimal(self, x: float, n: int) -> float:
        if n==0: return 1
        if n<0: return 1/self.myPow(x,-n)
        if n % 2 == 1:
            return x * self.myPow(x * x, (n - 1) // 2)
        else:
            return self.myPow(x * x, n // 2)
    
    '''
    APPROACH 3: DIVIDE AND CONQUER (RECURSIVE)
    - The main idea of solution is to break down the problem
    
    For example how can we evaluate x^20? We can just multiply x in loop 20 times, but we also can evaluate x^10
    and multiply it by itself! Similarly, x^10 = x^5 * x^5. Now we have odd power, but it is not a problem, we
    evaluate x^5 = x^2 * x^2 * x

    TC - O(logN) where N is the power "n"
    SC - O(logN) where N is the power "n"
    '''
    def myPowOptimalRecursive(self, x: float, n: int) -> float:
        
        def helper(x, n):
            # 0 ^ any number is 0
            if x == 0: return 0

            # x ^ 0 = 1 (any number raised to the power 0 is 1)
            if n == 0: return 1

            res = helper(x, n // 2)
            res = res * res # for x ^ 4 -> x^2 * x^2

            # for x^5 -> x * x^2 * x^2
            if n % 2 != 0: res *= x
            
            return res
            
        ans = helper(x, abs(n))

        return ans if n >= 0 else 1 / ans

    '''
    APPROACH 4: DIVIDE AND CONQUER (ITERATIVE)
    - The main idea of solution is to break down the problem
    
    For example how can we evaluate x^20? We can just multiply x in loop 20 times, but we also can evaluate x^10
    and multiply it by itself! Similarly, x^10 = x^5 * x^5. Now we have odd power, but it is not a problem, we
    evaluate x^5 = x^2 * x^2 * x

    TC - O(logN) where N is the power "n"
    SC - O(1)
    '''
    def myPowOptimalIterative(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        # Handling negative exponent
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2
        
        return result


'''
META ALTERNATE - pow(a, b)
'''

class Solution:
    '''
    APPROACH 1 - Brute Force - Recursive

    TC - O(N) where N is the power "n"
    SC - O(N) for recursive stack frames; where N is the power "n"
    '''
    def myPowRecursive(self, a: float, b: int) -> float:
        if a == 0: return 0
        if b == 0: return 1

        if b < 0: return 1 / self.myPowRecursive(a, -b)

        return a * self.myPowRecursive(a, b - 1)
    
    '''
    APPROACH 2 - Brute Force - Iterative

    TC - O(N) where N is the power "n"
    SC - O(1)
    '''
    def myPowIterative(self, a: float, b: int) -> float:
        if a == 0: return 0
        if b == 0: return 1

        ans, power = 1, abs(b)
        while power > 0:
            ans *= a
            power -= 1
        
        return ans if b > 0 else 1 / ans
    
    '''
    APPROACH 3: DIVIDE AND CONQUER (RECURSIVE)
    - The main idea of solution is to break down the problem
    
    For example how can we evaluate x^20? We can just multiply x in loop 20 times, but we also can evaluate x^10
    and multiply it by itself! Similarly, x^10 = x^5 * x^5. Now we have odd power, but it is not a problem, we
    evaluate x^5 = x^2 * x^2 * x

    TC - O(logN) where N is the power "n"
    SC - O(logN) where N is the power "n"
    '''
    def myPowOptimalRecursive(self, a: float, b: int) -> float:
        
        def helper(a, b):
            # 0 ^ any number is 0
            if a == 0: return 0

            # a ^ 0 = 1 (any number raised to the power 0 is 1)
            if b == 0: return 1

            res = helper(a, b // 2)
            res = res * res # for a ^ 4 -> a^2 * a^2

            # for a^5 -> a * a^2 * a^2
            if b % 2 != 0: res *= a
            
            return res
            
        ans = helper(a, abs(b))

        return ans if b >= 0 else 1 / ans

    '''
    APPROACH 4: DIVIDE AND CONQUER (ITERATIVE)
    - The main idea of solution is to break down the problem
    
    For example how can we evaluate x^20? We can just multiply x in loop 20 times, but we also can evaluate x^10
    and multiply it by itself! Similarly, x^10 = x^5 * x^5. Now we have odd power, but it is not a problem, we
    evaluate x^5 = x^2 * x^2 * x

    TC - O(logN) where N is the power "n"
    SC - O(1)
    '''
    def myPowOptimalIterative(self, a: float, b: int) -> float:
        if a == 0:
            return 0
        if b == 0:
            return 1
        
        # Handling negative exponent
        if b < 0:
            a = 1 / a
            b = -b
        
        result = 1
        while b > 0:
            if b % 2 == 1:
                result *= a
            a *= a
            b //= 2
        
        return result