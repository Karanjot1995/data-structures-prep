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
  
  def search(self,val):
    root = self.root
    while root and root.val!=val:
      root = root.left if val<root.val else root.right
    return root
  
  def findLastRight(self,root):
    if not root.right: return root
    return self.findLastRight(root.right)
  
  def helper(self,root):
    if not root.left: return root.right
    elif not root.right: return root.left

    #find the last right in the left subtree and 
    # attach the right subtree at he bottom of it
    rightChild = root.right  #(20,15,25,21,26)
    lastRight = self.findLastRight(root.left) #6
    lastRight.right = rightChild #6->20->...
    return root.left #5->6->20...

  def delete(self, key):
    root = self.root
    if not root: return
    if not self.search(key): return False
    if root.val == key: return self.helper(root)
    
    curr = root
    while root:
      if key<root.val:
        if root.left and root.left.val == key:
          root.left = self.helper(root.left)  #30 will directly attach left or right of 10(removed node)
          break
        else: root = root.left
      else:
        if root.right and root.right.val == key:
          root.right = self.helper(root.right)
          break
        else: root = root.right
    return curr



#             30
#            /    \
#         10       40
#       /   \      /  \
#      5     20  35    45
#       \    / \
#        6  15  25
#               / \
#             21   26

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
# print('Delete: ',tree.delete(10))


