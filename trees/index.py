# Full BT - all level full ie each node has either 0 or 2 children
# complete BT - al levels are completely filled except the last level and last level has nodes as left as possible
# Balanced Tree - height is at max log(N)   N = 8 => max height = log2(8) = 3
from queue import PriorityQueue

class Node:
  def __init__(self, val):
    self.left = None
    self.right = None
    self.val = val
    self.values = {}

class BinaryTree:
  def __init__(self, root):
    self.root = Node(root)

  def insert(self, val):
    root = self.root
    newNode = Node(val)
    if not root:
      root = newNode
      return
    
    while root:
      if newNode.val < root.val:
        if not root.left:
          root.left = newNode
          return
        root = root.left
      else:
        if not root.right:
          root.right = newNode
          return
        root = root.right


tree = BinaryTree(8)
tree.insert(3)
tree.insert(10)
tree.insert(1)
tree.insert(6)
tree.insert(14)
tree.insert(4)
tree.insert(7)
tree.insert(13)

print(tree)