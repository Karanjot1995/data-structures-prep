# height in BST is generally log2(N)
# TC -> O(logN)

class TreeNode:
   def __init__(self, val):
      self.left = None
      self.right = None
      self.val = val
      self.values = {}

  #  def PrintTree(self):
  #     print(self.data)

class BinaryTree:
  def __init__(self, root):
    self.root = TreeNode(root)
    self.stack = []

  # def insert(self, val):
    # root = self.root
    # newNode = TreeNode(val)
    # if not root:
    #   root = newNode
    #   return root
    # while root:
    #   if newNode.val < root.val:
    #     if not root.left:
    #       root.left = newNode
    #       break
    #     root = root.left
    #   else:
    #     if not root.right:
    #       root.right = newNode
    #       break
    #     root = root.right
    # return root

#             30
#            /    \
#         10       40
#       /   \      /  \
#      5     20  35    45
#           /  \
#         15    25

tree = BinaryTree(30)
tree.root.left = TreeNode(10)
tree.root.left.left = TreeNode(5)
tree.root.left.right = TreeNode(20)

tree.root.right = TreeNode(40)
tree.root.right.left = TreeNode(35)
tree.root.right.right = TreeNode(45)

tree.root.left.right.left = TreeNode(15)
tree.root.left.right.right = TreeNode(25)


