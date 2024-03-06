# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def rangeSumBST(self, root, low: int, high: int) -> int:
    self.sum = 0
    def traverse(root):
      if not root: return
      if low<=root.val<=high: self.sum+=root.val
      if root.val>=low: traverse(root.left)
      if root.val<=high: traverse(root.right)
    traverse(root)
    return self.sum
  
  def rangeSumBSTBFS(self, root, low: int, high: int) -> int:
    tot = 0
    st = [root]
    while st:
      node = st.pop()
      if low <= node.val <= high: tot += node.val
      if node.left and low <= node.val: st.append(node.left)
      if node.right and high >= node.val: st.append(node.right)
    return tot

        