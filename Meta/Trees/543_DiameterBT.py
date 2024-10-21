from Templates.tree import BinaryTree, Node

'''
Time complexity: O(N). This is because in our recursion function longestPath, we only enter and exit from each node once. 
We know this because each node is entered from its parent, and in a tree, nodes only have one parent.

Space complexity: O(N). The space complexity depends on the size of our implicit call stack during our DFS, 
which relates to the height of the tree. In the worst case, the tree is skewed so the height of the tree is O(N). 
If the tree is balanced, it'd be O(logN).

'''
class Tree(BinaryTree):
  def diameterOfBinaryTree(self) -> int:
    current = self.root
    d = 0
    def traverse(curr):
      if not curr: return 0
      nonlocal d
      left = traverse(curr.left)
      right = traverse(curr.right)
      d = max(d, left+right)
      return 1+max(left,right)
    traverse(current)
    return d
  
  
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