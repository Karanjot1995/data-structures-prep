

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
      if root.left: traverse(root.left)
      if root.right: traverse(root.right)
      order.append(root.val)
    traverse(root)
    return order