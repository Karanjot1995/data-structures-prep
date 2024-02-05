from Templates.DisjointSet import DisjointSet

def largestIsland(grid):

  rows, cols = len(grid), len(grid[0])
  ds = DisjointSet(rows*cols)

  #step 1
  for row in range(rows):
    for col in range(cols):
      if grid[row][col] == 0:
        continue
      directions = [[1,0], [-1,0], [0,1], [0,-1]]
      for dr, dc in directions:
        #these are the coordinates
        r,c = row+dr,col+dc
        if r in range(rows) and c in range(cols) and grid[r][c]==1:
          #this is the number associated with the coordinates because we can't store coordinates
          i = row*cols + col
          j = r*cols + c
          ds.unionBySize(i,j)

  print(ds.parent)
  print(ds.size)

  #step 2
  mx = 0
  for row in range(rows):
    for col in range(cols):
      if grid[row][col]==1:
        continue
      directions = [[1,0], [-1,0], [0,1], [0,-1]]
      components = set()
      for dr, dc in directions:
        r,c = row+dr,col+dc
        #check if anything in all 4 directions of the 0 is a 1 and then get the ultimate parent of it and add to the list
        if r in range(rows) and c in range(cols) and grid[r][c]==1:
          newNode = r*cols + c
          components.add(ds.findUParent(newNode))

      sizeTotal = 0
      print(components)
      for c in components:
        # get the size associated with the ultimate parent
        sizeTotal += ds.size[c]
        mx = max(sizeTotal+1,mx)
  
  #in case all are 1s
  for cell in range(rows*cols):
    up_cell = ds.findUParent(cell)
    mx = max(mx, ds.size[up_cell])
  
  return mx

# grid = [[1,0],[0,1]]
grid = [[1,1,0,1,1],[1,1,0,1,1],[1,1,0,1,1],[0,0,1,0,0],[0,0,1,1,1],[0,0,1,1,1]]
print(largestIsland(grid))

# [1,1,0,1,1]
# [1,1,0,1,1]
# [1,1,0,1,1]
# [0,0,1,0,0]
# [0,0,1,1,1]
# [0,0,1,1,1]





