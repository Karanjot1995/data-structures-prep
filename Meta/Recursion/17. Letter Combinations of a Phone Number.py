# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    '''
    APPROACH 1: BACKTRACKING
    
    ALGORITHM
    1) We can store the chars corresponding to a digit in a hashmap
    2) Then we can find all the combinations using the given digits using a backtracking algorithm
    
    For ex: "23"
    - 2 can map to "a", "b", "c" and each of these char can map to 3's corresponding chars "d", "e", "f"
    
                            2("a", "b", "c")
                         /         |        \
                        a          b          c
                      / | \      / | \      / | \
                     d   e  f   d  e  f    d  e  f
    
    TC
    - O(N * 4^N) (as 9 has 4 chars, N is length of the digits string)
    - 4^N is the number of output strings we can have, ex digits = 9999 then we can have 4*4*4*4 choices so 4^N
    SC
    - O(N) where N is the length of digits
    '''
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        
        if digits == "": return ans

        digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(idx, curStr):
            if len(curStr) >= len(digits):
                ans.append(curStr)
                return
            
            chars = digit_to_char[digits[idx]]
            for c in chars:
                curStr += c
                backtrack(idx + 1, curStr)
                
                # backtrack (take all the chars in curStr except the last one)
                curStr = curStr[: -1]
                
                # instead of all the above code we can do (as this would handle the backtracking)
                # backtrack(idx + 1, curStr + c)
        
        backtrack(0, "")
        return ans
    
    '''
    APPROACH 2: BFS
    
    https://leetcode.com/problems/letter-combinations-of-a-phone-number/solutions/1022553/python-3-approaches-iterative-dfs-bfs-recursive-visuals-explanation/
    '''
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        d = {1: '', 2: 'abc',3: 'def',4: 'ghi',5: 'jkl',6: 'mno',7: 'pqrs',8: 'tuv',9: 'wxyz'}
        q = deque(d[int(digits[0])])
        
        for i in range(1,len(digits)):
            s = len(q)
            while s:
                poppedChar = q.popleft()
                for char in d[int(digits[i])]:
                    q.append(poppedChar + char)
                s -= 1
                
        return q
