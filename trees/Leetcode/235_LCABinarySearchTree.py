# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#TC -> O(H)
#find the point of split

class Solution:
  def lowestCommonAncestor(self, root, p, q):
    def traverse(root, p,q):
      if not root: return None
      if p.val<root.val and q.val<root.val: return traverse(root.left,p,q)
      elif p.val>root.val and q.val>root.val : return traverse(root.right,p,q)
      return root
    return traverse(root,p,q)
    def traverse(root, p,q):
      if not root: return None
      if (p.val<=root.val and q.val>=root.val) or (q.val<=root.val and p.val>=root.val): return root
      
      if p.val and q.val <root.val: return traverse(root.left,p,q)
      else: return traverse(root.right,p,q)
    return traverse(root,p,q)
  

#             1
#           /    \
#         2        3
#       /   \     /  \
#      4     5   6    7
#    /  \
#   8     9