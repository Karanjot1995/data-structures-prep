
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
  def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    if not node:
      return node

    dict = {}

    def dfs(node):
      if node in dict:
        return dict[node]
      copy = Node(node.val)
      dict[node] = copy
      for nb in node.neighbors:
        copy.neighbors.append(dfs(nb))
      return copy

    return dfs(node)