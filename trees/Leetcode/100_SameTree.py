from Templates.tree import BinaryTree, Node

class Tree(BinaryTree):

  def isSameTree(self, p, q):
    if not p or not q: return p == q
    if p.val != q.val: return False
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
  
  # def isSameTree(self, p, q) -> bool:
  #   def traverse(curr,order):
  #     if curr == None:
  #       order.append(None)
  #       return
  #     order.append(curr.val)
  #     traverse(curr.left, order)
  #     traverse(curr.right, order)

  #   order1 = []
  #   order2 = []
  #   traverse(p, order1)
  #   traverse(q, order2)
  #   if len(order1)!=len(order2):
  #     return False
  #   print(order1, order2)
  #   for i in range(len(order1)):
  #     if order1[i]!=order2[i]:
  #       return False
  #   return True
  

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

print(tree.isSameTree())