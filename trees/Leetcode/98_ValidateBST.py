# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def isValidBST(self, root) -> bool:
    order = []
    st = []
    curr = root

    while True:
      if curr != None:
        st.append(curr)
        curr = curr.left
      else:
        if not st: break
        node = st.pop()
        if order and node.val<=order[-1]: return False
        order.append(node.val)
        curr = node.right
    return True  
  

  def isValidBSTRecursive(self, root) -> bool:
    order = []
    def traverse(root):
      if root:
        if not traverse(root.left): return False
        if order and root.val <= order[-1]: return False
        order.append(root.val)
        return traverse(root.right)
      return True

    return traverse(root)

        
        