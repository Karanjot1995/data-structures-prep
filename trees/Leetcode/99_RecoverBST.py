# TC -> O(N)
# SC -> O(1)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def recoverTree(self, root):
    self.prev = None
    self.first = None
    self.middle = None
    self.second = None

    def traverse(root):
      if not root: return
      traverse(root.left)
      if self.prev and root.val<self.prev.val:
        # if only one violation which will be side by side is there store them both
        if not self.first:
          self.first = self.prev
          self.middle = root
        # if a second violation happens
        else: self.second = root
      self.prev = root
      traverse(root.right)
    traverse(root)

    if not self.second: self.first.val, self.middle.val = self.middle.val, self.first.val
    else: self.first.val, self.second.val = self.second.val, self.first.val


  #Brute force
  def recoverTreeBrute(self, root):
    order = []
    nodes = []
    def traverse(root):
      if not root:return
      traverse(root.left)
      order.append(root.val)
      nodes.append(root)
      traverse(root.right)
    traverse(root)
    order.sort()

    for i in range(len(order)):
      nodes[i].val = order[i]


        