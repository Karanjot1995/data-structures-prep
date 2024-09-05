# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# https://leetcode.com/problems/range-sum-of-bst/

'''
BRUTE
Visit each node and calculate sum of nodes in between low and high (but we are not taking advantage of BST property)
TC - O(N)
SC - O(N) (recursive stack)


INTUITION
If the current node is less than low then there is no point traversing the left sub tree
-> when should we go left ? if node.val > low

If the current node is greater than high then there is no point in traversing the right sub tree
-> when should we go right ? if node.val < high

-> low < root.val < high

TC - O(N)
SC - O(N) recursive stack
'''
class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        total = 0
        
        def dfs(root):
            nonlocal total
            
            if not root:
                return

            if root.val >= low and root.val <= high:
                total += root.val

            # WHEN will we go left?
            if root.val > low:
                dfs(root.left)

            # WHEN will we go right?
            if root.val < high:
                dfs(root.right)
        
        dfs(root)
        return total



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

        