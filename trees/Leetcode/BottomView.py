
class Node:
   def __init__(self, val):
      self.left = None
      self.right = None
      self.val = val
      self.values = {}

class BinaryTree:
  def __init__(self, root):
    self.root = Node(root)

  def bottomView(self):
    root = self.root
    dict = {}

    def levelOrder(current, x):
      q = [[current,0]]
      while q:
        curr,x = q.pop(0)
        dict[x] = curr.val
        # dict[x].append([y,curr.val])
        if curr.left: q.append([curr.left,x-1])
        if curr.right: q.append([curr.right,x+1])

    levelOrder(root,0)

    res = []
    for x in sorted(dict.keys()):
      res.append(dict[x])
    return res     
      
  
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


print('Bottom View:', tree.bottomView())
