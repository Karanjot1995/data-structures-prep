'''
Time Complexity: O(N+E), where N is the number of nodes in the graph, and E is the number of edges. 
We explore each node once when we transform it from uncolored to colored, traversing all its edges in the process.

Space Complexity: O(N), the space used to store the color.
'''

class Solution:
  def checkBipartiteDFS(self, graph, colors, curr, currCol):
    colors[curr] = currCol
    for neighbor in graph[curr]:
      if colors[neighbor]==-1:
        if not self.checkBipartiteDFS(graph, colors, neighbor, 1 - currCol):
          return False
      elif currCol == colors[neighbor]:
        return False
    return True

  def isBipartite(self, graph) -> bool:
    n = len(graph)
    colors = [-1]*n
    
    for node in range(n):
      if colors[node]==-1 and not self.checkBipartiteDFS(graph,colors,node,0): return False
    
    return True
  

# Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# Output: false