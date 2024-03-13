from queue import deque

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

  #backtracking
  def letterCombinations(self, digits: str):
    if not digits: return []

    hmap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    #digits = "23"
    res = []
    def backtrack(index, path):
      if len(path) == len(digits): 
        res.append("".join(path))
        return
      possible_letters = hmap[digits[index]]
      for letter in possible_letters:
        path.append(letter)
        # print("path before:", path)
        backtrack(index+1,path)
        # print(path)
        path.pop()


    # def backtrack(index, currStrr):
    #   if len(currStrr) == len(digits): 
    #     res.append(currStrr)
    #     return
    #   possible_letters = hmap[digits[index]]
    #   for letter in possible_letters:
    #     currStrr+=letter
    #     backtrack(index+1,currStrr)
    #     currStrr = currStrr[:-1]
      
    # backtrack(0,"")
      
    backtrack(0,[])

    return res 

  def letterCombinations(self, digits: str):
    if digits == "":
      return []
    d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}    
    q = deque(d[digits[0]])
    
    for i in range(1,len(digits)):
      s = len(q)
      while s:
        poppedChar = q.popleft()
        for char in d[digits[i]]:
          q.append(poppedChar+char)
        s-=1
    return q
    
