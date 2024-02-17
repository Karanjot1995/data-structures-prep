# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def widthOfBinaryTree(self, root):
    if not root: return 0
    q = [[root,0]]
    max_width = 0

    while q:
      first,last = 0, 0
      # lvl = []
      for i in range(len(q)):
        curr,idx=q.pop(0)
        # lvl.append(idx)
        if i ==0: first = idx
        last = idx
        if curr.left: q.append([curr.left,2*idx])
        if curr.right: q.append([curr.right,2*idx+1])
      max_width = max(max_width, last - first + 1)
    return max_width
  
  def widthOfBinaryTree(self, root):
    if not root: return 0
    q = [[root,0]]
    max_width = 0
    while q:
      min = q[0][1]
      first,last = 0,0
      for i in range(len(q)):
        curr,idx=q.pop(0)
        i = idx-min
        if i==0: first = i
        last = i
        if curr.left: q.append([curr.left,2*i])
        if curr.right: q.append([curr.right,2*i+1])
      max_width = max(max_width, last-first+1)

    return max_width
      
             