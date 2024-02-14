# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def boundaryOfBinaryTree(self, root):
    order = [root.val]

    def leftTraverse(root):
      if not root: return
      if not root.left and not root.right: return
      order.append(root.val)
      if root.left: leftTraverse(root.left)
      elif root.right: leftTraverse(root.right)
    leftTraverse(root.left)
    print(order)

    def leafTraverse(root):
      if not root: return
      if not root.left and not root.right:
        order.append(root.val)
      if root.left: leafTraverse(root.left)
      if root.right: leafTraverse(root.right)
    leafTraverse(root.left)
    leafTraverse(root.right)

    right = []
    def rightTraverse(root):
      if not root: return
      if not root.left and not root.right: return
      right.append(root.val)
      if root.right: rightTraverse(root.right)
      elif root.left: rightTraverse(root.left)
    rightTraverse(root.right)

    for i in range(len(right)-1,-1,-1):
      order.append(right[i])

    return order

        