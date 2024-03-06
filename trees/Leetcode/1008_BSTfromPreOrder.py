# TC -> O(N)
# SC -> O(1)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  def bstFromPreorder(self, preorder):
    self.i = 0

    def build(bound):
      if self.i == len(preorder) or preorder[self.i]>bound: return None
      root = TreeNode(preorder[self.i])
      self.i+=1
      #lower bound = root.left and upper bound = bound which is the previous value
      root.left = build(root.val)
      root.right = build(bound)
      return root
    
    build(float('inf'))