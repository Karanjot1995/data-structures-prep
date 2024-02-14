#Given the root of a binary tree, return the leftmost value in the last row of the tree.

class Solution:
  def findBottomLeftValue(self, root) -> int:
    order = []
    q = [root]
    level = 0
    while q:
      lvl = []
      for i in range(len(q)):
        popped = q.pop(0)
        lvl.append(popped.val)
        if popped.left: q.append(popped.left)
        if popped.right: q.append(popped.right)
      order.append(lvl)
      level+=1
    return order[-1][0]    
  

# Input: root = [1,2,3,4,null,5,6,null,null,7]
# Output: 7