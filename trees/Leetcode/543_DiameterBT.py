from Templates.tree import BinaryTree, Node

class Tree(BinaryTree):
  def diameterOfBinaryTree(self) -> int:
    current = self.root
    d = [0]
    def traverse(curr):
      if not curr: return 0
      left = traverse(curr.left)
      right = traverse(curr.right)
      d[0] = max(d[0], left+right)
      return 1+max(left,right)
    traverse(current)
    return d[0]
  
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

print(tree.diameterOfBinaryTree())