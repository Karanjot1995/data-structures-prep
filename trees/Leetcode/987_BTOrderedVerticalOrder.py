# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
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
        