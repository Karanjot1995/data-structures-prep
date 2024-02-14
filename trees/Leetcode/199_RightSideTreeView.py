# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
      order = []
      def dfs(root, level):
        if not root:
          return
        if level == len(order):
          order.append(root.val)
        if root.right: dfs(root.right,level+1)
        if root.left: dfs(root.left,level+1)
      dfs(root,0)
    
      return order
    
    def rightSideViewLevelOrder(self, root):
      order = []
      q = [root]

      while q:
        level = None
        for i in range(len(q)):
          curr = q.pop(0)
          if not curr: break
          level = curr.val
          if curr.left: q.append(curr.left)
          if curr.right: q.append(curr.right)
        if level != None: order.append(level)
      
      return order

