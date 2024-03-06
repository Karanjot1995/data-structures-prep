# Each node will return min node value, max node value, size
class NodeValue:
    def __init__(self, min_node, max_node, max_size):
        self.max_node = max_node
        self.min_node = min_node
        self.max_size = max_size

class Solution:
  def largest_bst_subtree_helper(self, root):
    # An empty tree is a BST of size 0.
    if not root: return NodeValue(float('inf'), float('-inf'), 0)

    # Get values from left and right subtree of current tree.
    left = self.largest_bst_subtree_helper(root.left)
    right = self.largest_bst_subtree_helper(root.right)
    
    # Current node is greater than max in left AND smaller than min in right, it is a BST.
    if left.max_node < root.val < right.min_node:
      return NodeValue(min(root.val, left.min_node), max(root.val, right.max_node), left.max_size + right.max_size + 1)
    
    # Otherwise, return [-inf, inf] so that parent can't be valid BST
    return NodeValue(float('-inf'), float('inf'), max(left.max_size, right.max_size))

  def largestBSTSubtree(self, root) -> int:
    return self.largest_bst_subtree_helper(root).max_size





#my solution
class Solution:
  def largestBSTSubtree(self, root) -> int:
    if not root: return 0
    if not root.left and not root.right: return 1

    def traverse(root):
      if not root: return {'size':0, 'minNode': float('inf'), 'maxNode':float('-inf') }
      # if not root.left and not root.right: return {'size':1, 'maxNode':root.val, 'minNode': root.val}

      left = traverse(root.left)
      right = traverse(root.right)

      if left['maxNode']<root.val<right['minNode']:
        sz =  1+left['size']+right['size']
        # obj = {'size': sz, 'maxNode':max(root.val,right['maxNode']), 'minNode':  min(root.val,left['minNode'])}
        # print(root.val, obj)
        return {'size': sz, 'minNode':  min(root.val,left['minNode']), 'maxNode':max(root.val,right['maxNode'])}

      return {'size': max(left['size'],right['size']), 'maxNode':float('inf'), 'minNode': float('-inf')}

    return traverse(root)['size']


  #Brute Force
  def isValidBST(self, root) -> bool:
    maxi = float('-inf')
    # order = []
    st = []
    curr = root
    self.cnt = 0
    while True:
      if curr:
        st.append(curr)
        curr = curr.left
      else:
        if not st: break
        node = st.pop()
        self.cnt+=1
        if node.val<=maxi: return 0
        maxi = max(node.val, maxi)
        curr = node.right
    return self.cnt

  def largestBSTSubtreeBrute(self, root):
    if not root: return 0
    # order = []
    bsts = []
    def traverse(root):
      if not root: return
      bsts.append(self.isValidBST(root))
      traverse(root.left)
      traverse(root.right)

    traverse(root)
    return max(bsts)

        