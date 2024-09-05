
class Node:
   def __init__(self, val):
      self.left = None
      self.right = None
      self.val = val
      self.values = {}

class BinaryTree:
  def __init__(self, root):
    self.root = Node(root)

  def bfs(self):
    order = []
    current = self.root
    q = [current]

    while q:
      curr = q.pop(0)
      order.append(curr.val)
      if curr.left: q.append(curr.left)
      if curr.right: q.append(curr.right)
    return order
  
  def dfsPre(self,root):
    if root == None:
      return
    self.dfsPre(root.left)
    self.dfsPre(root.right)
  
  def preOrderRecursive(self):
    order = []
    current = self.root
    if current == None:
      return
    def traverse(curr):
      order.append(curr.val)
      if curr.left:
        traverse(curr.left)
      if curr.right:
        traverse(curr.right)
    traverse(current)
    return order
  
  def preOrderIterative(self):
    order = []
    root = self.root
    if root == None:
      return
    
    q = [root]
    while q:
      curr = q.pop()
      order.append(curr.val)
      if curr.right: q.append(curr.right)
      if curr.left: q.append(curr.left)

    return order
  
  def inOrderRecursive(self):
    order = []
    current = self.root
    if current == None:
      return
    def traverse(curr):
      if curr.left:
        traverse(curr.left)
      order.append(curr.val)
      if curr.right:
        traverse(curr.right)
    traverse(current)
    return order
  
  def inOrderIterative(self):
    curr = self.root
    st = []
    order = []

    while True:
      if curr != None:
        st.append(curr)
        curr = curr.left
      else:
        if not st:
          break
        node = st.pop()
        order.append(node.val)
        curr = node.right
    return order  

  
  def postOrderRecursive(self):
    order = []
    current = self.root
    if current == None:
      return
    def traverse(curr):
      if curr.left:
        traverse(curr.left)
      if curr.right:
        traverse(curr.right)
      order.append(curr.val)
    traverse(current)
    return order
  
  def postOrderIterative(self):
    node = self.root
    # st = []
    order = []

    q = [node]
    while q:
      curr = q.pop()
      order.append(curr.val)
      if curr.left: q.append(curr.left)
      if curr.right: q.append(curr.right)

    return order[::-1]
  
  def postOrderIterativeOneStack(self):
    curr = self.root
    st = [curr]
    order = []
    while True:
      # print(curr.val)
      if curr != None:
        st.append(curr)
        curr = curr.left
      else:
        if not st: break
        # curr = st[-1]
        temp = st[-1].right
        if temp == None:
          temp = st.pop()
          order.append(temp.val)
          while st and temp == st[-1].right:
            temp = st.pop()
            order.append(temp.val)
        else:
          curr = temp
      

    return order  
     
      
    

  def countNodes(self):
    root = self.root
    self.count = 0
    def traverse(root):
      if not root:
          return
      if root.left:
          traverse(root.left)
      if root.right:
          traverse(root.right)
      self.count+=1
    traverse(root)
    return self.count

#             1
#           /    \
#         2        3
#       /   \     /  \
#      4     5   6    7
#    /  \
#   8     9

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.left.left.left = Node(8)
tree.root.left.left.right = Node(9)
