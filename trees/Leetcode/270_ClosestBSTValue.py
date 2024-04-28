# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def closestValue(self, root, target):
    closest = root.val
    diff = float('inf')
    while root:
      closest = min(root.val, closest, key = lambda x: (abs(target - x), x))
      # if root.val == target: return root.val
      # if abs(root.val-target)<diff:
      #   diff = abs(root.val-target)
      #   closest = root.val
      # elif abs(root.val-target) == diff:
      #   if root.val<closest: closest = root.val
      root = root.left if target < root.val else root.right
    return closest




        