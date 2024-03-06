# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def isValidBST(self, root) -> bool:
    maxi = float('-inf')
    # order = []
    st = []
    curr = root
    while True:
      if curr:
        st.append(curr)
        curr = curr.left
      else:
        if not st: break
        node = st.pop()
        if node.val<=maxi: return False
        maxi = max(node.val, maxi)
        # if order and node.val<= order[-1]: return False
        # order.append(node.val)
        curr = node.right
    return True
        
  # def __init__(self):
  #   self.maxi = float('-inf')
    
  # def isValidBST(self, root):
  #   order = []
  #   def traverse(root):
  #     if root:
  #       if not traverse(root.left): return False
  #       if root.val<=self.maxi: return False
  #       self.maxi = max(self.maxi, root.val)
  #       return traverse(root.right)
  #     return True
  #   return traverse(root)

  # def isValidBST(self, root):
  #   return self.isValid(root, float('-inf'), float('inf'))

  # def isValid(self,root, minVal, maxVal):
  #   if not root: return True
  #   if root.val >= maxVal or root.val <= minVal: return False
  #   return self.isValid(root.left, minVal, root.val) and self.isValid(root.right, root.val, maxVal)

        
        