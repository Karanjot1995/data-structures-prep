
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
  
  def levelOrder(self):
    order = []
    current = self.root
    q = [current]
    while q:
      level = []
      for i in range(len(q)):
        curr = q.pop(0)
        level.append(curr.val)
        if curr.left: q.append(curr.left)
        if curr.right: q.append(curr.right)
      order.append(level)
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
      if curr.left: traverse(curr.left)
      if curr.right: traverse(curr.right)
    traverse(current)
    return order
  
  def preOrderIterative(self):
    order = []
    root = self.root
    if root == None: return
    st = [root]
    while st:
      curr = st.pop()
      order.append(curr.val)
      if curr.right: st.append(curr.right)
      if curr.left: st.append(curr.left)

    return order
  
  def inOrderRecursive(self):
    order = []
    curr = self.root
    def traverse(curr):
      if curr.left: traverse(curr.left)
      order.append(curr.val)
      if curr.right: traverse(curr.right)
    traverse(curr)
    return order
  
  def inOrderIterative(self):
    curr = self.root
    st = []
    order = []
    while True:
      if curr!=None:
        st.append(curr)
        curr = curr.left
      else:
        if not st: break
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
      if curr.left: traverse(curr.left)
      if curr.right: traverse(curr.right)
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
  

  def zigZag(self):
    root = self.root
    if not root: return []
    root = self.root
    order = []
    q = [root]
    leftToright = True
    while q:
      n = len(q)
      level = [0]*n
      for i in range(n):
        node = q.pop(0)
        if node==None: break
        if leftToright: level[i] = node.val
        else: level[n-1-i] = node.val
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
      leftToright = not leftToright
      order.append(level)

    return order
  
  def boundaryTraversal(self):
    root = self.root
    arr = []
    def leftTraverse(root):
      if not root.left and not root.right:
        return
      arr.append(root.val)
      if root.left: leftTraverse(root.left)
      elif root.right: leftTraverse(root.right)
    leftTraverse(root)

    def leafTraverse(root):
      if not root.left and not root.right: 
        arr.append(root.val)
      if root.left: leafTraverse(root.left)
      if root.right: leafTraverse(root.right)
    leafTraverse(root)

    right = []
    def rightTraverse(root):
      if not root.left and not root.right:
        return
      right.append(root.val)
      # arr.append(root.val)
      if root.right: rightTraverse(root.right)
      elif root.left: rightTraverse(root.left)
    rightTraverse(root.right)
    
    for i in range(len(right)-1,-1,-1):
      arr.append(right[i])
    # arr+=right
    return arr
  
  def verticalTraversal(self):
    root = self.root
    dict = {}

    def traverse(root,x,y):
      if not root: return
      if x not in dict: dict[x] = []
      dict[x].append([y,root.val])
      traverse(root.left, x-1, y+1)
      traverse(root.right, x+1, y+1)
       
    traverse(root,0,0)

    def levelOrder(current, x,y):
      q = [[current,0,0]]
      while q:
        popped,x,y= q.pop(0)
        if x not in dict: dict[x] = []
        dict[x].append([y,popped.val])
        if popped.left: q.append([popped.left,x-1,y+1])
        if popped.right: q.append([popped.right,x+1,y+1])

    # levelOrder(root,0,0)

    res = []
    for x in sorted(dict.keys()):
      lvl = []
      for node in sorted(dict[x]):
        lvl.append(node[1])
      res.append(lvl)
    return res     
      
    

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


print('BFS: ',tree.bfs())
print('LevelORder: ',tree.levelOrder())
print('Pre Rec: ',tree.preOrderRecursive())
print('Pre It: ',tree.preOrderIterative())
print('InOrder Rec:', tree.inOrderRecursive())
print('InOrder It:', tree.inOrderIterative())
print('PostOrder Rec:', tree.postOrderRecursive())
print('PostOrder It:', tree.postOrderIterative())
print('PostOrder It2:', tree.postOrderIterativeOneStack())
print('ZigZag: ',tree.zigZag())
print('Boundary Traverse: ',tree.boundaryTraversal())
print('Vertical Traverse:', tree.verticalTraversal())
# print(tree.dfsPre(tree.root))
