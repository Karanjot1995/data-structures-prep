# All root to leaf nodes paths


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def binaryTreePaths(self, root):
    paths = []

    def traverse(root,path):
      newstr = path+str(root.val)
      if not root.left and not root.right:
        paths.append(newstr)
        return
      newstr+='->'
      if root.left: traverse(root.left,newstr)
      if root.right: traverse(root.right,newstr)
      return

    traverse(root,'')
    return paths

        