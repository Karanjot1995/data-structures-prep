

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def preorderTraversal(self, root):
    order = []
    def traverse(root):
      if not root: return
      order.append(root.val)
      if root.left: traverse(root.left)
      if root.right: traverse(root.right)
    traverse(root)
    return order