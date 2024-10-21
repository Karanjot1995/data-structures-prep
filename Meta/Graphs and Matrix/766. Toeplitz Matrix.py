
# https://leetcode.com/problems/toeplitz-matrix/description/

class Solution:
    '''
    APPROACH 1: Brute Force
    Store use hashmap to store diagonals { (r - c): val } and down the line if hmap[r -c ] != val (already calculated we return False)

    TC - O(M * N)
    SC - O(M + N)
    '''
    def isToeplitzMatrix(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        groups = {}

        for r in range(rows):
            for c in range(cols):
                if r - c not in groups:
                    groups[r - c] = matrix[r][c]
                elif groups[r - c] != matrix[r][c]:
                    return False
        return True
    
    '''
    APPROACH 2: Compare with top left neighbor
    What feature makes two coordinates (r1, c1) and (r2, c2) belong to the same diagonal?
    -> Two coordinates are on the same diagonal if and only if r1 - c1 == r2 - c2
    
    TC - O(M * N)
    SC - O(1)
    '''
    def isToeplitzMatrix2(self, matrix: List[List[int]]) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        for r in range(rows):
            for c in range(cols):
                if r > 0 and c > 0 and matrix[r - 1][c - 1] != matrix[r][c]:
                    return False
        return True
