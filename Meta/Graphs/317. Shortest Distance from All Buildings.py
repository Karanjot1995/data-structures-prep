# https://leetcode.com/problems/shortest-distance-from-all-buildings/

'''
VARIATION - https://leetcode.com/discuss/interview-question/302416/facebook-phone-screen-shortest-distance-from-all-houses

You've been tasked to help a village find the best place to install a new well. You're given a 2D grid where cells can be empty, a house, or a tree. People can walk up, down, left and right, but they can't walk through trees. Place the well that minimizes the total sum distance from all the houses.

=. =. =. =
= H T =
= H T =
= = H =

'''

'''
Algorithm
1) Keep a distance 2D array (same size as input)
2) Do BFS from every building and mark the distance from building to each land cell (in the distance array)
3) For the subsequent BFS calls just add in the distance at each cell
4) After all the BFS calls just return the minimum distance in the 2D matrix
5) For each BFS how to mark as visited? Just use the LAND cells (0) and reduce -1 from each cell for marking as visited and after every BFS change the LAND cell variable by -1

TC - O(((NM) ^ 2)
SC - O(NM)
'''

from collections import deque
class Solution:
  LAND = 0
  def shortestDistance(self, grid) -> int:
    rows, cols = len(grid), len(grid[0])
    distances = [[0]*cols for _ in range(rows)]

    def bfs(r,c):
      q = deque([[r,c,0]])
      visited = set()
      dist = float('inf')

      while q:
        row, col, d = q.popleft()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        
        for dr,dc in directions:
          r,c = row+dr, col+dc
          #adding the land variable also makes sure that
          #all lands are visited. If some are not visited in the next
          #iteration then they will not match the land variables value
          if (r in range(rows) and c in range(cols) and grid[r][c]==self.LAND):
            visited.add((r,c))
            grid[r][c]-=1
            q.append([r,c,d+1])
            distances[r][c] += d+1
            dist = min(dist, distances[r][c])
      # decrementing LAND so that we dont have to carry visit set for each BFS call
      self.LAND-=1
      return dist

    min_d = float('inf')
    for r in range(rows):
      for c in range(cols):
        if grid[r][c] == 1:
          d = bfs(r,c)
          min_d = d

    return -1 if min_d == float('inf') else min_d

    
        