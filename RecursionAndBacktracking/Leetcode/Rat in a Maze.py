def rathInAMaze(maze):
  if maze[0][0] != 1: return -1
  rows = len(maze)
  cols = len(maze[0])

  vis = set()
  ans = []

  def dfs(r,c, path):
    if r == rows-1 and c == cols-1: 
      ans.append(path.copy())
      return
    # directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    directions = {'L': (0, -1), 'R': (0, 1), 'D': (1, 0), 'U':(-1, 0)}

    for move,dir in directions.items():
      nr, nc = r+dir[0] , c+ dir[1]
      if nr in range(rows) and nc in range(cols) and maze[nr][nc]==1 and (nr,nc) not in vis:
        # path.append([nr,nc])
        # path.append(move)
        vis.add((nr,nc))
        dfs(nr,nc, path+[move])
        # path.pop()
        vis.remove((nr,nc))
  
  vis.add((0,0))
  # dfs(0,0, [(0,0)])
  dfs(0,0, [])
  return ans if ans else -1

# [1,0,0,0]
# [1,1,0,1]
# [1,1,0,0]
# [0,1,1,1]

maze = [[1,0,0,0], [1,1,0,1], [1,1,0,0], [0,1,1,1]]
# maze = [[1,0,1,0]]
print(rathInAMaze(maze))