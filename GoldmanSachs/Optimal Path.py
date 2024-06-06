import math
# LEETCODE LINK - https://leetcode.com/discuss/interview-question/1837465/Goldman-Sachs-or-Coderpad-or-Find-the-maximum-gold-that-can-be-collected

'''
Approach: Recursive
- Travel from top right (New York) to so cal since we have to collect rocks at New York

# TC - O(2^(m + n)) -> exponential
# SC - O(m + n)
We use an extra matrix dpdpdp of the same size as the original matrix. 
In this matrix, dp(i,j)dp(i, j)dp(i,j) represents the minimum sum of the path from the index (i,j)(i, j)(i,j) to
the bottom rightmost element. We start by initializing the bottom rightmost element
of dpdpdp as the last element of the given matrix. Then for each element starting from
the bottom right, we traverse backwards and fill in the matrix with the required
minimum sums. Now, we need to note that at every element, we can move either
rightwards or downwards. Therefore, for filling in the minimum sum, we use the
equation:
'''
def optimal_path_recursive(grid):
    if not grid or len(grid) == 0 or len(grid[0]) == 0:
        return 0

    R, C = len(grid), len(grid[0])
    def solve(r, c):
        if r == 0 and c == C - 1:
            return grid[r][c]
        
        if r < 0 or c >= C:
            return -math.inf

        up = grid[r][c] + solve(r - 1, c)
        right = grid[r][c] + solve(r, c + 1)
        
        return max(up, right)

    return solve(R - 1, 0)

# TC - O(mn) | SC - O(mn)
def optimal_path_memo(grid):
    if not grid or len(grid) == 0 or len(grid[0]) == 0:
        return 0

    R, C = len(grid), len(grid[0])
    dp = [[-1 for _ in range(C)] for _ in range(R)]
    def solve(r, c):
        if r == 0 and c == C - 1:
            return grid[r][c]
        
        if r < 0 or c >= C:
            return -math.inf
        
        if dp[r][c] != -1: return dp[r][c]

        up = grid[r][c] + solve(r - 1, c)
        right = grid[r][c] + solve(r, c + 1)
        
        dp[r][c] = max(up, right)
        return dp[r][c]

    return solve(R - 1, 0)

# GS SOLUTION
# TC - O(mn) | SC - O(mn)
def optimal_path(grid):
    if not grid or len(grid) == 0 or len(grid[0]) == 0:
        return 0
    
    R, C = len(grid), len(grid[0])
    for r in range(R - 1, -1, -1):
        for c in range(0, C):
            # print("r ", r, " | ", "c ", c, " | ", "val", grid[r][c])
            if r < R - 1 and C > 0:
                grid[r][c] += max(grid[r + 1][c], grid[r][c - 1])
            elif r < R - 1:
                grid[r][c] += grid[r + 1][c]
            elif c > 0:
                grid[r][c] += grid[r][c - 1]
    return grid[0][C - 1]

# Video - https://www.youtube.com/watch?v=BzTIOsC0xWM&ab_channel=Pepcoding
# TC - O(M*N)
# SC - O(M*N)
def solve(grid):
    
    if not grid or len(grid) == 0 or len(grid[0]) == 0:
        return 0
    
    R, C = len(grid), len(grid[0])
    dp = [[0 for _ in range(C)] for _ in range(R)]
    print(dp)
    
    # solve from new york (top right)
    for r in range(0, R):
        for c in range(C - 1, -1, -1):
            if r == 0 and c == C - 1: # top right cell
                dp[r][c] = grid[r][c]
            elif r == 0: # first row
                # cant go up, can only go right
                dp[r][c] = dp[r][c + 1] + grid[r][c]
            elif c == C - 1: # last col
                # cant go right, can only go up
                dp[r][c] = dp[r - 1][c] + grid[r][c]
            else:
                # rest of cells
                dp[r][c] = max(dp[r][c + 1], dp[r - 1][c]) + grid[r][c]
            print(dp)
    
    return dp[R - 1][0]


grid1 = [
    [0, 0, 0, 0, 5],
    [0, 1, 1, 1, 0],
    [2, 0, 0, 0, 0]
]

grid2 = [
    [1, 3, 2, 0, 2, 1, 8],
    [3, 4, 1, 2, 0, 1, 1],
    [1, 1, 1, 2, 3, 2, 1],
    [1, 0, 1, 1, 4, 2, 1],
]

grid3 = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

grid4 = [
    [1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0],
    [1, 1, 1,1, 1],
]

grid5 = [[]]

print(solve(grid1)) # 10
print(solve(grid2)) # 25
print(solve(grid3)) # 0
print(solve(grid4)) # 8
print(solve(grid5)) # 0