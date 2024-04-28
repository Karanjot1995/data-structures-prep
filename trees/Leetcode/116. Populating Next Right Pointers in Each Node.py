"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
  def connect(self, root):
    if not root: return None
    root.next = None
    q = [root]
    while q:
      size = len(q)
      for i in range(size):
        node = q.pop(0)
        node.next = None
        if i<size-1: node.next = q[0]
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)

    return root
  
  def connect(self, root):
    if not root: return None
    root.next = None
    q = [[root,0]]
    while q:
      size = len(q)
      for i in range(size):
        node,lvl = q.pop(0)
        node.next = None
        if len(q) and q[0][1] == lvl: node.next = q[0][0]
        if node.left: q.append([node.left,lvl+1])
        if node.right: q.append([node.right,lvl+1])

    return root
   

# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A), your function should 
# populate each next pointer to point to its next right node, just like in Figure B. 
# The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

