# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from queue import deque

# OPTIMIZED BFS
# TC - O(N) | SC - O(N)
class Solution:
  def verticalTraversal(self, root):
    dict = defaultdict(list)
    ans = []
    q = deque([[root, 0, 0]])
    min_x = max_x = 0
    while q:
      node,x,y = q.popleft()
      min_x = min(min_x, x)
      max_x = max(max_x, x)
      dict[x].append([y, node.val])
      if node.left: q.append([node.left, x-1, y+1])
      if node.right: q.append([node.right, x+1, y+1])

    for x in range(min_x, max_x+1):
      lvl = []
      for node in sorted(dict[x]):
        lvl.append(node[1])
      ans.append(lvl)
    return ans
  
  
  # BRUTE - BFS
  # TC - O(NlogN) | SC - O(N)
  def verticalTraversal(self, root):
    dict = {}
    ans = []

    def traverse(root,x,y):
      if not root: return
      if x not in dict: dict[x] = []
      dict[x].append([y,root.val])
      ans.append([x,y,root.val])
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

    # d=defaultdict(list)
    # for i,j,k in sorted(ans):
    #   d[j].append(k)
    # l=[]
    # for i in d.values():
    #   l.append(i)
    # return l
    res = []
    for x in sorted(dict.keys()):
      lvl = []
      for node in sorted(dict[x]):
        lvl.append(node[1])
      res.append(lvl)
    return res
        