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
