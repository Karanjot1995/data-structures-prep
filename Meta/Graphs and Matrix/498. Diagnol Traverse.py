from collections import deque


class Solution:
  #APPROACH 1: BFS
  #TC - O(N * M) | SC - O(min(N, M))
  def findDiagonalOrder(self, mat):
    rows = len(mat)
    cols = len(mat[0])
    ans = []

    directions = [[0,1],[1,0]] #right and bottom
    vis = set()
    vis.add((0,0))
    q = deque([(0, 0)])

    rev = False
    while q:
      print(q)
      lvl = []
      for i in range(len(q)):
        row,col = q.popleft()
        lvl.append(mat[row][col])
        for dr,dc in directions:
          r,c = row+dr, col+dc
          if r in range(rows) and c in range(cols) and (r,c) not in vis:
            q.append([r,c])
            vis.add((r,c))

      ans += lvl if rev else lvl[::-1]
      rev = not rev
    return ans

        
  # APPROACH 2: Simulation
  #TC - O(N * M) | SC - O(1)
  def findDiagonalOrder(self, mat):
    R = len(mat)
    C = len(mat[0])
    ans = []
    row,col=0,0

    direction = 1


    while row<R and col<C:
      ans.append(mat[row][col])
      nr = row + (-1 if direction==1 else 1)
      nc = col + (1 if direction==1 else -1)
      print('nr,nc: ', nr,nc)
      if nr>=0 and nr<R and nc>=0 and nc<C:
        row = nr
        col =nc
      else:
        if direction:
          if col == C-1: row+=1
          if col < C-1: col+=1
        else:
          if row == R-1: col+=1
          if row < R-1: row+=1
        direction = 1-direction
        
    return ans




  