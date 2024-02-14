# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def isSymmetric(self, root):
    if not root: return False
    def traverse(left,right):
      if not left or not right:
        return left==right
      if left.val!=right.val: return False
      return traverse(left.left, right.right) and traverse(left.right, right.left)
      
    return traverse(root.left, root.right)
        