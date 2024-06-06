
# Surrounded Regions
# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

def surroundedRegions(board):
  rows, cols = len(board), len(board[0])
  visited = [[0 for _ in range(cols)] for _ in range(rows)]
  q=[]

  #first, last row and column DFS on all Os at the boundary
  # 0,0 to 0,cols-1  0,0 to rows-1,0   rows-1,0 to rows-1,cols-1  cols-1,0 to rows-1,cols-1 
  def dfs(row,col):
    visited[row][col] = 1
    directions = [[1,0], [-1,0], [0,1], [0,-1]]
    for dr,dc in directions:
      r,c = row+dr, col+dc
      if (r in range(rows) and c in range(cols) and board[r][c]=="O" and visited[r][c]!=1):
        dfs(r,c)

  for r in range(rows):
    for c in range(cols):
      if board[r][c] == 'O' and (r == 0 or c == 0 or r == rows-1 or c == cols-1):
        dfs(r,c)


  for r in range(rows):
    for c in range(cols): 
      if board[r][c] == 'O' and visited[r][c]!=1:
         board[r][c] = 'X'
  return board


# print(surroundedRegions([["O","O"],["O","O"]]))
print(surroundedRegions([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))
# X X X X
# X O O X
# X X O X
# X O X X
