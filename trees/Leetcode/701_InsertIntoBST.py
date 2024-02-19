# height in BST is generally log2(N)
# TC -> O(logN)


from collections import deque

class TreeNode:
   def __init__(self, val):
      self.left = None
      self.right = None
      self.val = val

class BinaryTree:
  def __init__(self, root):
    self.root = TreeNode(root)
    self.stack = []

  def inOrder(self):
    root = self.root
    res = []
    def traverse(root):
      if root.left: traverse(root.left)
      res.append(root.val)
      if root.left: traverse(root.right)
    traverse(root)
    return res
  
  def insert(self, val):
    root = self.root
    newNode = TreeNode(val)
    if not root:
      root = newNode
      return
    curr = root
    while curr:
      if val < curr.val: 
        if not curr.left:
          curr.left = newNode
          break
        curr = curr.left
      else: 
        if not curr.right:
          curr.right = newNode
          break
        curr = curr.right
    return root


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


print(tree.inOrder())
print('Insert: ',tree.insert(6))


