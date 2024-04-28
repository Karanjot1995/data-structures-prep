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
      if root.right: traverse(root.right)
    traverse(root)
    return res
  
  #reduce the curr val as much as possible so move left
  def ceil(self,key):
    root = self.root
    ceil = -1
    while root:
      if root.val == key:
        ceil = root.val
        return ceil
      if key<root.val:
        ceil = root.val
        root = root.left
      else: root = root.right
    return ceil
  
  #increase the curr val as much as possible so move right
  def floor(self,key):
    root = self.root
    floor = -1
    while root:
      if root.val == key:
        floor = root.val
        return floor
      if key>root.val:
        floor = root.val
        root = root.right
      else:
        root = root.left
    return floor
  
  def closestValue(self,target):
    root = self.root
    diff = float('inf')
    closest = -1
    while root:
      if root.val == target:
        return root.val
      if abs(root.val-target)<=diff:
        diff = abs(root.val-target)
        closest = root.val
      if target<root.val: root = root.left 
      else: root = root.right
    return closest
  
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
print('Ceil: ',tree.ceil(32))
print('Floor: ',tree.floor(32))
print('Closest Val: ',tree.closestValue(32))
print('Insert: ',tree.insert(6))


