# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def inorderTraversal(self, root):
    order = []
    def traverse(curr):
      if not root: return
      if curr.left: traverse(curr.left)
      order.append(curr.val)
      if curr.right: traverse(curr.right)
    traverse(root)
    return order
        