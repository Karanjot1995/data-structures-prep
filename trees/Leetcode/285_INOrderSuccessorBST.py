class TreeNode:
   def __init__(self, val):
      self.left = None
      self.right = None
      self.val = val

class BinaryTree:
  def __init__(self, root):
    self.root = TreeNode(root)
    
   # TC -> O(H) and SC -> O(1)
  def inorderSuccessor(self, root, p):
    successor = None
    #leftmost value after that number
    while root:
      if p.val<root.val:
        successor = root
        root = root.left
      else: root=root.right
    print(successor.val)
    return successor

  #Brute Force TC -> O(N) and SC -> O(N)
  def inorderSuccessorBrute(self, root, p):
    order = []
    def traverse(root):
      if not root: return
      if root.left: traverse(root.left)
      order.append(root)
      if root.right: traverse(root.right)
    traverse(root)
    for i in range(0,len(order)-1):
      if order[i].val == p.val:
        return order[i+1]
    return None
  
  # TC -> O(H) and SC -> O(1)
  def inorderPredecessor(self, root, p):
    predeccessor = None
    #rightmost value before that number
    while root:
      if p.val<=root.val: root = root.left
      else: 
        predeccessor = root
        root=root.right
    print(predeccessor.val)
    return predeccessor
  

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

print(tree.inorderSuccessor(tree.root,TreeNode(20)))
print(tree.inorderPredecessor(tree.root,TreeNode(35)))
