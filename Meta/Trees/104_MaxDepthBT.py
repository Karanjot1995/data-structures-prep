class Solution:
  def maxDepth(self, root):
    curr = root
    if not curr: return 0
    left = self.maxDepth(curr.left)
    right = self.maxDepth(curr.right)
    
    return 1+max(left,right)
  
class Solution:
  def maxDepth(self, root):
    curr = root
    if not curr:
      return 0
    def traverse(curr):
      if not curr: return 0
      left = traverse(curr.left)
      right = traverse(curr.right)
      return 1+max(left,right)
    return traverse(curr)
  
class Solution:
  def maxDepth(self, root):
    if not root: return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))