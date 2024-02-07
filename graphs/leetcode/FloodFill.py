
def floodFill(image, sr: int, sc: int, color: int):
    rows, cols = len(image), len(image[0])
    visited = set()

    q = []
    q.append([sr,sc])
    visited.add((sr,sc))

    while q:
        row, col = q.pop(0)
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        for dr,dc in directions:
            r,c = row+dr, col+dc
            if ( r in range(rows) and c in range(cols) and image[r][c] == image[sr][sc] and (r,c) not in visited):
                q.append([r,c])
                visited.add((r,c))
                image[r][c] = color

    image[sr][sc] = color
    return image

def floodFillDFS(image, sr , sc , color):
    curr = image[sr][sc]
    rows, cols = len(image), len(image[0])
    def dfs(row, col):
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        for dr,dc in directions: 
          r,c = row+dr, col+dc
          if r in range(rows) and c in range(cols) and image[r][c] == curr and image[r][c] != color:
              image[r][c] = color
              dfs(r, c)
              
    dfs(sr, sc)
    image[sr][sc] = color
    return image



# input: image = [[1,1,1],
#                 [1,1,0],
#                 [1,0,1]] , sr=1, sc=1, color = 2
# output: [[2,2,2],
#          [2,2,0],
#          [2,0,1]]