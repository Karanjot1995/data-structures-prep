from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def zigzagLevelOrder(self, root):
    if not root: return []
    q = deque([root])
    order = []
    isRev = True
    while q:
      lvl = []
      for i in range(len(q)):
        curr = q.popleft()
        if not curr: break
        lvl.append(curr.val)
        if curr.left: q.append(curr.left)
        if curr.right: q.append(curr.right)
      if isRev: order.append(lvl)
      else: order.append(lvl[::-1])
      isRev = not isRev
    return order
        

  def zigzagLevelOrder(self, root):
    if not root: return []
    root = self.root
    order = []
    q = [root]
    leftToright = True
    while q:
      n = len(q)
      level = [0]*n
      for i in range(n):
        node = q.pop(0)
        if node==None: break
        if leftToright: level[i] = node.val
        else: level[n-1-i] = node.val
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
      leftToright = not leftToright
      order.append(level)

    return order