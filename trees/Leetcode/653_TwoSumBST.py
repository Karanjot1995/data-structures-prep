# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def findTarget(self, root, k):
    diff = {}
    def traverse(root):
      if not root: return False
      if root.val in diff: return True
      diff[k-root.val] = True
      return traverse(root.left) or traverse(root.right)
    return traverse(root)
  

#######    BST Iterator solution     #########

class BSTIterator:
  def __init__(self,root, isReverse):
    self.stack = []
    self.reverse = isReverse
    self.pushAll(root)


  def pushAll(self, root):
    while root:
      self.stack.append(root)
      if self.reverse: root = root.right
      else: root = root.left
  
  def next(self):
    node = self.stack.pop()
    if self.reverse: self.pushAll(node.left) #for before val
    else: self.pushAll(node.right)   #for next val
    return node.val
  
  def hasNext(self):
    return self.stack
  
class Solution:
  def findTarget(self, root, k):
    if not root: return False
    
    # for next
    l = BSTIterator(root,False)
    # for before
    r = BSTIterator(root,True)

    def traverse(root):
      if not root: return False
      if root.val in diff: return True
      diff[k-root.val] = True
      return traverse(root.left) or traverse(root.right)
    return traverse(root)
  

  
