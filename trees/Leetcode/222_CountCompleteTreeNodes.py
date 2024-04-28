# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def countNodes(self, root) -> int:
    cnt = [0]
    def dfs(root):
      if not root: return
      cnt[0]+=1
      if root.left: dfs(root.left)
      if root.right: dfs(root.right)

    dfs(root)
    return cnt[0]

  def countNodes(self, root):
   if not root: return 0
   lh = self.findLeftHeight(root)
   rh = self.findRightHeight(root)

   if lh == rh: return 2**lh-1

   return 1 + self.countNodes(root.left) + self.countNodes(root.right)


  def findLeftHeight(self, node):
    ht = 0
    while node:
      ht+=1
      node = node.left
    return ht
  
  def findRightHeight(self, node):
    ht = 0
    while node:
      ht+=1
      node = node.right
    return ht


        