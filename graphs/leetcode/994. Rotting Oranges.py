def orangesRotting(grid):
	if not grid:
		return 0
	rows, cols = len(grid), len(grid[0])
	vis = set()
	fresh_cnt = 0
	minutes = 0
	q = []
  
	for r in range(rows):
		for c in range(cols):
			if grid[r][c]==2:
				q.append([r,c,minutes])
				vis.add((r,c))
			elif grid[r][c]==1:
				fresh_cnt+=1

	while q:
		row, col, m = q.pop(0)
		directions = [[1,0], [-1,0], [0,1], [0,-1]]
		minutes = max(minutes,m)
		for dr, dc in directions:
			r,c = row+dr, col+dc
			if r in range(rows) and c in range(cols) and grid[r][c]==1 and (r,c) not in vis:
				q.append([r,c,m+1])
				vis.add((r,c))
				fresh_cnt-=1
	
	return minutes if fresh_cnt==0 else -1

			
#   for r in range(rows):
# 	  for c in range(cols):
# 		  if grid[r][c] == 2:
# 				q.append([r,c,minutes])
# 				visited.add((r,c))
# 			elif grid[r][c]==1:
# 				fresh_cnt +=1

# 	while q:
# 		row, col, t = q.pop(0)
# 		directions = [[1,0], [-1,0], [0,1], [0,-1]]
# 		minutes = max(minutes, t)
		
# 		for dr,dc in directions:
# 			r,c = row+dr, col+dc
# 			if (r in range(rows) and c in range(cols) and grid[r][c]==1 and (r,c) not in visited):
# 				q.append([r,c,t+1])
# 				grid[r][c]=2
# 				visited.add((r,c))
# 				fresh_cnt-=1

#   return minutes if fresh_cnt ==0 else -1

# # input: image = [[1,1,1],
# #                 [1,1,0],
# #                 [1,0,1]] , sr=1, sc=1, color = 2
# # output: [[2,2,2],
# #          [2,2,0],
# #          [2,0,1]]
