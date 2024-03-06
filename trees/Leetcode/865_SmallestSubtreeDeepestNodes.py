# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def subtreeWithAllDeepest(self, root):
    def dfs(curr):
      if not curr: return [curr,0]
      left = dfs(curr.left)
      right = dfs(curr.right)
      # 0 => parent node, 1 => dist from root
      if left[1]>right[1]: return [left[0], left[1]+1]
      if left[1]<right[1]: return [right[0], right[1]+1]
      return [curr, left[1]+1]
    return dfs(root)[0]

  # def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
  #   if not root: return 0
  #   depth = {None:-1}
  #   def dfs(curr, parent = None):
  #     if not curr: return
  #     depth[curr] = depth[parent]+1
  #     dfs(curr.left, curr)
  #     dfs(curr.right, curr)
  #   dfs(root)
  #   max_depth = max(depth.values())
  #   print(max_depth)

  #   def traverse(node):
  #     if not node or depth.get(node,None) == max_depth: return node
  #     left = traverse(node.left)
  #     right = traverse(node.right)
  #     return node if left and right else left or right
  #   return traverse(root)
    



        