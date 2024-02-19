# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  
  # Iterative
  def searchBST(self, root, val):
    while root and root.val!=val:
      root = root.left if val<root.val else root.right
    return root
    # OR
    while root:
      if val<root.val: root = root.left
      elif val>root.val: root = root.right
      else: return root
    
  # Recursive
  def searchBST(self, root, val):
    if not root: return
    if val < root.val: return self.searchBST(root.left, val)
    elif val > root.val: return self.searchBST(root.right, val)
    return root