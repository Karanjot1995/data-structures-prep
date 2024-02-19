#TC -> O(N)
#SC -> O(N)

class Node:
  def __init__(self, val):
    self.left = None
    self.right = None
    self.val = val
    self.values = {}

class BinaryTree:
  def __init__(self, root):
    self.root = Node(root)


  def flatten(self, root):
    prev = [None]
    def traverse(node):
      if not node: return
      traverse(node.right)
      traverse(node.left)
      node.right = prev[0]
      node.left = None
      prev[0] = node
    traverse(root)
 
    return root
  
  def flattenIterative(self, root):
    st = [root]
    while st:
      curr = st.pop()
      if not curr: break
      if curr.right: st.append(curr.right)
      if curr.left: st.append(curr.left)
      if st: curr.right = st[-1]
      curr.left = None
    return root
  
  def flattenIterative2(self, root):
    curr = root
    prev = None
    while curr:
      if curr.left:
        prev = curr.left #2
        while prev.right:
          prev = prev.right #4
        prev.right = curr.right #4->5
        curr.right = curr.left #1->2
        curr.left = None
      curr = curr.right
    return root

        
     
    


#             1
#           /    \
#         2        5
#       /   \        \
#      3     4        6
#                    /
#                   7

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(5)
tree.root.left.left = Node(3)
tree.root.left.right = Node(4)
tree.root.right.right = Node(6)
tree.root.right.right.left = Node(7)


print('Flatten to linked list:', tree.flatten(tree.root))
print('Flatten to linked list Iterative:', tree.flattenIterative(tree.root))
print('Flatten to linked list Iterative2:', tree.flattenIterative2(tree.root))
# print(tree.dfsPre(tree.root))
