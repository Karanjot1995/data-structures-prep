class Solution:
    '''
    APPROACH: Recursion
    - https://leetcode.com/problems/find-the-winner-of-the-circular-game/solutions/1601186/c-3-approach-easy-understanding/
    - Video: https://www.youtube.com/watch?v=gAZwWpv_GUM
    TC - O(N)
    SC - O(N)
    '''
    def findTheWinner1(self, n: int, k: int) -> int:
        def solve(n):
            if n == 1:
                return 0
            
            return (solve(n - 1) + k) % n
        
        # +1 to convert to 1 based indexing
        return solve(n) + 1
    
    def findTheWinner(self, n: int, k: int) -> int:
      q = [i + 1 for i in range(n)]
      i = 0
      while len(q)>1:
        i = (i+k-1)%len(q)
        q.pop(i)
      return q[0]
    '''
    APPROACH: Recusrive approach to iterative

    TC - O(N)
    SC - O(1)
    '''
    def findTheWinner(self, n: int, k: int) -> int:
      ans = 0
      for i in range(1, n + 1):
        ans = (ans + k) % i
      return ans + 1