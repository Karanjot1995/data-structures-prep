'''
APPROACH 1: Brute Force (check all substrings)
- Using 2 loops to generate all the substrings then a 3rd loop inside the 2nd loop to check if the
generated substring is a palindfrom or not

TC - O(N^3)
SC - O(1)
'''
def countSubstrings1(s: str) -> int:
    count = 0
    
    def isPalindrome(i, j):
        left = i
        right = j - 1
        
        while left < right:
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
        
        return True
    
    for length in range(len(s), 0, -1):
        for start in range(len(s) - length + 1):
            if isPalindrome(start, start + length):
                count += 1

    return count



'''
APPROACH 2: Check in the middle and expand outwards (Optimal)
- Usually how do we check if a string is a palindrome or not?
    - we take 2 pointers at start and end keep on checking if the str[start] is equal to str[end] or not
- Here we use similar approach but instead of starting from ends of string we check from middle and expand outwards
- We need to check for both even and odd length palindromes so using a loop we would consider every char as the middle of the palindrome
  and expand outwards to seee how many palindromes we can get
- We have to do this for even length palindromes as well so we would consider 2 characters a time as well

TC - O(N^2)
SC - O(1)
'''
def countSubstrings2(s: str) -> int:
  ans = 0
  def isPalindrome(l,r):
    count = 0
    while l>=0 and r<len(s) and s[l]==s[r]:
      count+=1
      l-=1
      r+=1
    return count

  for i in range(len(s)):
    # for odd length + for even length
    ans+=isPalindrome(i,i)+isPalindrome(i,i+1)
  return ans



# Time complexity: O(n^2) because for a character worst case can be to traverse all neighbours.
# Space complexity: O(n^2)
def countSubstrings3(s: str) -> int:
  n = len(s)
  dp = [[False] * n for _ in range(n)]
  ans = 0

  for i in range(n):
    dp[i][i] = True
    ans += 1

  for i in range(n - 1):
    if s[i] == s[i + 1]:
      dp[i][i + 1] = True
      ans += 1

  for length in range(3, n + 1):
    for i in range(n - length + 1):
      j = i+length-1
      if s[i] == s[j] and dp[i+1][j-1]:
        dp[i][j] = True
        ans += 1

  return ans









def countSubstrings(s: str) -> int:
  memo = {}
  def checkPalind(i,j):
    if i>j: return 1
    if (i,j) in memo: return memo[(i,j)]
    if s[i]==s[j]:
      memo[(i,j)] = checkPalind(i+1,j-1)
      return memo[(i,j)]
    return 0

  cnt = 0
  for i in range(len(s)):
    for j in range(i,len(s)):
      if checkPalind(i,j): 
        cnt+=1
  return cnt



        