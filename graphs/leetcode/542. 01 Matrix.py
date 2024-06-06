class Solution:
  def updateMatrix(self, mat):
    if not mat: return mat
    rows = len(mat)
    cols = len(mat[0])
    distances = [[0 for _ in range(cols)] for _ in range(rows)]
    vis = [[0 for _ in range(cols)] for _ in range(rows)]
    q=[]

    for r in range(rows):
      for c in range(cols):
        if mat[r][c]==0:
          q.append([r,c,0])
          vis[r][c] =1
    
    while q:
      row, col, d = q.pop(0)
      directions = [[1,0], [-1,0], [0,1], [0,-1]]

      for dr,dc in directions:
        r,c = row+dr, col+dc
        if 0<=r<rows and 0<=c<cols and not vis[r][c] and mat[r][c]==1:
          q.append([r,c,d+1])
          distances[r][c]=d+1
          vis[r][c] = 1

    return distances