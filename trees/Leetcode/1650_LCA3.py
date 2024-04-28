"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
  def lowestCommonAncestor(self, p, q):
    path = set()
    while p:
      path.add(p)
      p = p.parent
    while q not in path:
      q = q.parent
    return q
    # p1,p2 = p,q
    # while p1 != p2:
    #   p1 = p1.parent if p1 else q
    #   p2 = p2.parent if p2 else p
    
    # return p1
      
      
        