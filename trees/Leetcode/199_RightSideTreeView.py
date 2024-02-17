# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Templates.tree import BinaryTree, Node

class Tree(BinaryTree):
    def rightSideView(self):
      root = self.root
      order = []
      def traverse(root, level):
        if not root: return
        if level == len(order):
          order.append(root.val)
        if root.right: traverse(root.right,level+1)
        if root.left: traverse(root.left,level+1)
        
      traverse(root,0)
      return order
    
    def rightSideViewLevelOrder(self):
      root = self.root
      order = []
      q = [root]

      while q:
        level = None
        for i in range(len(q)):
          curr = q.pop(0)
          if not curr: break
          level = curr.val
          if curr.left: q.append(curr.left)
          if curr.right: q.append(curr.right)
        if level != None: order.append(level)
      
      return order


#             1
#           /    \
#         2        3
#       /   \     /  \
#      4     5   6    7
#    /  \
#   8     9

tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.left.left.left = Node(8)
tree.root.left.left.right = Node(9)

print(tree.rightSideView())
print(tree.rightSideViewLevelOrder())