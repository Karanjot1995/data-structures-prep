# from queue import PriorityQueue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def distanceK(self, root, target, k):
    parents = {}
    q = [root]
    while q:
      curr = q.pop(0)
      if curr.left: 
        parents[curr.left] = curr
        q.append(curr.left)
      if curr.right: 
        parents[curr.right] = curr
        q.append(curr.right)
    # print(parents)
  
    vis = [target]
    q = [target]
    dis = 0
    while q:
      if dis == k: break
      for i in range(len(q)):
        curr = q.pop(0)
        if curr.left and curr.left not in vis: 
          vis.append(curr.left)
          q.append(curr.left)
        if curr.right and curr.right not in vis: 
          vis.append(curr.right)
          q.append(curr.right)
        if curr in parents and parents[curr] and parents[curr] not in vis:
          vis.append(parents[curr])
          q.append(parents[curr])
      dis+=1

    res = []
    while q:
      curr = q.pop(0)
      res.append(curr.val)
    return res




  # def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
  #   adj = {}
  #   q = [root]
  #   while q:
  #     curr = q.pop(0)
  #     if curr.left: 
  #       if curr.left.val not in adj: adj[curr.left.val] = []
  #       if curr.val not in adj: adj[curr.val] = []
  #       adj[curr.left.val].append(curr.val)
  #       adj[curr.val].append(curr.left.val)
  #       q.append(curr.left)
  #     if curr.right: 
  #       if curr.right.val not in adj: adj[curr.right.val] = []
  #       if curr.val not in adj: adj[curr.val] = []
  #       adj[curr.right.val].append(curr.val)
  #       adj[curr.val].append(curr.right.val)        
  #       q.append(curr.right)

  #   q = [target.val]
  #   vis = [target.val]
  #   j = 0
  #   while q:
  #     if j == k:
  #       return q
  #     for i in range(len(q)):
  #       curr = q.pop(0)
  #       if not adj: break
  #       for nb in adj[curr]:
  #         if nb not in vis:
  #           q.append(nb)
  #           vis.append(nb)
  #     j+=1

  #   return []
        