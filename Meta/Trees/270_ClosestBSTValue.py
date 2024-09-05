# https://leetcode.com/problems/closest-binary-search-tree-value/

'''
CLARIFYING QUESTIONS
- What if the tree is empty?
- What if the input is null
- What if we have multiple values less than the target? -- should I return the smallest of them all?
'''

class Solution:
  def closestValue(self, root, target):
    ans = root.val

    '''
    TC - O(H) will be O(N) in worst case for skewed tree but can be O(logN) for balanced BST
    SC - O(1)
    '''
    def iterative(root):
      nonlocal ans
      while root:
        if abs(root.val - target) == abs(ans - target):
          ans = min(ans, root.val)
        elif abs(root.val - target) < abs(ans - target):
          ans = root.val
        
        if target < root.val: root = root.left
        else: root = root.right
    
    '''
    TC - O(H) will be O(N) in worst case for skewed tree but can be O(logN) for balanced BST
    SC - O(N) for recursion stack space
    '''
    def dfs(root):
      nonlocal ans
      if not root: return 

      if abs(root.val - target) == abs(target - ans):
        ans = min(ans, root.val)
      elif abs(root.val - target) < abs(target - ans):
        ans = root.val
  
      if target < root.val: dfs(root.left)
      if target > root.val: dfs(root.right)
    
    # dfs(root)
    iterative(root)

    return ans



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




        