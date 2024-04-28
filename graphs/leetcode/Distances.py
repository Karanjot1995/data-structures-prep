
# distance of nearest cell having 1 up down left or right
def distance(grid):
  distances = set()
  rows, cols = len(grid), len(grid[0])
  distances = [[0 for _ in range(cols)] for _ in range(rows)]
  visited = set()
  q=[]

  for r in range(rows):
    for c in range(cols):
      if grid[r][c] == 1:
        q.append([r,c,0])
        visited.add((r,c))
        
  while q:
    row, col, d = q.pop(0)
    directions = [[1,0], [-1,0], [0,1], [0,-1]]
    
    for dr,dc in directions:
      r,c = row+dr, col+dc
      print((r,c),d)
      if (r in range(rows) and c in range(cols) and grid[r][c]==0 and (r,c) not in visited):
        visited.add((r,c))
        q.append([r,c,d+1])
        distances[r][c] = d+1

  return distances

# print(distance([[0,0,0],[0,1,0],[1,0,1]]))
print(distance([[0, 0, 0, 1],[0, 0, 1, 1],[0, 1, 1, 0]]))

# [0, 0, 0, 1]
# [0, 0, 1, 1]
# [0, 1, 1, 0]
# input: grid = [[0,0,0],
#                [0,1,0],
#                [1,0,1]]

