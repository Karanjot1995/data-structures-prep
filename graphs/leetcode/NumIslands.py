from Templates.DisjointSet import DisjointSet

def numIslands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def bfs(r,c):
        q = []
        q.append([r,c])
        visited.add((r,c))

        while q:
            row, col = q.pop(0)
            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            for dr,dc in directions:
                r,c = row+dr, col+dc
                if ( r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visited):
                    q.append([r,c])
                    visited.add((r,c))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r,c) not in visited:
                bfs(r,c)
                islands+=1
    return islands



def numIslandsQueries(rows, cols, operators):
    ds = DisjointSet(rows*cols)
    visited = [[0 for j in range(cols)] for i in range(rows)]
    cnt = 0
    ans = []

    for row,col in operators:
      if visited[row][col]==1:
        ans.append(cnt)
        continue
      visited[row][col]=1
      cnt+=1
      directions = [[1,0], [-1,0], [0,1], [0,-1]]
      for dr, dc in directions:
        r,c = row+dr,col+dc
        if r in range(rows) and c in range(cols) and visited[r][c]==1:
            i = row*cols + col
            j = r*cols + c
            if ds.findUParent(i)!=ds.findUParent(j):
                cnt-=1
                ds.unionBySize(i,j)
      ans.append(cnt)

    return ans


# rows = 4
# cols = 5
# A= [[1,1], [0,1], [3,3], [3,4]]

rows = 3
cols = 5
A= [[1,0], [1,1], [0,3], [2,3], [2,4], [2,4], [2,1], [1,4], [0,0], [1,2], [2,0]]
print(numIslandsQueries(rows,cols,A))

# 1 0 0 1 0
# 1 1 1 0 1
# 1 1 0 1 1
