"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
  def treeToDoublyList(self, root):
    if not root: return None

    first, last = None, None

    def dfs(curr):
      nonlocal first, last
      if curr:
        dfs(curr.left)
        if last:
          last.right = curr
          curr.left = last
        else: first = curr
        last = curr
        dfs(curr.right)

    dfs(root)

    last.right = first
    first.left = last

    return first