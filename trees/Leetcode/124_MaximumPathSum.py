from Templates.tree import BinaryTree, Node


'''
Time complexity: O(n)

Each node in the tree is visited only once. During a visit, we perform constant time operations, 
including two recursive calls and calculating the max path sum for the current node. So the time complexity is O(n).

Space complexity: O(n)
We don't use any auxiliary data structure, but the recursive call stack can go as deep as the tree's height. 
In the worst case, the tree is a linked list, so the height is n. Therefore, the space complexity is O(n).

'''
class Tree(BinaryTree):
  def maxPathSum(self):
    current = self.root
    if not current: return 0
    if not current.left and not current.right: return current.val
    maxPath = float('-inf')
    def traverse(curr):
      if not curr: return 0
      nonlocal maxPath
      left = max(0,traverse(curr.left))
      right = max(0,traverse(curr.right))
      maxPath = max(maxPath, curr.val+left+right)
      return curr.val+ max(left,right)
    traverse(current)
    return maxPath
  
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