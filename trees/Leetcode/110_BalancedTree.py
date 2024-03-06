from Templates.tree import BinaryTree, Node

class Tree(BinaryTree):
  def isBalanced(self) -> bool:
    curr = self.root
    diff = [0]
    if not curr: return True
    def traverse(curr):
      if not curr: return 0
      left = traverse(curr.left)
      right = traverse(curr.right)
      diff[0] = max(diff[0], abs(left-right))
      return 1+max(left,right)
    traverse(curr)
    return False if diff[0] > 1 else True
  
  
  def isBalanced(self):
    curr = self.root
    def traverse(curr):
      if not curr: return 0
      left = traverse(curr.left)
      right = traverse(curr.right)
      if left == -1 or right == -1: return -1
      if abs(left-right)>1: return -1
      return 1+max(left,right)

    return traverse(curr) != -1
  

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

print(tree.isBalanced())