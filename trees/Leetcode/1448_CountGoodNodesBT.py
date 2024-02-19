
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root):
      if not root: return []
      self.count = 0
      #every elem should be greater or equal to the prev max in the path
      def traverse(root,maxi):
        if not root: return
        if root.val>=maxi:
          maxi = root.val
          self.count+=1
        if root.left: traverse(root.left, maxi)
        if root.right: traverse(root.right, maxi)

      traverse(root,float('-inf'))
      return self.count