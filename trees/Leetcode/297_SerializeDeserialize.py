from queue import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree:
  def __init__(self, root):
    self.root = TreeNode(root)

  def serialize(self,root):
    if not root: return ''
    s = ''
    q = deque([root])
    while q:
      curr = q.popleft()
      if not curr: s+='#,'
      else:
        s+=str(curr.val)+','
        q.append(curr.left)
        q.append(curr.right)
    s = s[:-1]
    return s
    
      

  def deserialize(self, data):
    if len(data)==0: return None
    arr = data.split(',')
    root = TreeNode(arr[0])
    q = deque([root])
    
    i=1
    while q and i<len(arr):
      curr = q.popleft()
      if arr[i]=='#': curr.left = None
      else: 
        curr.left = TreeNode(arr[i])
        q.append(curr.left)
      i+=1
      if arr[i]=='#': curr.right = None
      else:
        curr.right = TreeNode(arr[i])
        q.append(curr.right)
      i+=1
    return root

    return root


       
        
#             1
#           /    \
#         2        3
#       /   \     /  \
#      4     5   6    7
#           / \
#          8   9

tree = Tree(1)
tree.root.left = TreeNode(2)
tree.root.right = TreeNode(3)
tree.root.left.left = TreeNode(4)
tree.root.left.right = TreeNode(5)
tree.root.right.left = TreeNode(6)
tree.root.right.right = TreeNode(7)
tree.root.left.right.left = TreeNode(8)
tree.root.left.right.right = TreeNode(9)

print(tree.serialize(tree.root))
print(tree.deserialize('1,2,3,4,5,6,7,#,#,8,9,#,#,#,#,#,#,#,#'))
