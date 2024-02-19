
class Node:
   def __init__(self, val):
      self.left = None
      self.right = None
      self.val = val
      self.values = {}

class BinaryTree:
  def __init__(self, root):
    self.root = Node(root)

  ##### Morris traversal #####
  def inOrder(self):
    root = self.root
    order = []
    curr = root
    while curr:
      if not curr.left:
        order.append(curr.val)
        curr = curr.right
      else:
        prev = curr.left
        while prev.right and prev.right!=curr:
          prev = prev.right

        if not prev.right:
          prev.right = curr
          curr = curr.left
        else:
          prev.right = None
          order.append(curr.val)
          curr = curr.right
    return order
  
  def preOrder(self):
    root = self.root
    order = []
    curr = root
    while curr:
      if not curr.left:
        order.append(curr.val)
        curr = curr.right
      else:
        prev = curr.left
        while prev.right and prev.right!=curr:
          prev = prev.right

        if not prev.right:
          prev.right = curr
          order.append(curr.val)
          curr = curr.left
        else:
          prev.right = None
          curr = curr.right
    return order

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


print('Morris InOrder Traverse:', tree.inOrder())
print('Morris preOrder Traverse:', tree.preOrder())
  



