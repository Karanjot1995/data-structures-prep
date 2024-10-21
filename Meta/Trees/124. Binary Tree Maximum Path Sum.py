# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def maxPathSum(self, root) -> int:
    if not root: return 0
    if not root.left and not root.right: return root.val

    max_sum = -float("inf")

    def dfs(root):
      if not root: return 0
      nonlocal max_sum
      l = max(0,dfs(root.left))
      r = max(0,dfs(root.right))
      max_sum = max(max_sum, root.val+l+r)
      return root.val + max(l,r)

    dfs(root)
    return max_sum