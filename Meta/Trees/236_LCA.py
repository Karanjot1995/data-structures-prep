# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
CLARIFYING QUESTIONS
- Will there always be a common ancestor?
- Will p and q always be present? (if not then this becomes LCA II (LC 1644) problem)

TC - O(N)
SC - O(N)
'''


class Solution:
  def lowestCommonAncestor(self, root, p, q):
    if not root or not q or not p: return None

    def dfs(root):
      if not root: return None
      if p == root or q == root: return root
      l = dfs(root.left)
      r = dfs(root.right)
      if l and r: return root
      elif l: return l
      else: return r
    return dfs(root)
  
    def traverse(root, p,q):
      if not root or root==p or root == q: return root
      left = traverse(root.left, p, q)
      right = traverse(root.right, p, q)
      if not left: return right
      elif not right: return left
      #means if both have been found
      else: return root
    return traverse(root,p,q)
  

  def lowestCommonAncestor(self, root, p, q):
    arr1= []
    arr2= []

    def traverse(root, arr, x):
      if not root: return False
      arr.append(root)
      if root.val == x.val: return True
      if traverse(root.left, arr, x) or traverse(root.right, arr, x): return True
      arr.pop()
      return False

    traverse(root,arr1,p) 
    traverse(root,arr2,q) 
    min_l = min(len(arr1),len(arr2))
    lca = None
    for i in range(min_l):
      if arr1[i].val!=arr2[i].val:
        break
      lca = arr1[i]
    return lca
  


#             1
#           /    \
#         2        3
#       /   \     /  \
#      4     5   6    7
#    /  \
#   8     9