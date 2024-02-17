class Solution:
  def changeTree(self,root):
    if not root: return
    child = 0
    if root.left:
      child += root.left.val
    if root.right:
      child += root.right.val

    if child >= root.val: root.val = child
    else:
      if root.left: root.left.val = child
      elif root.right: root.right.val = child

    self.changeTree(root.left)
    self.changeTree(root.right)
    tot = 0
    if root.left: tot += root.left.val
    if root.right:  tot+= root.right.val
    if root.left or root.right: root.val = tot