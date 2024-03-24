from collections import defaultdict
# https://www.codingninjas.com/studio/problems/m-coloring-problem_981273

# graph is adj matrix
# TC - O(M^N) where N is the total number of nodes (https://www.youtube.com/watch?v=052VkKhIaQ4)
# SC - O(N) -> depth of tree will be N max + color array of size N

def graphColoring(graph, m):
  V = len(graph)
  colorHash = [0]*V

  
  def isColorPossible(node, color):
    for i in range(V):
      if graph[node][i]==1 and colorHash[i]==color: return False
    return True
  
  def dfs(node):
    if node == V: return True
    
    for c in range(1,m+1):
      if isColorPossible(node, c) == True:
        colorHash[node] = c        
        if dfs(node+1) == True: return True
        colorHash[node] = 0
    return False
  print(colorHash)
      
  return dfs(0)

graph = [[0,1,1,1],[1,0,1,1],[1,1,0,0],[1,1,0,0]]

print(graphColoring(graph, 3))
