from collections import defaultdict
from queue import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def verticalOrder(self, root):
    if not root: return
    dict = {}
    res = []

    def bfs(root):
      q = deque([[root,0]])
      while q:
        node,x = q.popleft()
        if x not in dict: dict[x] = []
        dict[x].append(node.val)
        if node.left: q.append([node.left,x-1])
        if node.right: q.append([node.right,x+1])
    bfs(root)
    for x in sorted(dict.keys()):
      res.append(dict[x])
    return res


  def verticalOrder(self, root):
    if not root: return
    dict = defaultdict(list)
    res = []

    q = deque([[root,0]])
    min_x = max_x = 0
    while q:
      node,x = q.popleft()
      dict[x].append(node.val)
      min_x = min(min_x, x)
      max_x = max(max_x, x)
      if node.left: q.append([node.left,x-1])
      if node.right: q.append([node.right,x+1])
    return [dict[x] for x in range(min_x, max_x + 1)]
  

    # def traverse(root,x,y):
    #   if not root: return
    #   if x not in dict: dict[x] = {}
    #   if y not in dict[x]: dict[x][y] = []
    #   dict[x][y].append(root.val)
    #   traverse(root.left, x-1,y+1)
    #   traverse(root.right, x+1,y+1)
    # traverse(root,0,0)
    # res = []
    # for x in sorted(dict.keys()):
    #   lvl = []
    #   for y in sorted(dict[x].keys()):
    #     lvl+=dict[x][y]
    #   res.append(lvl)
    # return res
        