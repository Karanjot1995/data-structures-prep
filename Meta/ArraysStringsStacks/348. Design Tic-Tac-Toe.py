# https://leetcode.com/problems/design-tic-tac-toe/

'''
APPROACH 1: Brute force
Traverse nxn matrix and find the winner

TC - O(N^2)
SC - O(N^2)
'''

'''
APPROACH 2: Optimized Brute Force
Where ever the player marks on board, check that particular row and col ONLY + check diagonals

TC - O(N)
SC - O(N^2)
'''
class TicTacToe1:

    def __init__(self, n: int):
        self.board = [[-1 for _ in range(n)] for _ in range(n)]
        self.n = n
    
    def checkRow(self, row, player):
        for col in range(self.n):
            if self.board[row][col] != player:
                return False
        
        return True
    
    def checkColumn(self, col, player):
        for row in range(self.n):
            if self.board[row][col] != player:
                return False
        
        return True
    
    def checkDiagonal(self, player):
        # in diagonal row == col
        for row in range(self.n):
            if self.board[row][row] != player:
                return False
        
        return True
    
    def checkAntiDiagonal(self, player):
        # in anti diagonal col = n - row - 1
        for row in range(self.n):
            if self.board[row][self.n - row - 1] != player:
                return False
        
        return True
    
    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player

        if self.checkRow(row, player) or \
            self.checkColumn(col, player) or \
            (row == col and self.checkDiagonal(player)) or \
            (col == self.n - row - 1 and self.checkAntiDiagonal(player)):
            return player
        
        return 0
    
'''
APPROACH 3: Most Optimal

OBSERVATIONS
- We have to determine for each row or column that if the user has marked all the cells in that row or column -- if 
  there are n rows and cols we have to check if the user has marked all the n cells in a row or column
- We also have to keep track of 1 diagonal and 1 antidiagonal if the user has marked all the cells in that

ALGORITHM
1) We will take the first player as 1 and the second player as -1
2) To keep track of rows and cols we will create 2 lists of size n for row and col each (each element in that array will represent each row/col of the grid)
3) Simillarly for keeping track of diagonals we will create 2 variables diagonal and anti_diagonal
4) When any of the player marks at a coordinate (i, j) we will add that player (1 or -1) to row[i] and col[j]
5) If the coordinate is diagonal or anti_diagonal then we will add that player (1 or -1) to the diagonal or anti_diagonal as well
6) At every move after marking the board we will check if row that was just marked is equal to "n" (size of the board) or not if it is then we have a winner
7) We will check the same for col, diagonal and anti_diagonal and if one of them is true we return that player
8) This winner checking will be done in constant time


TC - O(1)
SC - O(N)
'''
class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0
    
    def move(self, row: int, col: int, player: int) -> int:
        cur_player = 1 if player == 1 else -1

        self.rows[row] += cur_player
        self.cols[col] += cur_player

        if row == col:
            self.diagonal += cur_player
        
        if col == self.n - row - 1:
            self.anti_diagonal += cur_player
        
        if abs(self.rows[row]) == self.n or \
            abs(self.cols[col]) == self.n or \
            abs(self.diagonal) == self.n or \
            abs(self.anti_diagonal) == self.n:
            print(player)
            return player
        
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)


# Your TicTacToe object will be instantiated and called as such:
obj = TicTacToe(3)
param_1 = obj.move(0, 0, 1)
param_1 = obj.move(0, 2, 2)
param_1 = obj.move(2, 2, 1)
param_1 = obj.move(1, 1, 2)
param_1 = obj.move(2, 0, 1)
param_1 = obj.move(1, 0, 2)
param_1 = obj.move(2, 1, 1)
# print(obj)