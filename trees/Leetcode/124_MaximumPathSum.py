from Templates.tree import BinaryTree, Node

class Tree(BinaryTree):
  def maxPathSum(self):
    current = self.root
    if not current: return 0
    if not current.left and not current.right: return current.val
    d = [float('-inf')]
    def traverse(curr):
      if not curr: return 0
      left = max(0,traverse(curr.left))
      right = max(0,traverse(curr.right))
      d[0] = max(d[0], curr.val+left+right)
      return curr.val+ max(left,right)
    traverse(current)
    return d[0]
  
  # def maxPathSum(self):
  #   current = self.root
  #   if not current: return 0
  #   if not current.left and not current.right: return current.val
  #   d = [float('-inf')]
  #   def traverse(curr):
  #     if not curr: return 0
  #     left = traverse(curr.left)
  #     right = traverse(curr.right)
  #     if left<0: left = 0
  #     if right<0: right = 0
  #     d[0] = max(d[0], curr.val+left+right)
  #     return curr.val+ max(left,right)
  #   traverse(current)
  #   return d[0]
  
#            -10
#           /    \
#         9        20
#                 /  \
#                15    7


tree = Tree(-10)
tree.root.left = Node(9)
tree.root.right = Node(20)
tree.root.right.left = Node(15)
tree.root.right.right = Node(7)


print(tree.maxPathSum())