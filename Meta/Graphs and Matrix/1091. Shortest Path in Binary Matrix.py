# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

from collections import deque

class Solution:
    '''
    APPROACH: BFS (overwriting input)

    CLARIFYING QUESTIONS
    - Can we find obstacle at start and/or end?
    - Can I overwrite input instead of taking a visited set?

    TC - O(N * N)
    SC - O(N)
    '''
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1: return - 1
        
        R, C = len(grid), len(grid[0])
        q = deque([(0, 0, 1)]) # (r, c, steps)
        grid[0][0] = 1 # mark as visited

        directions = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1],
            [1, -1],
            [-1, 1],
            [-1, -1],
            [1, 1]
        ]
        
        while q:
            r, c, steps = q.popleft()

            if r == R - 1 and c == C - 1:
                return steps

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= R or nc < 0 or nc >= C or grid[nr][nc] == 1:
                    continue
                
                grid[nr][nc] = 1
                q.append((nr, nc, steps + 1))

        return -1

'''
FOLLOW UP -- print out the path taken also
-------------------------------------------

1) We can maintain an additional 2D matrix to store the previous position (parent) for each cell
2) Then, we can backtrack from the destination cell to the source cell using this parent information to reconstruct the path

Check the below code (same as above) -- ONLY new code added where there are comments
'''
def shortestPathBinaryMatrix(grid):
    if grid[0][0] == 1 or grid[-1][-1] == 1: 
        return -1
    
    R, C = len(grid), len(grid[0])
    q = deque([(0, 0, 1)])
    grid[0][0] = 1

    directions = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1],
        [1, -1],
        [-1, 1],
        [-1, -1],
        [1, 1]
    ]
    
    # STEP 1: Parent matrix to store the previous position for each cell
    parent = [[None] * C for _ in range(R)]
    
    while q:
        r, c, steps = q.popleft()

        if r == R - 1 and c == C - 1:
            # STEP 3: Reconstruct the path and print it
            path = []
            while (r, c) != (0, 0):
                path.append((r, c))
                r, c = parent[r][c]
            path.append((0, 0))
            path.reverse()
            print("Path:", path)
            return steps

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if nr < 0 or nr >= R or nc < 0 or nc >= C or grid[nr][nc] == 1:
                continue
            
            grid[nr][nc] = 1
            parent[nr][nc] = (r, c)  # STEP 2: Store the parent cell
            q.append((nr, nc, steps + 1))

    return -1

# Example usage:
grid = [
    [0, 0, 0],
    [1, 1, 0],
    [1, 1, 0]
]
print(shortestPathBinaryMatrix(grid))



class Solution:
  def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    if grid[0][0] == 1 or grid[-1][-1] == 1: return -1
    rows = len(grid)
    cols = len(grid[0])

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1,-1), (-1,1), (1,-1), (1,1)]
    dist = [[float('inf') for _ in range(cols)] for _ in range(rows)]
    dist[0][0] = 0
    q = deque([[0,0,0]])

    while q:
      row,col,dis = q.popleft()
      if row == rows-1 and col == cols-1: return dis+1
      for dr,dc in directions:
        nr,nc = row+dr, col+dc
        new_dis = dis+1
        if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 0 and new_dis<dist[nr][nc]:
          dist[nr][nc] = new_dis
          q.append([nr,nc,new_dis])


    return -1