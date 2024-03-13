# https://leetcode.com/problems/minesweeper/description/

class Solution:
    '''
    APPROACH: DFS
    
    TC - O(M * N)
    SC - O(M * N) for recursion stack space
    '''
    def updateBoard(self, board, click):
      c1, c2 = click
      if board[c1][c2] == "M": 
        board[c1][c2]="X"
        return board
      rows = len(board)
      cols = len(board[0])
      vis = set()

      def dfs(row,col):
        if board[row][col]!="E": return
        directions = [(1, 1), (1, 0), (0, 1), (-1, -1), (-1, 0), (0, -1), (1, -1), (-1, 1)]
        mines = 0
        for dr,dc in directions:
          nr,nc = row+dr,col+dc
          if 0<=nr<rows and  0<=nc<cols and board[nr][nc]=="M":mines+=1
        
        if mines: board[row][col]=str(mines)
        else: 
          board[row][col]="B"
          for dr,dc in directions:
            nr,nc = row+dr,col+dc
            if 0<=nr<rows and  0<=nc<cols:
              dfs(nr,nc)

      dfs(c1,c2)

      return board
          