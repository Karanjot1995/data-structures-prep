
class Node:
   def __init__(self, val):
      self.left = None
      self.right = None
      self.val = val
      self.values = {}

class BinaryTree:
  def __init__(self, root):
    self.root = Node(root)

  def rootToNodePath(self,target):
    root = self.root
    arr = []
    if not root:
      return arr

    def traverse(root,arr):
      if not root: return False
      arr.append(root.val)
      if root.val == target:
        return True
      if traverse(root.left,arr) or traverse(root.right,arr): return True
      arr.pop()
      return False

    traverse(root,arr)
      
      
    return arr
   
     

#             1
#           /    \
#         2        3
#       /   \     /  \
#      4     5   6    7
#    /  \
#   8     9

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.left.left.left = Node(8)
tree.root.left.left.right = Node(9)

print(tree.rootToNodePath(9))