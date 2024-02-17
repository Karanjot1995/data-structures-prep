# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def isSubtree(self, root, subRoot):
    if not root: return False

    # def isSameTree(root, subRoot):
    #   if not root or not subRoot: return root==subRoot
    #   if root.val != subRoot.val: return False
    #   return isSameTree(root.left, subRoot.left) and isSameTree(root.right, subRoot.right)
    
    if self.isSameTree(root,subRoot): return True
    #if checking from first node of both did not give True 
    #then move one left or right in the main tree
    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
  
  def isSameTree(self,p,q):
    if not p or not q: return p == q
    if p.val != q.val: return False
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
