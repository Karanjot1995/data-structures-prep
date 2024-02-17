from queue import deque
from collections import defaultdict 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def amountOfTime(self, root, start) -> int:
    adj = defaultdict(list)
    q = [root]
    while q:
      curr = q.pop()
      if curr.left: 
        adj[curr.left.val].append(curr.val)
        adj[curr.val].append(curr.left.val)
        q.append(curr.left)
      if curr.right: 
        adj[curr.right.val].append(curr.val)
        adj[curr.val].append(curr.right.val)        
        q.append(curr.right)

    queue = deque([start])
    vis = {start}
    t = -1
    while queue:
      for i in range(len(queue)):
        u = queue.popleft()
        if not adj: break
        for v in adj[u]:
          if v not in vis:
            queue.append(v)
            vis.add(v)
      t+=1

    return t
  
  # def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
  #   parents = {}
  #   start_node = None
  #   q = [root]
  #   while q:
  #     curr = q.pop()
  #     if curr.val == start: start_node = curr
  #     if curr.left: 
  #       parents[curr.left] = curr
  #       q.append(curr.left)
  #     if curr.right: 
  #       parents[curr.right] = curr
  #       q.append(curr.right)
  
  #   vis = {start_node}
  #   q=deque([start_node])
  #   t = 0
  #   while q:
  #     fl = 0
  #     for i in range(len(q)):
  #       curr = q.popleft()
  #       if curr.left and curr.left.val not in vis: 
  #         vis.add(curr.left.val)
  #         q.append(curr.left)
  #         fl=1
  #       if curr.right and curr.right.val not in vis: 
  #         vis.add(curr.right.val)
  #         q.append(curr.right)
  #         fl=1
  #       if curr in parents and parents[curr] and parents[curr].val not in vis:
  #         vis.add(parents[curr].val)
  #         q.append(parents[curr])
  #         fl=1
  #     if fl==1: t+=1
  #   return t



        