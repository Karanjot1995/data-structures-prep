# Brute Force
#TC - O(N*N!) = n possibilities to place 1 queen, n - 1 possibilities to place 2nd queen and so on

def solveNQueensBrute(n: int):
  board =  [["."] * n for _ in range(n)]
  ans = []

  def isSafe(row,col):
    #check if theres a Q in previous row/col/diagnol

    #prev cols in the row
    r,c = row,col
    while c>=0:
      if board[r][c]=='Q': return False
      c-=1

    #diagnol left
    r,c = row,col
    while r>=0 and c>=0:
      if board[r][c]=='Q': return False
      r-=1
      c-=1

    #antidiagnol left
    r,c = row,col
    while r<n and c>=0:
      if board[r][c]=='Q': return False
      r+=1
      c-=1

    return True
  
  def backtrack(col):
    if col == n: 
      ans.append(["".join(r) for r in board])
      # ans.append(board[:])
      return
    
    for row in range(n):
      if isSafe(row,col):
        board[row][col] = 'Q'
        backtrack(col+1)
        board[row][col] = '.'

  backtrack(0)

  return ans

print(solveNQueensBrute(4))





# TC - O(N!) = n possibilities to place 1 queen, n - 1 possibilities to place 2nd queen and so on
# SC - O(N^2)
def solveNQueens(n: int):
  row = set()
  upperDiag = set() # (r - c)
  lowerDiag = set() # (r + c)

  ans = []
  board =  [["."] * n for _ in range(n)]

  def backtrack(c):
    if c == n:
      # found a valid solution
      bcopy = ["".join(row) for row in board]
      ans.append(bcopy)
      return
    
    for r in range(n):
      print(r,c)
      if r in row or (r + c) in lowerDiag or (n-1+(c-r)) in upperDiag:
          continue
      
      row.add(r)
      lowerDiag.add(r + c)
      upperDiag.add(n-1+(c-r))
      board[r][c] = "Q"

      backtrack(c + 1)

      row.remove(r)
      lowerDiag.remove(r + c)
      upperDiag.remove(n-1+(c-r))
      board[r][c] = "."
  
  backtrack(0)
  return ans


print(solveNQueens(4))
