def wallsAndGates(mat):
  rows, cols = len(mat), len(mat[0])
  inf = 2147483647
  distances = [[0 for _ in range(cols)] for _ in range(rows)]
  q = []
  vis = set()  

  for r in range(rows):
    for c in range(cols):
      if mat[r][c] == 0:
        q.append([r,c,0])
        vis.add((r,c))

  while q:
    row,col,d = q.pop(0)
    print(row, col, d)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dr,dc in directions:
      r,c = row+dr, col+dc
      if r in range(rows) and c in range(cols) and (r,c) not in vis and mat[r][c]==inf:
        q.append([r,c,d+1])
        mat[r][c]=d+1
        # distances[r][c]=d+1
        vis.add((r,c))
      # elif r in range(rows) and c in range(cols) and (r,c) not in vis and mat[r][c]==-1:
      #   # distances[r][c]=-1
      #   vis.add((r,c))
  return mat




# mat = [[0,-1],[0,2147483647]] 
mat = [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1], [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]]

print(wallsAndGates(mat))
