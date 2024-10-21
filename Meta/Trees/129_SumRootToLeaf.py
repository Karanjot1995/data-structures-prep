# https://leetcode.com/problems/sum-root-to-leaf-numbers/

class Solution:
    '''
    APPROACH 1: Preorder DFS (taking num as string)

    TC - O(N)
    SC - O(N)
    '''
    def sumNumbers1(self, root) -> int:
        total = 0
        if not root: return 0

        def dfs(root, path):
            nonlocal total
            if not root: return
            path += str(root.val)
            if not root.left and not root.right:
                total += int(path)
                return
            dfs(root.left, path)
            dfs(root.right, path)
        
        dfs(root, "")

        return total
    
    '''
    APPROACH 2: Preorder DFS (taking num as integer)

    TC - O(N)
    SC - O(N)
    '''
    def sumNumbers(self, root) -> int:
        total = 0
        
        def preorder(root, num):
            nonlocal total
            if not root: return
            num = num * 10 + root.val
            if not root.left and not root.right:
                total += num
                return
            preorder(root.left, num)
            preorder(root.right, num)
        
        preorder(root, 0)
        return total




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Node:
   def __init__(self, val):
      self.left = None
      self.right = None
      self.val = val
      self.values = {}

class BinaryTree:
  def __init__(self, root):
    self.root = Node(root)
    
  def sumNumbers(self, root) -> int:
    total = 0
    def traverse(root,num):
      if not root: return
      nonlocal total
      num=num*10+root.val
      if not root.left and not root.right:
        total+=num
        return
      if root.left: traverse(root.left,num)
      if root.right: traverse(root.right,num)
    traverse(root,0)

    return total
  
#             1
#           /    \
#         2        3
#       /   \     /  \
#      4     5   6    7
#           /  \
#          8     9


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.left.right.left = Node(8)
tree.root.left.right.right = Node(9)

print(tree.sumNumbers(tree.root))

# eg = [1,2,3]
#       1
#     2   3
# 1->2 + 1->3 = 12+13 = 25
