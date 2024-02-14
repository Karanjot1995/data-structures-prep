# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def levelOrder(self, root):
    q = [root]
    order = []

    while q:
      level = []
      for i in range(len(q)):
        curr = q.pop(0)
        if not curr: break
        level.append(curr.val)
        if curr.left: q.append(curr.left)
        if curr.right: q.append(curr.right)
      if level: order.append(level)
    return order

      