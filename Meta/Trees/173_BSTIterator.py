# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# https://leetcode.com/problems/binary-search-tree-iterator/

'''
APPROACH 1: BRUTE FORCE (Flattening the BST)
- Do inorder traversal and store all elements in a list

TC - O(N) for constructor; O(1) for next(), hasNext()
SC - O(N)

APPROACH 2: ITERATIVE INORDER DFS

TC - O(1) average for next(); O(1) for hasNext()
SC - O(Height)
'''

# TC -> O(1) and SC -> O(H)
class BSTIterator:
  def __init__(self,root):
    self.stack = []
    self.pushAll(root)

  def pushAll(self, root):
    while root:
      self.stack.append(root)
      root = root.left

  def next(self):
    node = self.stack.pop()
    self.pushAll(node.right)
    return node.val
  
  def hasNext(self):
    return self.stack
  

  # def next(self):
  #   node = self.stack.pop()
  #   # go to right and insert all the left (there will all be greater than the node)
  #   curr = node.right
  #   while curr:
  #     self.stack.append(curr)
  #     curr = curr.left
  #   return node.val
  
  # def prev(self):
  #   node = self.rev_stack.pop()
  #   # go to right and insert all the left (there will all be greater than the node)
  #   curr = node.left
  #   while curr:
  #     self.stack.append(curr)
  #     curr = curr.right
  #   return node.val
          

  



# TC -> O(1) and SC -> O(N)
class BSTIterator:
  def __init__(self, root):
    self.order = self.getInOrder(root)
    self.i = 0

  def getInOrder(self, root):
    order = []
    def traverse(root):
      if not root: return
      traverse(root.left)
      order.append(root.val)
      traverse(root.right)
    traverse(root)
    return order

  def next(self) -> int:
    node = self.order[self.i]
    self.i+=1
    return node
      

  def hasNext(self) -> bool:
    return self.i<len(self.order)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()