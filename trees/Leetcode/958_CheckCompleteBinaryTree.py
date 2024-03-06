from collections import deque

class Solution:
  def isCompleteTree(self, root) -> bool:
    q = deque([root])    
    empty_node = False
    while q:
      for i in range(len(q)):
        node = q.popleft()
        if node:
          #if it found a node after an empty node or on the next level
          if empty_node: return False
          q.append(node.left)
          q.append(node.right)
        else: 
          empty_node = True

    return True